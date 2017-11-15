# -*- coding: utf-8 -*-
__author__ = ["Thiago Lopes", "Daniel Machado", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasilia"
__maintainer__ = "Thiago Lopes"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Nov 14 of 2017"
__version__ = "1.1.0"

import sys

class Get_PArameters():

    def __init__(self, namefile):
        self.file = [x.strip() for x in open(namefile, "r").read().split('\n')]

    def feed_file_corrupted(self):
        print("The feed file is corrupted, please complete it as indicated.")
        sys.exit()

    def find_a_list_pos(self, target):
        pos = -1
        pos_target = -1
        for element in self.file:
            pos += 1
            if target in element:
                pos_target = pos
        return pos_target

    def validad_pos_feed_string(self, target):
        pos = self.find_a_list_pos(target) + 1
        if pos < 0:
            self.feed_file_corrupted()
        while True:
            if self.file[pos] == "->":
                break
            else:
                pos += 1
                continue
        return pos

    def get_names_input(self):
        target = "output files "
        pos = self.validad_pos_feed_string(target)
        files_to_output = self.file[pos].split()[1:]
        return files_to_output[0]

    def get_name_input(self):
        target = "Declare all the files you want"
        pos = self.validad_pos_feed_string(target)
        files_to_output = self.file[pos].split()[1]
        return files_to_output

    def get_wavelenght_range(self):
        target = "beginning of the wavelenght range"
        pos = self.validad_pos_feed_string(target)
        wavelenght_range = self.file[pos].split()[1:2]
        return wavelenght_range

    def get_n_points(self):
        target = "Number of points for wavelenght range"
        pos = self.validad_pos_feed_string(target)
        n_points = self.file[pos].split()[1]
        return n_points

    def get_fwhm(self):
        target = "Full Width at Half Maximum"
        pos = self.validad_pos_feed_string(target)
        fwhm_found = self.file[pos].split()[1]
        return fwhm_found

    def get_chart_title(self):
        target = "Full Width at Half Maximum"
        pos = self.validad_pos_feed_string(target)
        fwhm_found = self.file[pos].split()[1]
        return fwhm_found

    def get_plot_system(self):
        target = "X inside the parenthesis of the chosen"
        pos = self.find_a_list_pos(target)
        if pos < 0:
            self.feed_file_corrupted()
        while True:
            if "gnuplot" in self.file[pos].lower() and "x" in list[pos].lower():
                plot_system = "gnuplot"
                break
            elif "pyplot" in self.file[pos].lower() and "x" in list[pos].lower():
                plot_system = "pyplot"
                break
            else:
                pos += 1
                continue
        return plot_system