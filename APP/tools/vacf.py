# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Ueslei Vasconcelos", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__maintainer__ = ["Thiago Lopes", "Sandro Brito"]
__email__ = ["lopes.th.o@gmail.com", "brittosandro@gmail.com"]
__date__ = "Oct 02 of 2018"
__version__ = "1.0.0"

class Velocity_AutoCor_Function(object):

    def __init__(self, fileName, goalTime, fileTipe = "CPMD"):
        self.fileName = fileName
        self.goalTime = goalTime
        self.fileTipe = fileTipe
        self.N = 1 #número de átomos -> vai ser mudado
        
    def vacf(self, time):
        for atom in self.frames[time]:
            cvv = self.vel(atom, 0) * self.getVel(atom, time)
        cvv = (1/self.N) * cvv

    def getVel(self, atom, time):
        



