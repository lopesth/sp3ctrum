class Get_PArameters():

    def __init__(self, namefile):
        self.file = [x.strip() for x in open(namefile, "r").read().split('\n')]

    def find_a_list_pos(self, target):
        pos = -1
        pos_target = -1
        for element in self.file:
            pos += 1
            if target in element:
                pos_target = pos
        return pos_target

    def get_names_input(self):
        target = "output files "
        pos = self.find_a_list_pos(target)+1
        while True:
            if len(self.file[pos]) == 0:
                pos+=1
                continue
            else:
                break
        files_to_input = self.file[pos].split()[1:]
        return files_to_input