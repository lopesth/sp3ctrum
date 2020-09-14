from sys import argv, platform
from PyQt5.QtWidgets import QApplication
from SP3CTRUM.APP.gui import MainWindow
from SP3CTRUM.APP.analysis_set import Analisys_Settings
from SP3CTRUM.APP.control import ViewController

if __name__ == "__main__":
    if len(argv) == 1:
        app = QApplication(argv)
        analysis_set = Analisys_Settings()
        controller = ViewController(analysis_set)
        gui = MainWindow(platform, controller)
        gui.show()
        app.exec_()
    else:
        if argv[1] != "-nogui":
            gui_interface()
        else:
            pass





