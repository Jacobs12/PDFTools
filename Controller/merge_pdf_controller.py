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


class MergeController(BaseController):
    result_array: [] = []

    def setup_ui(self):
        super().setup_ui()
        self.setup_button()
        self.window.merge_output_field.setText('合并PDF')

    def setup_button(self):
        self.window.merge_start_button.clicked.connect(self.start_button_click)
        self.window.merge_add_button.clicked.connect(self.add_button_click)

    def open_file(self) -> tuple:
        # my_filetypes = [('all files', '.*'), ('text files', '.txt')]
        files = QFileDialog.getOpenFileNames(filter='PDF Files(*.pdf)')
        return files

    def add_button_click(self):
        files = self.open_file()
        lst: [] = files[0]
        print(lst)

    def start_button_click(self):
        print('start')
