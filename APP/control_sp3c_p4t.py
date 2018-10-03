# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Ueslei Vasconcelos", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__maintainer__ = ["Thiago Lopes", "Sandro Brito"]
__email__ = ["lopes.th.o@gmail.com", "brittosandro@gmail.com"]
__date__ = "Set 28 of 2018"
__version__ = "1.0.0"

import sys, os
from APP.tools.start_spc import Opening
from APP.tools.get_osc import Get_Osc
from APP.tools.gaussian_conv import Gaussian_Convolution
from APP.tools.print_spectrum import Print_Spectrum
from APP.tools.get_parameters import Get_Parameters
from APP.tools.get_chart_title import Title_Chart


class Sp3ctrum_UVvis_P4tronum(object):

    def __init__(self, version):
        self.version = version
        Opening(self.version).welcome()
        self.dir = os.getcwd()

    def run_fed_terminal(self, filename):
        feed = Get_Parameters(filename)
        range_wl = feed.get_wavelenght_range()
        start = range_wl[0]
        end = range_wl[1]
        numb_of_points = feed.get_n_points()
        sdt_wl_cm = feed.get_fwhm()
        files_to_combine = feed.get_names_input()
        name_file = feed.get_name_output()
        title = feed.get_chart_title()
        total_oscillators = Get_Osc(files_to_combine).take_osc()
        spectrum = Gaussian_Convolution(total_oscillators, sdt_wl_cm)
        greater_epslon_osc = spectrum.make_spectrum(start, end, numb_of_points)
        spectrum.write_spectrum(name_file)
        Print_Spectrum(self.dir, name_file, start, end, greater_epslon_osc[0], greater_epslon_osc[1], title).print_matplotlib()
        print("\nOK. Have a nice day and enjoy your results.\n")
