"""
EWVtuber
项目名称：虚拟主播软件
版权所有：北京光线传媒股份有限公司
技术支持：北京光线传媒股份有限公司
Editor:fengtao
Mails:fengtao23@mails.ucas.ac.cn
"""
from mainwindow import *


class BaseController(object):
    window: Ui_MainWindow = None

    def __init__(self, window: Ui_MainWindow):
        super().__init__()
        self.window = window
        self.setup_ui()
        self.init()

    def setup_ui(self):
        pass

    def init(self):
        pass
