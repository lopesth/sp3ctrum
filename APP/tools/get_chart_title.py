# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Ueslei Vasconcelos", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasilia and Universidade Federal de Goiás"
__maintainer__ = ["Thiago Lopes", "Sandro Brito"]
__email__ = ["lopes.th.o@gmail.com", "brittosandro@gmail.com"]
__date__ = "Set 28 of 2018"
__version__ = "1.0.0"

import sys

class Title_Chart(object):

    def to_choose(self):
        while True:
            try:
                answer = input(
                    "\nWould you like to post a title on your chart? Type \'yes\' or \'y\' for yes, otherwise, type anything: "
                ).split()[0].lower() in ["y", "yes"]
                break
            except KeyboardInterrupt:
                sys.exit()
            except:
                continue
        if answer:
            self.title = input("Title your title of choice: ")
        else:
            self.title = ""
        return self.title
