# -*- coding: utf-8 -*-
__author__ = ["Thiago Lopes", "Daniel Machado", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasília"
__maintainer__ = "Thiago Lopes"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Nov 14 of 2017"
__version__ = "1.0.1"

from APP.control_sp3c_p4t import Sp3ctrum_UVvis_P4tronum


if (__name__ == "__main__"):

    program = Sp3ctrum_UVvis_P4tronum(__version__)
    program.run()

    