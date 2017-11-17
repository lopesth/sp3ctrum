# -*- coding: utf-8 -*-
__author__ = ["Thiago Lopes", "Daniel Machado", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasilia"
__maintainer__ = "Thiago Lopes"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Nov 17 of 2017"
__version__ = "2.0.1"

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