# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__date__ = "Oct 16 of 2019"
__version__ = "1.0.1"

from SP3CTRUM.APP.TOOLS.start_spc import Opening

class Sp3ctrum_UVvis_P4tronum(object):

    '''
        This class is used to display the initial version of the program when
        we run the graphical interface. It is a class that will always be invoked
        in start the program by the sp3ctrum_app.py module.
    '''

    def __init__(self, version):
        self.version = version
        Opening(self.version).welcome()
