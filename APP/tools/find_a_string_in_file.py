# -*- coding: utf-8 -*-
__author__ = ["Sandro Britto", "Mateus Barbosa", "Ueslei Vasconcelos", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasilia and Universidade Federal de Goiás"
__maintainer__ = ["Thiago Lopes", "Sandro Britoo"]
__email__ = ["lopes.th.o@gmail.com", "brittosandro@gmail.com"]
__date__ = "Set 28 of 2018"
__version__ = "1.0.0"

class Find_a_String(object):

    def __init__(self, file, lookup):
        self.file = file
        self.lookup = lookup

    def return_numbers_of_line(self):
        numbers = []
        with open(self.file) as myFile:
            for num, line in enumerate(myFile):
                if (self.lookup in line):
                    numbers.append(num+1)
        return numbers

    def return_the_line(self):
        lines = []
        with open(self.file) as myFile:
            for num, line in enumerate(myFile):
                if (self.lookup in line):
                    lines.append(line.split('\n')[0])
        return lines
