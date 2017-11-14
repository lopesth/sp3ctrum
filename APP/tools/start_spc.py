# -*- coding: utf-8 -*-
__author__ = ["Thiago Lopes", "Daniel Machado", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasília"
__maintainer__ = "Thiago Lopes"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Nov 14 of 2017"
__version__ = "1.0.1"

import sys

class Opening(object):

    def __init__(self, version):
        self.version = version

    def welcome(self):
        print("             \          |          / ")
        print("\n            _  .\\\\              //._      ")
        print("           _    .\ \          / /.  _           ")
        print("          _    .\  ,\     /` /,.-    _           ")
        print("         _      -.   \  /'/ /  .      _         ")
        print("        _       ` -   `-'  \  -        _        ")
        print("         _        '.       /.\`       _        ")
        print("          _          -    .-         _        ")
        print("           _         :`//.'         _         ")
        print("            _        .`.'          _          ")
        print("              _      .'           _ ")
        print("               _    *            _")
        print("                _  *            _")
        print("                  * ")
        print("                 /^\ ")
        print("           /\    \"V\"")
        print("          /__\    | ")
        print("         //..\\\\   | ")
        print("         \].`[/   |")
        print("         /l\/j\  (|)")
        print("        /. ~~ ,\//| ")
        print("        \\\\L__j^\/ | ")
        print("         \/--v}   | ")
        print("         |    |   | ")
        print("         |    |   | ")
        print("         |    l   | ")
        print("       _/j  L l\_ | \n")
        print("Welcome to UV-vis Sp3ctrum P4tronus (version {}), your favorite UV-vis Spectrum simulation APP through oscillator strength calculations.\n" .format(self.version))
        print("This APP was developed by Thiago Lopes, Daniel Machado, Heibbe Oliveira and made available by the LEEDMOL group (Laboratório de Estrutura Eletrônica e Dinâmica Molecular) of the Institute of Chemistry at the Universidade de Brasília (UnB).\n")
        print("The methodology used in this APP was taken from the source: http://gaussian.com/uvvisplot/")
        print("For now, only calculations coming from the Gaussian package and only with Gaussian convolutions are available to simulate the spectrum.\n")
        print("Make sure all files are in the same Spectrum Patronus folder and are in the output format of the gaussian (\".log\" or \".out\").\n")

class Take_Files(object):

    def __init__(self):
        print("Declare all the files you want to make a spectrum (these files will have their oscillators combined and only one spectrum will be formed).")
        while True:
            try:
                temp_l = input("Type all on a line, separated by commas: ").split(",")
                self.files_to_use = []
                for element in temp_l:
                    self.files_to_use.append(element.strip())
                if len(temp_l[0]) < 1:
                    continue
                    print (len(temp_l[0]))
                else:
                    print("\nThe following files will have their oscillators combined:", end=" ")
                    for x in self.files_to_use:
                        if x == self.files_to_use[-1]:
                            print("{}".format(x), end=".\n")
                        else:
                            print("{}".format(x), end=", ")
                    break

            except KeyboardInterrupt:
                sys.exit()
            except:
                continue


    def get_files(self):
        return self.files_to_use
