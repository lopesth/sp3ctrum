# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Ueslei Vasconcelos", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__maintainer__ = ["Thiago Lopes", "Sandro Brito"]
__email__ = ["lopes.th.o@gmail.com", "brittosandro@gmail.com"]
__date__ = "Set 28 of 2018"
__version__ = "1.0.0"

class Find_a_String(object):

    ''' Class used to handle a file and "remove" strings from interece '''

    def __init__(self, file, lookup):
        self.file = file        # file input
        self.lookup = lookup    # lookup is a string in file

    def return_numbers_of_line(self):

        ''' This method receives a file and a string within it and returns a list
             whose elements are the number of the line in which the string was found. '''

        numbers = []
        with open(self.file) as myFile:
            for num, line in enumerate(myFile):
                if self.lookup in line:
                    numbers.append(num + 1)
        return numbers

    def return_the_line(self):

        ''' This method receives a file and a string within it and returns a list
             whose elements are the lines containing that string.  '''

        lines = []
        with open(self.file) as myFile:
            for line in myFile:
                if self.lookup in line:
                    lines.append(line.split('\n')[0])
        return lines
