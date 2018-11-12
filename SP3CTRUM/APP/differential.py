# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Ueslei Vasconcelos", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__maintainer__ = ["Thiago Lopes", "Sandro Brito"]
__email__ = ["lopes.th.o@gmail.com", "brittosandro@gmail.com"]
__date__ = "Set 28 of 2018"
__version__ = "1.0.0"

class FiniteDifferenceDerivative(object):

    def __init__(self, y_values, x_values):
        f_x = y_values
        x = x_values
        h = abs(x[-2] - x[-1])
        self.firstDerivative = self.__Derivative(f_x, x, h)
        self.criticalpoints = self.__CP()
        self.secondDerivative = self.__Derivative(self.firstDerivative[0], self.firstDerivative[1], h)

    def __Derivative(self, f_x, x, h):
        f_line_x = []
        for i in range(0, len(f_x)-1, 1):
            f_line = (f_x[i + 1] - f_x[i]) / (h)
            f_line_x.append(f_line)
        return [f_line_x, x[0:-1]]

    def __CP(self):
        x2 = 0
        num = 0
        criticalPoints = []
        for x in self.firstDerivative[0]:
            if x == 0:
                x1 = 0
            else:
                x1 = x/abs(x)
            if x2 - x1 == 2:
                criticalPoints.append(self.firstDerivative[1][num-1])
            x2 = x1
            num +=1
        return criticalPoints
