# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__date__ = "Oct 16 of 2019"
__version__ = "1.0.1"

class Opening(object):

    ''' Class used in program display '''

    def __init__(self, version):
        self.version = version

    def welcome(self):
        print("\n             \          |          /   ")
        print("\n            _  .\\\\              //._ ")
        print("           _    .\ \          / /.  _    ")
        print("          _    .\  ,\     /` /,.-    _   ")
        print("         _      -.   \  /'/ /  .      _  ")
        print("        _       ` -   `-'  \  -        _ ")
        print("         _        '.       /.\`       _  ")
        print("          _          -    .-         _   ")
        print("           _         :`//.'         _    ")
        print("            _        .`.'          _     ")
        print("              _      .'           _      ")
        print("               _    *            _       ")
        print("                _  *            _        ")
        print("                  *                      ")
        print("                 /^\                     ")
        print("           /\    \"V\"                   ")
        print("          /__\    |                      ")
        print("         //..\\\\   |                    ")
        print("         \].`[/   |                      ")
        print("         /l\/j\  (|)                     ")
        print("        /. ~~ ,\//|                      ")
        print("        \\\\L__j^\/ |                    ")
        print("         \/--v}   |                      ")
        print("         |    |   |                      ")
        print("         |    |   |                      ")
        print("         |    l   |                      ")
        print("       _/j  L l\_ |                   \n ")
        print("Welcome to UV-vis Sp3ctrum P4tronus (version {}), your favorite UV-vis Spectrum simulation APP through oscillator strength calculations.\n".format(self.version))
        print("This APP was developed by Thiago Lopes, Daniel Machado, Heibbe Oliveira and made available by the LEEDMOL group (Laboratório de Estrutura Eletrônica e Dinâmica Molecular) of the Institute of Chemistry at the Universidade de Brasilia (UnB).\n")
        print("The methodology used in this APP was taken from the source: http://gaussian.com/uvvisplot/")
        print("For now, only calculations coming from the Gaussian package and only with Gaussian convolutions are available to simulate the spectrum.\n")
        print("Make sure all files are in the same Spectrum Patronus folder and are in the output format of the gaussian (\".log\" or \".out\").\n")
