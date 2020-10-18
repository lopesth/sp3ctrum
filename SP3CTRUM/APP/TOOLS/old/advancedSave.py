from SP3CTRUM.APP.TOOLS.textTools import Find_a_String

class saveAdvancedSimple(object):

    '''
       This class handles the data in a file, with the takeStates method and
       writes the data to a new file with the Save method.
    '''

    def __init__(self, fileName, spectrumName, newFile = True, lastTime = True):
        self.fileName = fileName           # type file
        self.spectrumName = spectrumName   # file name
        self.newFile = newFile
        self.lastTime = lastTime
        self.rhfAsw = True if len(Find_a_String(self.fileName, "RHF").return_numbers_of_line()) != 0 else False
        self.takeStates()
        self.save()

    def takeStates(self):

        '''
           This method does not receive parameters, from the data contained in the file
           self.fileName returns a dictionary whose keys describe the state of the
           and values of the dictionary are lists in which the first element indicates
           the orbital involved in the transition and the second elements indicates
           its respective transitions coefficient.
        '''

        lineStates = []
        self.contributeOsc = {}
        poslist = Find_a_String(self.fileName, " Excited State  ").return_numbers_of_line()
        poslist.append(Find_a_String(self.fileName, "SavETr:").return_numbers_of_line()[0])
        fileList = []
        self.excitations = []
        with open(self.fileName,  encoding="utf8", errors='ignore') as myFile:
            for line in myFile:
                fileList.append(line.split('\n')[0])
        num = 1
        for i in range(len(poslist)-1):
            self.excitations.append(fileList[poslist[i]-1])
            contribute = []
            for lineNum in range(poslist[i], poslist[i+1]):
                contribLine = []
                contribLine1 = fileList[lineNum].split("->")
                for contribLine1_1 in contribLine1:
                    for contribLine1_2 in contribLine1_1.split():
                        contribLine.append(contribLine1_2)
                try:
                    int(contribLine[0])
                    contribute.append([" to ".join(contribLine[0:2]), float(contribLine[2])])
                except:
                        pass
            self.contributeOsc.update({num : contribute})
            num += 1

    def save(self):

        '''
           This method is used to record a file with the calculated states
           and the respective contributions of each expo in percentage.
        '''

        wName = "------ Advanced Data from file " + self.fileName.split("/")[-1] + " ------"

        self.finalName = self.spectrumName.split("_spectrum.dat")[0] + "_advancedData.dat"

        if self.newFile:
            saveFile = open(self.finalName, "w")
        else:
            saveFile = open(self.finalName, "a")

        lineW = ("".join( "_" for num1 in range(0, len(wName)))) # creat a line

        saveFile.write("{}\n\n{}\n\n{}\n\n".format(lineW, wName, lineW))
        saveFile.write(" Excitation energies and oscillator strengths:\n\n")
        saveFile.write("                   Wavelenght (nm)  Oscillator Force\n")

        for excitationNumber in sorted(self.contributeOsc.keys()):
            lineSplited = self.excitations[excitationNumber-1].split()
            saveFile.write(" Excited State {:02d}:     {}            {} \n".format(excitationNumber,
                                                                                   lineSplited[6],
                                                                                   lineSplited[8].split('=')[1]))
        saveFile.write("\nContribution of the pairs of orbitals in the electronic excitation:\n")

        if self.rhfAsw:
            for excitationNumber in sorted(self.contributeOsc.keys()):
                saveFile.write("Excitation Number {:02d}:\n" .format(excitationNumber))
                for contibution in self.contributeOsc[excitationNumber]:
                    # Molecular orbitals with the contribution percentage of each oscillator
                    saveFile.write("       M.O. {}  -> {:6.2f}%\n" .format(contibution[0], 200*contibution[1]**2))
                saveFile.write("\n")
        else:
            saveFile.write("The UV-Vis Sp3ctrum P4tronus only calculates the contribution of the pairs of orbitals in the electronic excitation in Restricted Shell systems.\n")
        if self.lastTime:
            with open(self.finalName, encoding="utf8", errors='ignore') as myFile:
                saveFile.write("{}\n\n ---------------------- UV-Vis Spectrum -----------------------\n\n{}\n".format(lineW, lineW))
                saveFile.write("         Wavelength               Molar Absorptivity\n")
                saveFile.write("            (nm)                      (L/mol.cm)\n")
                for line in myFile:
                    saveFile.write("           %s\n" %("                       ".join(line.split())))
                stream = open(self.spectrumName.split("_spectrum.dat")[0] + "_spectrum.dat").readlines()
                for line in stream:
                    saveFile.write(line)
        saveFile.close()
