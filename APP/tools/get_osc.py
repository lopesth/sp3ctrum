# -*- coding: utf-8 -*-
__author__ = ["Thiago Lopes", "Daniel Machado", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasilia"
__maintainer__ = "Thiago Lopes"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Nov 17 of 2017"
__version__ = "2.0.1"

from APP.tools.find_a_string_in_file import Find_a_String
from APP.tools.sort_key_maps import Sort_Map

class Get_Osc(object):

    def __init__(self, files):
        self.list_of_files = files

    def take_osc(self):
        self.list_wl = []
        self.osc_map = {}
        for file_to_grep in self.list_of_files:
            lines = Find_a_String(file_to_grep, " Excited State  ").return_the_line()
            for line in lines:
                wl_nm = float(line.split()[6])
                osc_str = float(line.split()[8].split("=")[-1])
                if (wl_nm in self.list_wl):
                    x = []
                    for element in self.osc_map[wl_nm]:
                        x.append(element)
                    x.append(osc_str)
                    self.osc_map.update({wl_nm: x})
                else:
                    self.osc_map.update({wl_nm : [osc_str]})
                self.list_wl.append(wl_nm)

        return Sort_Map(self.osc_map).sort_by_keys()




