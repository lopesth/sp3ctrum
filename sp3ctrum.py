from sys import argv, platform
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from SP3CTRUM.APP.GUI.gui import MainWindow


if __name__ == "__main__":
    if len(argv) == 1:
        app = QApplication(argv)
        app.setWindowIcon(QIcon('./SP3CTRUM/styles/icon/icon.png'))
        gui = MainWindow(platform)
        gui.show()
        app.exec_()
    else:
        if argv[1] != "-nogui":
            gui_interface()
        else:
            pass





