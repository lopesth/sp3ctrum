# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Ueslei Vasconcelos", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__maintainer__ = ["Thiago Lopes", "Sandro Brito"]
__email__ = ["lopes.th.o@gmail.com", "brittosandro@gmail.com"]
__date__ = "Set 28 of 2018"
__version__ = "1.0.0"

from APP.tools.find_a_string_in_file import Find_a_String 

class saveAdvancedSimple(object):

    def __init__(self, fileName, spectrumName, newFile = True, lastTime = True):
        self.lastTime = lastTime
        self.newFile = newFile
        self.fileName = fileName
        self.spectrumName = spectrumName
        self.rhfAsw = True if len(Find_a_String(self.fileName, "RHF").return_numbers_of_line()) != 0 else False
        self.takeStates()
        self.save()

    def takeStates(self):
        lineStates = []
        self.contributeOsc = {}
        poslist = Find_a_String(self.fileName, " Excited State  ").return_numbers_of_line()
        poslist.append(Find_a_String(self.fileName, "SavETr").return_numbers_of_line()[0])
        fileList = []
        self.excitations = []
        with open(self.fileName,  encoding="utf8", errors='ignore') as myFile:
            for line in myFile:
                fileList.append(line.split('\n')[0])
        num = 1
        for i in range(0, len(poslist)-1):
            self.excitations.append(fileList[poslist[i]-1])
            contribute = []
            for lineNum in range(poslist[i], poslist[i+1]):
                try:  
                    contribLine = fileList[lineNum].split()
                    int(contribLine[0])
                    contribute.append([" to ".join([element for element in fileList[lineNum].split()[0:3] if element != "->"]), float(contribLine[3])])
                except:
                    try: 
                        int(fileList[lineNum].split()[2].split(":")[0])
                    except:
                        pass
            self.contributeOsc.update({num : contribute})
            num += 1
    
    def save(self):
        wName = "------ Advanced Data from file " + self.fileName.split("/")[-1] + " ------"
        if self.newFile:
            saveFile = open(self.spectrumName.split("_spectrum.dat")[0]+"_advancedData.dat", "w")
        else:
            saveFile = open(self.spectrumName.split("_spectrum.dat")[0]+"_advancedData.dat", "a")
        lineW = ("".join( "_" for num1 in range(0, len(wName))))
        saveFile.write("{}\n\n{}\n\n{}\n\n".format(lineW, wName, lineW))
        saveFile.write(" Excitation energies and oscillator strengths:\n\n")
        saveFile.write("                   Wavelenght (nm)  Oscillator Force\n")
        for excitationNumber in sorted(self.contributeOsc.keys()):
            lineSplited = self.excitations[excitationNumber-1].split()
            saveFile.write(" Excited State {:02d}:     {}            {} \n" .format(excitationNumber, lineSplited[6], lineSplited[8].split('=')[1])) 
        saveFile.write("\nContribution of the pairs of orbitals in the electronic excitation:\n")
        if self.rhfAsw:
            for excitationNumber in sorted(self.contributeOsc.keys()):
                saveFile.write("Excitation Number {:02d}:\n" .format(excitationNumber))
                for contibution in self.contributeOsc[excitationNumber]:
                    saveFile.write("       M.O. {}  -> {:6.2f}%\n" .format(contibution[0], 200*contibution[1]**2))
                saveFile.write("\n")
        else:
            saveFile.write("The UV-Vis Sp3ctrum P4tronus only calculates the contribution of the pairs of orbitals in the electronic excitation in Restricted Shell systems.\n")
        if self.lastTime:
            with open(self.spectrumName, encoding="utf8", errors='ignore') as myFile:
                saveFile.write("{}\n\n ---------------------- UV-Vis Spectrum -----------------------\n\n{}\n". format(lineW, lineW))
                saveFile.write("         Wavelength               Molar Absorptivity\n")
                saveFile.write("            (nm)                      (L/mol.cm)\n")
                for line in myFile:
                    saveFile.write("           %s\n" %("                       ".join(line.split())))
        saveFile.close()






if __name__ == "__main__":
    x = saveAdvancedSimple("/Users/thiagolopes/Downloads/Acroleina_water_15_1c.log", "/Users/thiagolopes/Downloads/downloads_1_spectrum.dat")
