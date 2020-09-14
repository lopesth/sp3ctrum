

class ViewController():

    def __init__(self, analysis_settings):
        self._as = analysis_settings


    @property
    def analysis_settings(self):
        return self.__as
