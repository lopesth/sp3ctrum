# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Ueslei Vasconcelos", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__maintainer__ = ["Thiago Lopes", "Sandro Brito"]
__email__ = ["lopes.th.o@gmail.com", "brittosandro@gmail.com"]
__date__ = "Set 28 of 2018"
__version__ = "1.0.0"

from find_a_string_in_file import Find_a_String 

class saveAdvancedSimple(object):

    def __init__(self, fileName, spectrumName):
        self.fileName = fileName
        self.spectrumName = spectrumName
        self.rhfAsw = True if len(Find_a_String(self.fileName, "RHF").return_numbers_of_line()) != 0 else False
        self.takeStates()

    def takeStates(self):
        lineStates = []
        self.contributeOsc = {}
        poslist = Find_a_String(self.fileName, "Excited state symmetry").return_numbers_of_line()
        poslist.append(Find_a_String(self.fileName, "SavETr").return_numbers_of_line()[0])
        fileList = []
        self.excitations = []
        with open(self.fileName,  encoding="utf8", errors='ignore') as myFile:
            for line in myFile:
                fileList.append(line.split('\n')[0])
        num = 1
        for i in range(0, len(poslist)-1):
            contribute = []
            for lineNum in range(poslist[i], poslist[i+1]):
                try:  
                    contribLine = fileList[lineNum].split()
                    int(contribLine[0])
                    contribute.append([fileList[lineNum].split("  ")[2], float(contribLine[2])])
                except:
                    try: 
                        int(fileList[lineNum].split()[2].split(":")[0])
                        self.excitations.append(fileList[lineNum])
                    except:
                        pass
            self.contributeOsc.update({num : contribute})
            num += 1
    
    def save(self):
        saveFile = open(self.spectrumName.split("_spectrum.dat")[0]+"_advancedData.dat", "w")

        with open(self.spectrumName, encoding="utf8", errors='ignore') as myFile:
            saveFile.write("               UV-Vis Spectrum\n")
            saveFile.write("  Wavelength                     Molar Absorptivity\n")
            saveFile.write("     (nm)                            (L/mol.cm)\n")
            for line in myFile:
                saveFile.write("%s" %(line))
        
        
        saveFile.close()






if __name__ == "__main__":
    x = saveAdvancedSimple("/Users/thiagolopes/Downloads/Acroleina_water_15_1c.log", "/Users/thiagolopes/Downloads/downloads_1_spectrum.dat").save()
