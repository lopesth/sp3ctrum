
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
