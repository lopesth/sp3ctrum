

class ViewController():

    def __init__(self, analysis_settings):
        self.__as = analysis_settings
        self.__tabs = []

    def __check_state(self, state):
        if state == 'on':
            return True
        else:
             return False

    @property
    def analysis_settings(self):
        return self.__as

    def def_prime_guide(self, guide):
        self.prime_guide = guide 

    def add_tab_toWindows(self, tab):
        self.__tabs.append(tab)

    def __try_if_has_att(self, attribute, command, state):
        if hasattr(self, attribute):
            command(state)
        else:
            print("The prime guide has not been defined in the View Controller!")

    def set_analysis_button_state(self, state):
        state = self.__check_state(state)
        command = self.prime_guide.button_make_analysis.setEnabled
        self.__try_if_has_att("prime_guide", command, state)

    def set_plot_button(self, state):
        state = self.__check_state(state)
        command = self.prime_guide.button_plot_results.setEnabled
        self.__try_if_has_att("prime_guide", command, state)
        
    def set_save_data_button(self, state):    
        state = self.__check_state(state)
        command = self.prime_guide.button_save_data.setEnabled
        self.__try_if_has_att("prime_guide", command, state)

    def set_save_analysis_setting_button(self, state):
        state = self.__check_state(state)
        command = self.prime_guide.button_save_analysis_s.setEnabled
        self.__try_if_has_att("prime_guide", command, state)