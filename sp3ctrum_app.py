# -*- coding: utf-8 -*-
__author__ = ["Thiago Lopes", "Daniel Machado", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasília"
__maintainer__ = "Thiago Lopes"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Nov 14 of 2017"
__version__ = "1.0.1"

from APP.control_sp3c_p4t import Sp3ctrum_UVvis_P4tronum
import sys

def control_the_flux(choice_interface):
    program = Sp3ctrum_UVvis_P4tronum(__version__)
    if choice_interface == "-file":
        pass
        #program.run_powered_terminal
    elif choice_interface == "-friendly":
        program.run_friendly_terminal()
    elif choice_interface == "-gui" or choice_interface == "-gui":
        pass
        #program.run_gui()


if (__name__ == "__main__"):
    choice_interface = sys.argv[-1]
    control_the_flux(choice_interface)


    