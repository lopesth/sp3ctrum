# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Ueslei Vasconcelos", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__maintainer__ = ["Thiago Lopes", "Sandro Brito"]
__email__ = ["lopes.th.o@gmail.com", "brittosandro@gmail.com"]
__date__ = "Oct 02 of 2018"
__version__ = "1.0.0"

from matplotlib import pyplot

class Velocity_AutoCor_Function(object):

    def __init__(self, fileName, goalFrame, fileTipe = "CPMD"):
        self.fileName = fileName
        self.goalFrame = goalFrame
        self.fileTipe = fileTipe
        self.N = 0
        self.takeValues()
        self.velocities = []
        for frame in self.frames:
            self.velocities.append(self.vacf(frame))
        
    def takeValues(self):
        atomN = 0
        frameList = []
        self.frames = []
        totalLength = 0
        with open(self.fileName, "r", encoding="utf8", errors = "ignore") as myFile: 
            for num, line in enumerate(myFile):
                lineS = line.split()
                if int(lineS[0]) != atomN:
                    if len(frameList) != 0:
                        self.frames.append(frameList)
                        if self.N == 0:
                            self.N = len(self.frames[0])
                            totalLength = self.N * self.goalFrame
                    atomN = int(lineS[0])
                    frameList = []
                    frameList.append(lineS[4:])
                else:
                    frameList.append(lineS[4:])
                    if num+1 == totalLength:
                        self.frames.append(frameList)
                        break
        if self.goalFrame > len(self.frames):
            print("The TRAJECT file has " + str(len(self.frames)+1) + " frames, so there is no way to use " + str(self.goalFrame) + " frames.")
            exit()

    def vacf(self, frame):
        cvv = 0
        for atom in range(0, self.N):
            cvv = cvv + (self.escalarProductVector(self.frames[0][atom], frame[atom]) )
        return (1/self.N) * cvv

    def escalarProductVector(self, vector1, vector2):
        return float(vector1[0]) * float(vector2[0]) + float(vector1[1]) * float(vector2[1]) + float(vector1[2]) * float(vector2[2])

    def vectorMagnitude(self, vector):
        return (float(vector[0])**2 + float(vector[1])**2 + float(vector[2])**2) ** (0.5)


if __name__ == "__main__":
    y = Velocity_AutoCor_Function("/Users/thiagolopes/Downloads/TRAJECTORY", 9000).velocities
    y_max = max(y)
    yNorm = [element/y_max for element in y]
    x = [x_i for x_i in range(1, 9000+1)]
    plot = pyplot.plot(x, yNorm)
    #pyplot.show()
    teste = open("/Users/thiagolopes/Downloads/teste.csv", "w")
    for x2, y2 in zip(x, yNorm):
        teste.write("{}, {}\n".format(x2, y2))
    