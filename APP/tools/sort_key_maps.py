# -*- coding: utf-8 -*-
__author__ = ["Sandro Britto", "Mateus Barbosa", "Ueslei Vasconcelos", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasilia and Universidade Federal de Goiás"
__maintainer__ = ["Thiago Lopes", "Sandro Britoo"]
__email__ = ["lopes.th.o@gmail.com", "brittosandro@gmail.com"]
__date__ = "Set 28 of 2018"
__version__ = "1.0.0"

class Sort_Map(object):

    def __init__(self, map):
        self.map = map

    def sort_by_keys(self):
        sorted_map = {}
        key_list = list(self.map.keys())
        key_list.sort()
        for element in key_list:
            sorted_map.update({element : self.map[element]})
        return sorted_map
