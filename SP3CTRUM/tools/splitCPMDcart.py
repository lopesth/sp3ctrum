# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Ueslei Vasconcelos", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__maintainer__ = ["Thiago Lopes", "Sandro Brito"]
__email__ = ["lopes.th.o@gmail.com", "brittosandro@gmail.com"]
__date__ = "Oct 09 of 2018 - 17:18:12"
__version__ = "1.0.0"

from os import getcwd
from sys import argv, platform

PERIODIC_TABLE = {1: "H", 2: "He", 3: "Li", 4: "Be", 5: "B", 6: "C", 7: "N", 8: "O", 9: "F", 10: "Ne", 11: "Na", 12: "Mg", 13: "Al", 14: "Si", 15: "P", 16: "S", 17: "Cl", 18: "Ar", 19: "K", 20: "Ca",
                  21: "Sc", 22: "Ti", 23: "V", 24: "Cr", 25: "Mn", 26: "Fe", 27: "Co", 28: "Ni", 29: "Cu", 30: "Zn", 31: "Ga", 32: "Ge", 33: "As", 34: "Se", 35: "Br", 36: "Kr", 37: "Rb", 38: "Sr", 39: "Y",
                  40: "Zr", 41: "Nb", 42: "Mo", 43: "Tc", 44: "Ru", 45: "Rh", 46: "Pd", 47: "Ag", 48: "Cd", 49: "In", 50: "Sn", 51: "Sb", 52: "Te", 53: "I", 54: "Xe", 55: "Cs", 56: "Ba", 57: "La", 58: "Ce", 59: "Pr",
                  60: "Nd", 61: "Pm", 62: "Sm", 63: "Eu", 64: "Gd", 65: "Tb", 66: "Dy", 67: "Ho", 68: "Er", 69: "Tm", 70: "Yb", 71: "Lu", 72: "Hf", 73: "Ta", 74: "W", 75: "Re", 76: "Os", 77: "Ir", 78: "Pt", 79: "Au",
                  80: "Hg", 81: "Tl", 82: "Pb", 83: "Bi", 84: "Po", 85: "At", 86: "Rn", 87: "Fr", 88: "Ra", 89: "Ac", 90: "Th", 91: "Pa", 92: "U", 93: "Np", 94: "Pu", 95: "Am", 96: "Cm", 97: "Bk", 98: "Cf", 99: "Es",
                  100: "Fm", 101: "Md", 102: "No", 103: "Lr", 104: "Rf", 105: "Db", 106: "Sg", 107: "Bh", 108: "Hs", 109: "Mt", 110: "Ds", 111: "Rg", 112: "Cn", 113: "Uut", 114: "Fl", 115: "Uup", 116: "Lv", 117: "Uus", 118: "Uuo", 119: "Uue", 120: "Ubn"}

class Atom(object):
    def __init__(self, atomType, xPos, yPos, ZPos, freezeCode=0):
        self.__atomType = atomType 
        self.__xPos = float(xPos)
        self.__yPos = float(yPos)
        self.__zPos = float(ZPos)
        self.__freezeCode = int(freezeCode)

    def returnAtomType(self):
        return self.__atomType
    
    def returnXPos(self):
        return self.__xPos

    def returnYPos(self):
        return self.__yPos

    def returnZPos(self):
        return self.__zPos

    def returnPos(self):
        return [self.__xPos, self.__yPos, self.__zPos]
    
    def returnAtom(self):
        return [self.__atomType, self.__xPos, self.__yPos, self.__zPos]

    def returnFreezeCode(self):
        return self.__freezeCode

    def returnReadableAtom(self):
        return "    ".join([self.__atomType, str(self.__xPos), str(self.__yPos), str(self.__zPos)])

    def moveAtom(self, newX, newY, newZ):
        self.__xPos = newX
        self.__yPos = newY
        self.__zPos = newZ

class Molecule(object):
    def __init__(self, charge = 0, multiplicity =  1):
        self.__atoms = []
        self.__charge = int(charge)
        self.__multiplicity = int(multiplicity)

    def addAtom(self, atom):
        self.__atoms.append(atom)

    def returnAtom(self, number):
        return self.__atoms[number]

    def returnAllAtoms(self):
        return self.__atoms

    def returnReadableMolecule(self):
        return "\n".join([x.returnReadableAtom() for x in self.__atoms])

    def returnCharge(self):
        return self.__charge

    def returnMultiplicity(self):
        return self.__multiplicity

    def returnMassCenter(self):
        atoms = []
        posAtoms = []
        for i in range(0, len(self.__atoms)):
            atomType = self.__atoms[i].returnAtomType()
            atomMass = Convert_Period_Table([], atomType).symbol_to_number()
            atoms.append(atomMass)
            posAtoms.append(self.__atoms[i].returnPos())
        mass =  MassCenterOfSet(atoms, posAtoms).returnMassCenter()
        return mass

class Convert_Period_Table(object):

    def __init__(self, atomic_number = [], atomic_symbol = []):
        self.atomic_number = atomic_number
        self.atomic_symbol = atomic_symbol

    def symbol_to_number(self):
        temp = list(PERIODIC_TABLE.values())
        result = []
        for symbol in self.atomic_symbol:
            nao_contem = True
            contador = 0
            for element in temp:
                if (symbol == element):
                    pos = 0
                    for number in list(PERIODIC_TABLE.keys()):
                        if (pos == contador):
                            result.append(number)
                        pos +=1
                        nao_contem = False
                    break
                contador +=1
            if (nao_contem):
                result.append(0)
        return result

    def number_to_symbol(self):
        result = []
        for number in self.atomic_number:
            try:
                result.append(PERIODIC_TABLE[number])
            except:
                result.append("???")
        return result

class ReadTheFrames(object):

    def __init__(self, filename, fullpath):
        self.fileName = fullpath+"/"+filename
        try:
            f = open(self.fileName)
            f.close()
        except:
            print("The {} file was not found in the {} path" .format(filename, fullpath))
            exit(0)
        self.frames = self.takeFrames()

    def takeFrames(self):
        molecule = Molecule()
        allFrames = {}
        stepNumber = 0
        with open(self.fileName, "r") as myFile: 
            for line in myFile:
                lineS = line.split()
                if len(lineS) > 1:
                    if lineS[0] == "STEP:":
                        stepNumber = int(lineS[1])
                        molecule = Molecule()
                    else:
                        molecule.addAtom(Atom(lineS[0], float(lineS[1]), float(lineS[2]), float(lineS[3])))
                else:
                    if len(molecule.returnAllAtoms()) > 0:
                        allFrames.update({stepNumber:molecule})
                    else:
                        pass
        return allFrames

def selSteps(stepsNumbers, allframes):
    selectedSteps = {}
    for number in stepsNumbers:
        selectedSteps.update({number : allframes[number]})
    return selectedSteps

def selFrames(stepNumbers, allframes):
    selectedFrames = {}
    number = 1
    for frame in list(allframes.values()):
        if number in stepNumbers:
            selectedFrames.update({number : frame})
        number +=1
    return selectedFrames

def takeCommands():
    try:
        filename = argv[1]
        if platform == "win32":
            place = "\\".join(filename.split("\\")[0:-1])
            if len(place) > 0:
                pass
            else:
                place = getcwd()
                filename = place + "\\" + filename
        else:
            place = "/".join(filename.split("/")[0:-1])
            if len(place) > 0:
                pass
            else:
                place = getcwd()
                filename = place + "/" + filename
        if argv[2] == "-step":
            return ["step", [int(argv[3])], place, filename]
        elif argv[2] == "-steps":
            return ["step", [int(x) for x in " ".join(argv[3:]).split(',')], place, filename]
        elif argv[2] == "-steprange":
            return ["stepRange", int(argv[3]), place, filename]
        elif argv[2] == "-frame":
            return ["frame", [int(argv[3])], place, filename]    
        elif argv[2] == "-frames":     
            return ["step", [int(x) for x in " ".join(argv[3:]).split(',')], place, filename]     
        elif argv[2] == "-framerange":     
            return ["frameRange", int(argv[3]), place, filename]
        else:
            print("\n-----------------------------------------------------------------\nType:\n  > python splitCPMDcart.py $FILE $COMMAND $TYPE\n\n    $FILE: the file name with the full file path (If the file is at the same address as splitCPMDcart.py, you do not need to place the Address.)\n\nOptions:\n    $COMMAND: -step $TYPE: chosen step to take the geometry from Traject.xyz\n    $COMMAND: -steps $TYPE: chosen steps (separated by commas) to take the geometry from Traject.xyz\n    $COMMAND: -steprange $TYPE: separation interval of all steps along the file Traject.xyz\n    $COMMAND: -frame $TYPE: chosen frame to take the geometry from Traject.xyz\n    $COMMAND: -frames $TYPE: chosen frames (separated by commas) to take the geometry from Traject.xyz\n    $COMMAND: -framerange $TYPE: separation interval of all frames along the file Traject.xyz\n-----------------------------------------------------------------\n")
            exit(0)

    except:
        print("\n-----------------------------------------------------------------\nType:\n  > python splitCPMDcart.py $FILE $COMMAND $TYPE\n\n    $FILE: the file name with the full file path (If the file is at the same address as splitCPMDcart.py, you do not need to place the Address.)\n\nOptions:\n    $COMMAND: -step $TYPE: chosen step to take the geometry from Traject.xyz\n    $COMMAND: -steps $TYPE: chosen steps (separated by commas) to take the geometry from Traject.xyz\n    $COMMAND: -steprange $TYPE: separation interval of all steps along the file Traject.xyz\n    $COMMAND: -frame $TYPE: chosen frame to take the geometry from Traject.xyz\n    $COMMAND: -frames $TYPE: chosen frames (separated by commas) to take the geometry from Traject.xyz\n    $COMMAND: -framerange $TYPE: separation interval of all frames along the file Traject.xyz\n-----------------------------------------------------------------\n")
        exit(0)

def printXYZ(geom, basicName):
    filE = open(basicName, "w")
    for atom in geom.returnAllAtoms():
        a = atom.returnAtom()
        filE.write("{:>s} {:>14.7f} {:>14.7f} {:>14.7f}\n". format(a[0], a[1], a[2], a[3]))
    filE.close()

if __name__ == "__main__":
    choices = takeCommands()
    filename = choices[3]
    choiceTake = choices[0]
    place = choices[2] + "\\" if platform == "win32" else choices[2] + "/"
    x = ReadTheFrames("TRAJEC.xyz", "/Users/thiagolopes/Downloads/").frames
    if choiceTake == "stepRange":
        stepsINfile = list(x.keys())
        stepstoTake = list(range(choices[1]+1, list(x.keys())[-1], choices[1]))
        stepsNframes = set(stepsINfile) & set(stepstoTake)
    elif choiceTake == "frameRange":
        stepsNframes = list(range(choices[1], len(x.keys()), choices[1]))
    else:
        stepsNframes = choices[1]
    y = selFrames(stepsNframes, x)
    if choiceTake == "step" or choiceTake == "steps" or choiceTake == "stepRange":
        nameBasic = "step"
    else:
        nameBasic = "frame"
    for pos in list(y.keys()):
        printXYZ(y[pos], place+nameBasic+"_"+str(pos)+".car")
    print("The files were saved in the directory {}" .format(place))
