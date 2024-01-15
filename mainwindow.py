# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from Controller.merge_pdf_controller import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('PDF转换')
        self.setup_button()

    def setup_button(self):
        self.ui.tab_button_word.clicked.connect(self.word_button_click)
        self.ui.tab_button_excel.clicked.connect(self.excel_button_click)
        self.ui.tab_button_ppt.clicked.connect(self.ppt_button_click)
        self.ui.tab_button_split.clicked.connect(self.split_button_click)
        self.ui.tab_button_merge.clicked.connect(self.merge_button_click)
        self.merge_button_click()

    merge_controller = None
    def word_button_click(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def excel_button_click(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def ppt_button_click(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def split_button_click(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def merge_button_click(self):
        if self.merge_controller is None:
            self.merge_controller = MergeController(self.ui)
        self.ui.stackedWidget.setCurrentIndex(4)

