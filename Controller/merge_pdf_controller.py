"""
EWVtuber
项目名称：虚拟主播软件
版权所有：北京光线传媒股份有限公司
技术支持：北京光线传媒股份有限公司
Editor:fengtao
Mails:fengtao23@mails.ucas.ac.cn
"""
from Controller.base_cotroller import *
from PySide6.QtWidgets import QFileDialog
from pypdf import PdfWriter
from Utils.thread import *


class MergeController(BaseController):
    result_array: [] = []
    output_folder: str = ''

    def setup_ui(self):
        super().setup_ui()
        self.setup_button()
        self.window.merge_output_field.setText('合并PDF')

    def setup_button(self):
        self.window.merge_start_button.clicked.connect(self.start_button_click)
        self.window.merge_add_button.clicked.connect(self.add_button_click)
        self.window.merge_folder_button.clicked.connect(self.select_output_folder)
        self.window.merge_up_button.clicked.connect(self.up_button_click)
        self.window.merge_down_button.clicked.connect(self.down_button_click)
        self.window.merge_delete_button.clicked.connect(self.delete_button_click)

    def open_file(self) -> tuple:
        # my_filetypes = [('all files', '.*'), ('text files', '.txt')]
        files = QFileDialog.getOpenFileNames(filter='PDF Files(*.pdf)')
        return files

    def add_button_click(self):
        files = self.open_file()
        lst: [] = files[0]
        if len(lst) == 0:
            return
        if self.output_folder == '':
            path: str = lst[0]
            path_split = path.split('/')
            path_split.remove(path_split[len(path_split) - 1])
            output_folder = '/'.join(path_split)
            self.output_folder = output_folder
            self.window.merge_output_label.setText(output_folder)
            print(output_folder)
        print(lst)
        self.result_array.extend(lst)
        self.reload()

    def select_output_folder(self):
        target = QFileDialog.getExistingDirectory(dir=self.output_folder)
        if target is None or target == '':
            return
        self.output_folder = target
        self.window.merge_output_label.setText(target)

    def reload(self):
        self.window.merge_listwidget.clear()
        row = 0
        for item in self.result_array:
            obj: str = item
            arr = obj.split('/')
            file_name = arr[len(arr) - 1]
            title = f'{file_name}  >>（{obj}）'
            # self.window.merge_listwidget.insertItem(row, title)
            self.window.merge_listwidget.addItem(title)
            row += 1

    def up_button_click(self):
        index = self.window.merge_listwidget.currentRow()
        if index <= 0:
            return
        obj = self.result_array[index]
        self.result_array.remove(obj)
        self.result_array.insert(index - 1, obj)
        self.reload()
        self.window.merge_listwidget.setCurrentRow(index - 1)
        print(index)

    def down_button_click(self):
        index = self.window.merge_listwidget.currentRow()
        print(self.window.merge_listwidget.count())
        if index < 0 or index >= self.window.merge_listwidget.count() - 1:
            return
        obj = self.result_array[index]
        self.result_array.remove(obj)
        self.result_array.insert(index + 1, obj)
        self.reload()
        self.window.merge_listwidget.setCurrentRow(index + 1)
        print(index)

    def delete_button_click(self):
        index = self.window.merge_listwidget.currentRow()
        if index < 0 or index > self.window.merge_listwidget.count() - 1:
            return
        obj = self.result_array[index]
        self.result_array.remove(obj)
        self.reload()
        index += 1
        if index > len(self.result_array) - 1:
            index = len(self.result_array) - 1
        self.window.merge_listwidget.setCurrentRow(index)

    def start_button_click(self):
        print('start')
        if '转换中' in self.window.merge_start_button.text():
            return
        if len(self.result_array) <= 0:
            return
        self.window.merge_start_button.setText('转换中...')
        if self.window.merge_output_field.text() == '':
            self.window.merge_output_field.setText('你把文件名删了干啥')
        thread = EWThread()

        def process():
            print('转换中')
            self.merger_pdf(source=self.result_array)

        def finished():
            print('转换完成')
            self.window.merge_start_button.setText('开始转换')

        thread.start(process_handler=process, completion_handler=finished)

    merger = PdfWriter()

    def merger_pdf(self, source: [] = []):
        if self.merger is None:
            self.merger = PdfWriter()
        if len(source) == 0:
            return
        for pdf in source:
            self.merger.append(pdf)
        target = f'{self.output_folder}/{self.window.merge_output_field.text()}.pdf'
        self.merger.write(target)
        self.merger.close()
        self.merger = None
