# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__date__ = "Oct 16 of 2019"
__version__ = "1.0.1"

from SP3CTRUM.APP.find_a_string_in_file import Find_a_String
from SP3CTRUM.APP.sort_key_maps import Sort_Map

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




