# -*- coding: utf-8 -*-
__author__ = ["Thiago Lopes", "Daniel Machado", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasilia"
__maintainer__ = "Thiago Lopes"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Nov 17 of 2017"
__version__ = "3.0"

class FiniteDifferenceDerivative(object):

    def __init__(self, y_values, x_values):
        self.f_x = y_values
        self.x = x_values
        self.h = abs(self.x[-2]-self.x[-1])

    def symmetricDerivative(self):
        f_line_x = []
        for i in range(1, len(self.f_x)-1):
            f_line = (self.f_x[i+1] - self.f_x[i-1])/(2*self.h)
            f_line_x.append(f_line)
        return [f_line_x, self.x[1:-1]]

    def regularDerivative(self):
        f_line_x = []
        for i in range(0, len(self.f_x)-1, 1):
            f_line = (self.f_x[i + 1] - self.f_x[i]) / (self.h)
            f_line_x.append(f_line)
        return [f_line_x, self.x[0:-1]]

