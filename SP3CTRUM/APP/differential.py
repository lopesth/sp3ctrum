# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__date__ = "Oct 16 of 2019"
__version__ = "1.0.1"

from numpy import gradient, array

class FiniteDifferenceDerivative(object):

    def __init__(self, y_values, x_values):
        f_x = y_values
        x = x_values
        self.firstDerivative = self.__Derivative(f_x, x)
        self.secondDerivative = self.__Derivative(self.firstDerivative[0], self.firstDerivative[1])
        self.criticalpoints = self.__CP(self.secondDerivative[0], x_values)


    def __Derivative(self, f_x, x):
        y = array(f_x)
        x = array(x)
        return gradient(y, x, edge_order=2), x

    def __near(self, lista, rangeAc):
        test = []
        for n in range(1, len(lista)):
            if abs(lista[n] - lista[n-1]) < rangeAc:
                return True
            else:
                pass
        return False

    def __CP(self, yvalues, xvalues):
        criticalPoints = []
        yvalues = [round(y, 2) for y in yvalues]
        for n in range(1, len(yvalues)-1):
            if abs(yvalues[n]) > 0.5:
                if yvalues[n] < yvalues[n-100]:
                    if yvalues[n] < yvalues[n+100]:
                        if yvalues[n] < yvalues[n-50]:
                            if yvalues[n] < yvalues[n+50]:
                                if yvalues[n] < yvalues[n-5]:
                                    if yvalues[n] < yvalues[n+5]:
                                        if yvalues[n] < yvalues[n-1]:
                                            if yvalues[n] < yvalues[n+1]:
                                                if yvalues[n] < 0:
                                                    criticalPoints.append(xvalues[n])
        if self.__near(criticalPoints, 5) == False:
            realCriticalPoints = criticalPoints
        else: 
            realCriticalPoints = []
        while self.__near(criticalPoints, 5):
            listA = []
            y = 0
            for x in range(0, len(criticalPoints)):
                if abs(criticalPoints[x] - criticalPoints[x-1]) < 2:
                    if y == 0:
                        y = criticalPoints[x]
                        listA.append(criticalPoints[x])
                        listA.append(criticalPoints[x-1])
                    elif criticalPoints[x] - y < 5:
                        listA.append(criticalPoints[x])
                    else:
                        pass
                else:
                    realCriticalPoints.append(criticalPoints[x])
            realCriticalPoints.append(min(listA))
            for e in listA:
                if e in criticalPoints:
                    criticalPoints.remove(e)
        return realCriticalPoints
