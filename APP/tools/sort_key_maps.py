# -*- coding: utf-8 -*-
__author__ = "Thiago Lopes and LEEDMOL group"
__credits__ = ["LOPES, T. O.", "OLIVEIRA, H. C. B."]
__maintainer__ = "Thiago Lopes"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Nov 11 of 2017"
__version__ = "1.0"

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
