"""
EWVtuber
项目名称：虚拟主播软件
版权所有：北京光线传媒股份有限公司
技术支持：北京光线传媒股份有限公司
Editor:fengtao
Mails:fengtao23@mails.ucas.ac.cn
"""
import sys
import mainwindow

from mainwindow import *
from PySide6.QtGui import QIcon

# pyinstaller --noconsole --icon=Assets/Icon/icon.png app.py
def application_start():
    """

    :param self:
    """
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('Assets/Icon/icon.png'))  # 设置窗口的头标
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application_start()
