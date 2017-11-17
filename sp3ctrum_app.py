# -*- coding: utf-8 -*-
__author__ = ["Thiago Lopes", "Daniel Machado", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasilia"
__maintainer__ = "Thiago Lopes"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Nov 14 of 2017"
__version__ = "1.1.0"

from APP.control_sp3c_p4t import *
from APP.tools.sp3ctrum_gui import *
from tkinter import *


def control_the_flux(choice_interface, file_name):
    program = Sp3ctrum_UVvis_P4tronum(__version__)
    if choice_interface == "-file":
        program.run_fed_terminal(file_name)
    elif choice_interface == "-friendly":
        program.run_friendly_terminal()
    elif choice_interface == "-gui" or choice_interface == "":
        root = Tk()
        root.title("Sp3ctrum")
        app = Application(root)
        mainloop()
    else:
        print("Unrecognized Keyword")
        print("Type -file, -friendly or -gui.")
        sys.exit()


if (__name__ == "__main__"):
    choice_interface = sys.argv[1]
    try:
        file_name = sys.argv[2]
    except:
        file_name = ""
    control_the_flux(choice_interface, file_name)


