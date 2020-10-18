
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


class Find_a_String(object):

    ''' Class used to handle a file and "remove" strings from interece '''

    def __init__(self, file, lookup):
        self.file = file        # file input
        self.lookup = lookup    # lookup is a string in file

    def return_numbers_of_line(self):

        ''' This method receives a file and a string within it and returns a list
             whose elements are the number of the line in which the string was found. '''

        numbers = []
        with open(self.file) as myFile:
            for num, line in enumerate(myFile):
                if self.lookup in line:
                    numbers.append(num + 1)
        return numbers

    def return_the_line(self):

        ''' This method receives a file and a string within it and returns a list
             whose elements are the lines containing that string.  '''

        lines = []
        with open(self.file) as myFile:
            for line in myFile:
                if self.lookup in line:
                    lines.append(line.split('\n')[0])
        return lines
