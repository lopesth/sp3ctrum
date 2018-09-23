# -*- coding: utf-8 -*-
__author__ = ["Sandro Britto", "Mateus Barbosa", "Ueslei Vasconcelos", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasilia and Universidade Federal de Goiás"
__maintainer__ = ["Thiago Lopes", "Sandro Britoo"]
__email__ = ["lopes.th.o@gmail.com", "brittosandro@gmail.com"]
__date__ = "Set 28 of 2018"
__version__ = "1.0.0"

from APP.tools.find_a_string_in_file import Find_a_String
from APP.tools.sort_key_maps import Sort_Map

class Get_Osc(object):

    def __init__(self, files):
        self.list_of_files = files

    def take_osc(self, start_wl, end_wl):
        self.list_wl = []
        self.osc_map = {}
        for file_to_grep in self.list_of_files:
            lines = Find_a_String(file_to_grep, " Excited State  ").return_the_line()
            for line in lines:
                wl_nm = float(line.split()[6])
                osc_str = float(line.split()[8].split("=")[-1])
                if float(wl_nm) < float(start_wl) or float(wl_nm) > float(end_wl):
                    pass
                elif (wl_nm in self.list_wl):
                    x = []
                    for element in self.osc_map[wl_nm]:
                        x.append(element)
                    x.append(osc_str)
                    self.osc_map.update({wl_nm: x})
                else:
                    self.osc_map.update({wl_nm : [osc_str]})
                self.list_wl.append(wl_nm)
        return Sort_Map(self.osc_map).sort_by_keys()




