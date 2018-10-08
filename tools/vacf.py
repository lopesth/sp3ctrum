# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Ueslei Vasconcelos", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__maintainer__ = ["Thiago Lopes", "Sandro Brito"]
__email__ = ["lopes.th.o@gmail.com", "brittosandro@gmail.com"]
__date__ = "Oct 02 of 2018"
__version__ = "1.0.0"

from matplotlib import pyplot
from sys import argv
from numpy import fft
import warnings
warnings.filterwarnings("ignore")

class Velocity_AutoCor_Function(object):

    def __init__(self, fileName, goalFrame, fileTipe = "CPMD"):
        self.fileName = fileName
        self.goalFrame = goalFrame
        self.fileTipe = fileTipe
        self.N = 0
        self.FrameTime = []
        self.velocities = []
        self.takeValues()
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
                    self.FrameTime.append(atomN)
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

    def returnFrames(self):
        return self.FrameTime
    
    def returnVelocities(self):
        return self.velocities

    def vacf(self, frame):
        cvv = 0
        for atom in range(0, self.N):
            cvv = cvv + (self.escalarProductVector(self.frames[0][atom], frame[atom]) )
        return (1/self.N) * cvv

    def escalarProductVector(self, vector1, vector2):
        return float(vector1[0]) * float(vector2[0]) + float(vector1[1]) * float(vector2[1]) + float(vector1[2]) * float(vector2[2])

    def vectorMagnitude(self, vector):
        return (float(vector[0])**2 + float(vector[1])**2 + float(vector[2])**2) ** (0.5)

def leaveWithError():
    print("\n-----------------------------------------------------------------\nFor the correct execution of the tool type:\n\n  > python vacf_sp3ctrum.py -file FILE -steps MAX_STEPS -norm RESP -color HEX_RGB\n\nNote: This tool requires the 3.5 as a minimum version of Python\n-----------------------------------------------------------------\n")
    exit(0)

def vacf(filename, MaxSteps):
    target = Velocity_AutoCor_Function(filename, MaxSteps)
    return [target.returnVelocities(), target.returnFrames()]

def normalize(target):
    maxValue = max(target)
    return [element/maxValue for element in target]

def fourierTr(target):
    targetFourier = fft.fft(target)
    leng = int(len(targetFourier)/1.2)
    return targetFourier[0:leng]

def plot(x, y, place, nameFig, colorTaked):
    toPlot = pyplot.plot(x, y, color=colorTaked)
    pyplot.ylabel(nameFig)
    pyplot.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
    pyplot.xlabel("Steps")
    pyplot.savefig(place+"/"+nameFig+".png", dpi=300, transparent=True, format="png")
    pyplot.close()

def printFile(coordinates, abscissaRAW, abscissaFFT, place, var):
    fileW = open(place+"/result_vacf.dat", "w")
    fileW.write("Cutting point for non-correlated steps: {} ({} Frames)\nVariance around the cutting point: {:8.5e}\n\n" .format(var[0], var[1], var[2]))
    fileW.write("{:>8s} {:>20.10s} {:>20.10s}\n".format("Frames", "VACF", "FFT of VACF"))
    for x, y1, y2 in zip(coordinates, abscissaRAW, abscissaFFT):
        fileW.write("{:>8d} {:>20.10e} {:20.10e}\n".format(x, y1, y2))

def two_pass_variance(data):
    sum_data1 = sum_data2 = 0
    n = len(data)
    for x in data:
        sum_data1 += x.real
    mean = sum_data1/n

    for x in data:
        sum_data2 += (x.real - mean)*(x.real - mean)

    variance = sum_data2 / (n - 1)
    return variance*100

def var(f, x, n):
    n = n/10
    t = int(len(f)/n)
    start = 0
    variance = []
    i = 0
    while True:
        i += 1
        end = i*t
        try:
            variance.append(two_pass_variance(f[start:end]))
            start = end
        except:
            break
    i_list = []
    for i in range(1, len(variance)+1):
        if variance[i-1] < 0.0001:
            i_list.append(i-1)
    try:
        return [x[(i_list[0]+1)*t], t*(i_list[0]+1), variance[i_list[0]]]
    except:
        print("The convergence criterion has not been reached. Use a bigger number of Frames.")
        exit(0)

def controlFlux(filename, n, normAw, color):
    place = "/".join(filename.split("/")[0:-1])
    vacf_RAW = vacf(filename, n)
    y = vacf_RAW[0]
    x = vacf_RAW[1]
    plot(x, y, place, "VACF", color)
    leng = int(len(x)/1.2)
    x = x[0:leng]
    f = fourierTr(y).real
    if normAw:
        f = normalize(f)
    plot(x, f, place, "FFT of VACF", color)
    v = var(f, x, n)
    printFile(x, y, f, place, v)

if __name__ == "__main__":
    try:
        if argv[1] == "-file" and argv[3] == "-steps" and argv[5] == "-norm":
            filename = str(argv[2])
            n = int(argv[4])
            normAw = True if argv[6].lower() == "yes" else False
            try:
                color = argv[8]
            except:
                color = "#FF0000"
            controlFlux(filename, n, normAw, color)
        else:
            leaveWithError()
    except:
        leaveWithError()
