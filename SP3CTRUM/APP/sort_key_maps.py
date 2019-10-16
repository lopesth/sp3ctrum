# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__date__ = "Oct 16 of 2019"
__version__ = "1.0.1"

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
