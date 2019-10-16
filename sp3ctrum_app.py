# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__date__ = "Oct 16 of 2019"
__version__ = "1.0.1"

from SP3CTRUM.APP.control_sp3c_p4t import *
from SP3CTRUM.APP.sp3ctrum_gui import *
from tkinter import *

def control_the_flux(choice_interface, file_name):
    program = Sp3ctrum_UVvis_P4tronum(__version__)

    if choice_interface == "-file":
        program.run_fed_terminal(file_name)

    elif choice_interface == "-gui" or choice_interface == "":
        root = Tk()
        root.title("UV-Vis Sp3ctrum P4tronum " + __version__)
        app = Application(root).mainloop()

    else:
        print("Unrecognized Keyword")
        print("Type -gui or -file.")
        sys.exit()

if __name__ == "__main__":

    try:
        choice_interface = sys.argv[1]
        file_name = sys.argv[2]
    except:
        try:
            if choice_interface == "-gui" or choice_interface == "":
                file_name = ""
        except:
            choice_interface = ""
            file_name = ""

    control_the_flux(choice_interface, file_name)
