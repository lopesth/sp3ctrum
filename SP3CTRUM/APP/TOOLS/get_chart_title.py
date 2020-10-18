# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__date__ = "Oct 16 of 2019"
__version__ = "1.0.1"

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
