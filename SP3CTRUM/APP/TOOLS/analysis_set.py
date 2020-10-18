class Analysis_Settings(object):
    
    def __init__(self, gui_interface) -> None:
        self.__gui = gui_interface
        self.__files = []
        self.__g09_out_files = True
        self.__depend_iput_files = False
        self.__wl_range = [150, 350]
        self.__grid_points = 300
        self.__fwhm = 3226.22
        self.__spec_int_method = 0
        self.__beers_law_par = [1.000, -2, 1.000]
        self.__chart_title = ""
        self.__curve_colors = ['#E01E23', '#573280', '#945055', '#005CB8', '#29000A', '#000000']
        self.__oscil_colors = ['#E01E23', '#573280', '#945055', '#005CB8', '#29000A', '#000000']
        self.__overlapping_plots = False
        self.__plot_label = False
        
        ### Talvez eu retire essa parte
        self.__base_name_output_files = ""
        self.__fig_res = 150
        self.__file_format = 1
        ####
        
        self.__plot_overl_exp_data = False
        self.__exp_file_data_name = None
        self.__find_fwhm = False
        self.__plot_exp_data_curve = True
        self.__exp_data_color = '#E01E23'
        self.__points_exp_values_wl = [None, None, None, None]
        self.__points_exp_values_molar_abs = [None, None, None, None]

    @property
    def files(self):
        return self.__files
    
    @files.setter
    def files(self, values):
        self.__files = values

    @property
    def gaussian_output_files(self):
        return self.__g09_out_files
    
    @gaussian_output_files.setter
    def gaussian_output_files(self, value):
        self.__g09_out_files = value

    @property
    def dependence_input_files(self):
        return self.__depend_iput_files
    
    @dependence_input_files.setter
    def dependence_input_files(self, value):
        self.__depend_iput_files = value
    
    @property
    def start_of_wl_interval(self):
        return self.__wl_range[0]
    
    @start_of_wl_interval.setter
    def start_of_wl_interval(self, value):
        self.__wl_range[0] = value

    @property
    def end_of_wl_interval(self):
        return self.__wl_range[1]
    
    @end_of_wl_interval.setter
    def end_of_wl_interval(self, value):
        self.__wl_range[1] = value
    
    @property
    def grid_points(self):
        return self.__grid_points

    @grid_points.setter
    def grid_points(self, value):
        self.__grid_points = value

    @property
    def fwhm(self):
        return self.__fwhm
    
    @fwhm.setter
    def fwhm(self, value):
        self.__fwhm = value

    @property
    def spectrum_intensity_method(self):
        return self.__spec_int_method

    @spectrum_intensity_method.setter
    def spectrum_intensity_method(self, value):
        self.__spec_int_method = value

    @property
    def beer_s_law_concetration(self):
        return (self.__beers_law_par[0], self.__beers_law_par[1])
    
    @beer_s_law_concetration.setter
    def beer_s_law_concetration(self, values):
        self.__beers_law_par[0] = values[0]
        self.__beers_law_par[1] = values[1]
        
    @property
    def beer_s_law_pathlength(self):
        return self.__beers_law_par[2]
    
    @beer_s_law_pathlength.setter
    def beer_s_law_pathlength(self, value):
        self.__beers_law_par[2] = value

    @property
    def chart_title(self):
        return self.__chart_title
    
    @chart_title.setter
    def chart_title(self, value):
        self.__chart_title = value
        
    @property
    def curve_colors(self):
        return self.__curve_colors
    
    @curve_colors.setter
    def curve_colors(self, values):
        self.__curve_colors = values
    
    @property
    def oscillators_colors(self):
        return self.__oscil_colors

    @oscillators_colors.setter
    def oscillators_colors(self, values):
        self.__oscil_colors = values

    @property
    def overlapping_plots_answer(self):
        return self.__overlapping_plots

    @overlapping_plots_answer.setter
    def overlapping_plots_answer(self, value):
        self.__overlapping_plots = value

    @property
    def plot_labeling_answer(self):
        return self.__plot_label

    @plot_labeling_answer.setter
    def plot_labeling_answer(self, value):
        self.__plot_label = value


    ### Talvez eu retire essa parte
    @property
    def output_base_name(self):
        return self.__base_name_output_files
    
    @output_base_name.setter
    def output_base_name(self, value):
        self.__base_name_output_files = value
        
    @property
    def figure_resolution(self):
        return self.__fig_res
    
    @figure_resolution.setter
    def figure_resolution(self, value):
        self.__fig_res = value
        
    @property
    def figure_file_format(self):
        return self.__file_format
    
    @figure_file_format.setter
    def figure_file_format(self, value):
        self.__file_format = value
    ####

    @property
    def overlapping_exp_data_answer(self):
        return self.__plot_overl_exp_data

    @overlapping_exp_data_answer.setter
    def overlapping_exp_data_answer(self, value):
        self.__plot_overl_exp_data = value

    @property
    def filenam_exp_data_file(self):
        return self.__exp_file_data_name

    @filenam_exp_data_file.setter
    def filenam_exp_data_file(self, value):
        self.__exp_file_data_name = value

    @property
    def find_fwhm_answer(self):
        return self.__find_fwhm

    @find_fwhm_answer.setter
    def find_fwhm_answer(self, value):
        self.__find_fwhm = value

    @property
    def plot_exp_data_as_a_curve(self):
        return self.__plot_exp_data_curve

    @plot_exp_data_as_a_curve.setter
    def plot_exp_data_as_a_curve(self, value):
        self.__plot_exp_data_curve = value

    @property
    def exp_plot_color(self):
        return self.__exp_data_color

    @exp_plot_color.setter
    def exp_plot_color(self, value):
        self.__exp_data_color = value

    @property
    def exp_molar_abs_points(self):
        return self.__points_exp_values_molar_abs

    @exp_molar_abs_points.setter
    def exp_molar_abs_points(self, value):
        self.__points_exp_values_molar_abs = value

    @property
    def exp_wl_points(self):
        return self.__points_exp_values_wl

    @exp_wl_points.setter
    def exp_wl_points(self, value):
        self.__points_exp_values_wl = value

    def save(self, filename):
        pass
    
    def open(self, filename):
        pass