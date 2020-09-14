


class Analisys_Settings():
    def __init__(self):
        self.__files = []
    
    @property
    def file_list(self):
        return self.__files
    
    @file_list.setter
    def file_list(self, file_list):
        self.__files =  file_list
