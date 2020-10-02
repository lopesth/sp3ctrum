from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QIntValidator, QDoubleValidator
from os import popen

box_title = "QGroupBox::title  { subcontrol-origin: margin; font-size: 12px; subcontrol-position: top ,left; }"

def selectStyle(styleFile):
    f = open("./SP3CTRUM/styles/"+styleFile)
    style = f.read()
    f.close()
    return style

class MainWindow(QMainWindow):
    
     def __init__(self, os_name, controller, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Sp3ctrum Wizard")
        self.table_widget = MyTableWidget(self, controller)
        self.setCentralWidget(self.table_widget)
        self.table_widget.add_new_tab(Table1, "Files") # Table 0 in table_list
        self.table_widget.add_new_tab(Table2, "Spectrum Parameters") # Table 1 in table_list
        self.table_widget.add_new_tab(Table3, "Plot Details") # Table 2 in table_list
        self.table_widget.add_new_tab(Table4, "Versus Experimental Values") # Table 3 in table_list
        layout = QGridLayout()
        
class MyTableWidget(QWidget):
    
    def __init__(self, parent, controller):
        super(QWidget, self).__init__(parent)
        self.control = controller
        self.control.def_prime_guide(self)
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tab_list = []
        self.__buildTabs()
        self.__make_final_buttons_area()
        
    def add_new_tab(self, tab, tab_name):
        self.tab_list.append(tab(self.control))
        self.tabs.addTab(self.tab_list[-1],tab_name)

    def __buildTabs(self):
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def __make_final_buttons_area(self):
        self.buttons_part = QWidget()
        layout = QHBoxLayout()

        self.button_make_analysis = QPushButton()
        self.button_make_analysis = QPushButton("Make Analysis", self)
        self.button_make_analysis.setToolTip("Make the chosen analysis.")
        self.button_make_analysis.clicked.connect(self.__make_analysis)

        self.button_plot_results = QPushButton()
        self.button_plot_results = QPushButton("Plot the results", self)
        self.button_plot_results.setToolTip("Plot the results obtained from the analysis.")
        self.button_plot_results.clicked.connect(self.__plot_results)

        self.button_save_data = QPushButton()
        self.button_save_data = QPushButton("Save the Data", self)
        self.button_save_data.setToolTip("Save all results to auxiliary files that can be used in other programs.")
        self.button_save_data.clicked.connect(self.__save_data)


        self.button_save_analysis_s = QPushButton()
        self.button_save_analysis_s = QPushButton("Save the Analysis settings", self)
        self.button_save_analysis_s.setToolTip("Save a file with the analysis of the settings that can be used to create a consistency between consecutive analyzes of the same research.")
        self.button_save_analysis_s.clicked.connect(self.__save_as)

        layout.addWidget(self.button_make_analysis)
        layout.addWidget(self.button_plot_results)
        layout.addWidget(self.button_save_data)
        layout.addWidget(self.button_save_analysis_s)


        self.button_make_analysis.setEnabled(False)
        self.button_plot_results.setEnabled(False)
        self.button_save_data.setEnabled(False)


        self.buttons_part.setLayout(layout)
        self.layout.addWidget(self.buttons_part)

    def __make_analysis(self):
        pass

    def __plot_results(self):
        pass

    def __save_as(self):
        pass

    def __save_data(self):
        pass

    def __create_final_buttons_area2(self):
        tab_part = QWidget()
        layout = QVBoxLayout()

        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part, 4 ,1)

class Table1(QWidget):
    
    def __init__(self, controller):
        super(QWidget, self).__init__()
        self.control = controller
        self.layout = QGridLayout()
        self.__create_input_file_box()
        self.__create_type_of_input_files()
        self.__create_file_list_area()
        self.__file_button_and_logo_area()
        self.layout.setHorizontalSpacing(5)
        self.layout.setVerticalSpacing(25)
        self.setLayout(self.layout)

    def __create_input_file_box(self):
        tab_part = QGroupBox("Input File Type:")
        tab_part.setStyleSheet(box_title)
        self.__button_type_file_g09 = QRadioButton("Gaussian files")
        self.__button_type_file_g09.setToolTip("Output files from G09 or G16 with theoretical photophysical data.")
        self.__button_type_file_g09.setChecked(True)
        layout = QHBoxLayout()
        layout.addStretch()
        layout.addWidget(self.__button_type_file_g09)
        layout.addStretch()
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part, 1, 0) 

    def __create_type_of_input_files(self):
        tab_part = QGroupBox("Choose the type of input files:")
        tab_part.setStyleSheet(box_title)
        self.__button_indep_files = QRadioButton("Independent")
        self.__button_indep_files.setToolTip("For each file a different analysis will be applied, resulting in different results.")
        self.__button_dep_files = QRadioButton("Dependent")
        self.__button_dep_files.setToolTip("All files will be used for the same analysis, resulting in a single result.")
        self.__button_indep_files.setChecked(True)
        layout = QHBoxLayout() 
        layout.addWidget(self.__button_indep_files)
        layout.addWidget(self.__button_dep_files)
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part, 1 ,1)

    def __file_button_and_logo_area(self):
        self.__button_files = QPushButton("Choose Files", self)
        self.__button_files.setToolTip("Select the files to be used in the analysis.")
        self.__button_files.clicked.connect(self.selectFiles_click)
        tab_part = QWidget()
        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(self.__button_files)
        label_logo = QLabel(self)
        label_name = QLabel(self)
        label_name.setText("Sp3ctrum Wizard!")
        label_name.setStyleSheet("QLabel{font-weight: bold; qproperty-alignment: AlignCenter; font-size: 20px;}")
        pixmap_logo = QPixmap('./SP3CTRUM/styles/icon/sp3ctrum_gray.svg')
        label_logo.setPixmap(pixmap_logo)
        label_logo.setScaledContents(True)
        layout.addWidget(label_logo)
        layout.addWidget(label_name)
        layout.addStretch()
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part, 3 ,1)
        
    def __create_file_list_area(self):
        tab_part = QGroupBox("Selected Files:")
        tab_part.setStyleSheet(box_title)
        layout = QVBoxLayout()
        self.fileList = QListWidget()
        layout.addWidget(self.fileList)
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part, 3 ,0)

    def selectFiles_click(self):
        if self.__button_type_file_g09.isChecked():
            files_to_take = "Gaussian Output Files (*.out *.log)"
        else:
            files_to_take = "Gaussian Output Files (*.out *.log)"
        fname = QFileDialog.getOpenFileNames(self, 'Open file', '', files_to_take)
        self.__clear_file_list()
        self.__fill_file_list(fname[:-1][0])
        self.control.set_analysis_button_state('on')
        
    def __clear_file_list(self):
        self.fileList.clear()

    def __fill_file_list(self, files):
        self.control.analysis_settings.file_list = files
        for i in range(0,len(files)):
            size = int(len(files[i]) * .6)
            item = QListWidgetItem()
            item.setText("..."+files[i][size:])
            item.setToolTip(files[i])
            self.fileList.addItem(item)

class Table2(QWidget):
    
    def __init__(self, controller):
        super(QWidget, self).__init__()
        self.control = controller
        self.layout = QVBoxLayout()
        self.__create_wavelenght_box()
        self.__fwhm_box()
        self.__spectum_method_box()
        self.__beers_law_box()
        self.setLayout(self.layout)
        
    def __create_wavelenght_box(self):
        tab_part = QGroupBox("Parameters of the wavelength range:")
        tab_part.setStyleSheet(box_title)
        layout = QVBoxLayout()
        
        tab_part2 = QWidget()
        layout2 = QHBoxLayout()
        layout2.addStretch()
        nm_label, start_nm_text, end_nm_text = QLabel(self), QLabel(self), QLabel(self)
        nm_label.setText("nm. ")
        start_nm_text.setText("The analysis and plot will be done using the range from ")
        end_nm_text.setText("nm to")
        self.__n_points_label1, self.__n_points_label2 = QLabel(self), QLabel(self)
        self.__n_points_label1.setText("The analysis must be done with a grid of")
        self.__n_points_label2.setText("points.")
        self.__r_start, self.__r_end = QLineEdit(), QLineEdit()
        self.__r_start.setText('150')
        self.__r_start.setMaximumWidth(45)
        self.__r_start.setValidator(QIntValidator())
        self.__r_start.setMaxLength(4)
        self.__r_start.setAlignment(Qt.AlignRight)
        layout2.addWidget(start_nm_text)
        layout2.addWidget(self.__r_start)
        self.__r_end.setText('350')
        self.__r_end.setMaximumWidth(45)
        self.__r_end.setValidator(QIntValidator())
        self.__r_end.setMaxLength(4)
        self.__r_end.setAlignment(Qt.AlignRight)
        layout2.addWidget(end_nm_text)
        layout2.addWidget(self.__r_end)
        layout2.addWidget(nm_label)
        layout2.addStretch()
        tab_part2.setLayout(layout2)
        
        tab_part3 = QWidget()
        layout3 = QHBoxLayout()
        layout3.addStretch()
        self.__n_points = QLineEdit()
        self.__n_points.setText('300')
        self.__n_points.setMaximumWidth(45)
        self.__n_points.setValidator(QIntValidator())
        self.__n_points.setMaxLength(4)
        self.__n_points.setAlignment(Qt.AlignRight)
        layout3.addWidget(self.__n_points_label1)
        layout3.addWidget(self.__n_points)
        layout3.addWidget(self.__n_points_label2)
        layout3.addStretch()
        tab_part3.setLayout(layout3)
        
        layout.addWidget(tab_part2)
        layout.addWidget(tab_part3)
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part)
    
    def __fwhm_box(self):
        tab_part = QGroupBox("Full Width at Half Maximum:")
        tab_part.setStyleSheet(box_title)
        layout = QHBoxLayout()
        label1, label2, self.__hwhm_entry = QLabel(self), QLabel(self), QLineEdit()
        label1.setText("FWHM value: ")
        label2.setText("cm<sup>-1</sup>")
        self.__hwhm_entry.setText('3226.22')
        self.__hwhm_entry.setMaximumWidth(70)
        self.__hwhm_entry.setValidator(QDoubleValidator())
        self.__hwhm_entry.setMaxLength(8)
        self.__hwhm_entry.setAlignment(Qt.AlignRight)
        layout.addStretch()
        layout.addWidget(label1)
        layout.addWidget(self.__hwhm_entry)
        layout.addWidget(label2)
        layout.addStretch()
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part)
    
    def __spectum_method_box(self):
        tab_part = QGroupBox("Spectrum Intensity Method:")
        tab_part.setStyleSheet(box_title)
        layout = QHBoxLayout()
        self.__spectrum_method_b1 = QRadioButton("Relative Intensity")
        self.__spectrum_method_b1.setToolTip("In this method, the ordinate axis is shown with a relative intensity, normalized by the highest value oscillator.")
        self.__spectrum_method_b1.clicked.connect(self.__turn_off_beer_law)
        self.__spectrum_method_b2 = QRadioButton("Estimated Molar Attenuation Coefficient")
        self.__spectrum_method_b2.setToolTip("In this method the ordinate axis is shown with an estimated (molar absorptivity, using the fwhm and the oscillators of the analysis.")
        self.__spectrum_method_b2.clicked.connect(self.__turn_off_beer_law)
        self.__spectrum_method_b3 = QRadioButton("Estimated Absorbance")
        self.__spectrum_method_b3.setToolTip("In this method, there is a previous calculation of molar absorptivity and this value is used, via Beer's law, to calculate the Absorbance for each point on the graph.")
        self.__spectrum_method_b3.clicked.connect(self.__turn_on_beer_law)
        self.__spectrum_method_b1.setChecked(True)
        layout = QHBoxLayout() 
        layout.addStretch()
        layout.addWidget(self.__spectrum_method_b1)
        layout.addWidget(self.__spectrum_method_b2)
        layout.addWidget(self.__spectrum_method_b3)
        layout.addStretch()
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part)
        
        
    def __beers_law_box(self):
        tab_part = QGroupBox("Beer's Law Parameters:")
        tab_part.setStyleSheet(box_title)
        layout = QHBoxLayout()
        self.__concentration_entry_1, self.__concentration_entry_2, self.__pathlength = QLineEdit(), QLineEdit(), QLineEdit()
        self.__concentration_entry_1.setMaximumWidth(45)
        self.__concentration_entry_2.setMaximumWidth(30)
        self.__pathlength.setMaximumWidth(45)
        
        self.__concentration_entry_1.setMaxLength(5)
        self.__concentration_entry_1.setValidator(QDoubleValidator())
        self.__concentration_entry_1.setAlignment(Qt.AlignRight)
        
        self.__concentration_entry_2.setMaxLength(3)
        self.__concentration_entry_2.setValidator(QIntValidator())
        self.__concentration_entry_2.setAlignment(Qt.AlignRight)

        self.__pathlength.setMaxLength(5)
        self.__pathlength.setValidator(QDoubleValidator())
        self.__pathlength.setAlignment(Qt.AlignRight)

        label1, label2, label3, label4, label5 = QLabel(), QLabel(), QLabel(), QLabel(), QLabel()
        label1.setText("Concentration:")
        label2.setText("x 10^(")
        label3.setText(") mol.L<sup>-1</sup>")
        label4.setText("        Pathlength:")
        label5.setText("cm")
        layout.addStretch()
        layout.addWidget(label1)
        layout.addWidget(self.__concentration_entry_1)
        layout.addWidget(label2)
        layout.addWidget(self.__concentration_entry_2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(self.__pathlength)
        layout.addWidget(label5)
        layout.addStretch()
        tab_part.setLayout(layout)
        self.__turn_off_beer_law()
        self.layout.addWidget(tab_part)

    
    def __turn_on_beer_law(self):
        self.__concentration_entry_1.setEnabled(True)
        self.__concentration_entry_2.setEnabled(True)
        self.__pathlength.setEnabled(True)
    
    def __turn_off_beer_law(self):
        self.__concentration_entry_1.setText('1.000')
        self.__concentration_entry_2.setText('-2')
        self.__pathlength.setText('1.000')
        self.__concentration_entry_1.setEnabled(False)
        self.__concentration_entry_2.setEnabled(False)
        self.__pathlength.setEnabled(False)
    
    @property
    def spectrum_intensity_method(self):
        """This property indicates the button selected in group 'Spectrum Intensity Method' on the 'Spectrum Parameters' tab

        Returns an integer that indicates: 
            0: for Relative Intensity
            1: for Estimated Molar Attenuation Coefficient;
            2: for Estimated Absorbance
        """     
        if self.__spectrum_method_b1.isChecked():
            return 0
        elif self.__spectrum_method_b2.isChecked():
            return 1
        else:
            return 2
    
    @property
    def wl_range(self):
        """This property indicates the values setted in group 'Parameters of the wavelength range' on the 'Spectrum Parameters' tab

        Returns a tuple whose pointers indicate:
            0: The beginning of the wavelength range
            1: The end of the wavelength range
            2: The number of points at which this range should be splitted
        """  
  
        return (int(self.__r_start.text()), int(self.__r_end.text()), int(self.__n_points.text()))
        
    @property
    def fwhm(self):
        """This property indicates the value of FWHM setted in group 'Parameters of the wavelength range' on the 'Spectrum Parameters' tab
        
        Returns an integer that indicates the Full Width Half Maximum value.
        """  
        return float(self.__hwhm_entry.text())
    
    @property
    def beers_law(self):
        """This property indicates the values setted in group 'Beer's Law Parameters' on the 'Spectrum Parameters' tab

        Returns a tuple whose pointers indicate:
            0: The number that multiplies the exponential base 10 in scientific notation of the indicated concentration value
            1: The number indicating the power of the exponential base 10 in scientific notation of the indicated concentration value
            2: The simulated value of the pathlength taken by radiation in a spctrometric analysis
            
        Note: If the data entries for that group are disabled, all values of the returned tuple will be null
        """ 
        if self.spectrum_intensity_method != 2:
            return (None, None, None)
        else:
            return (float(self.__concentration_entry_1.setText('1.000')), float(self.__concentration_entry_2.setText('-2')), float(self.__pathlength.setText('1.000')))
    
    
    
class Table3(QWidget):
    
    def __init__(self, controller):
        super(QWidget, self).__init__()
        self.control = controller
        self.layout = QGridLayout()

        self.setLayout(self.layout)
        
class Table4(QWidget):
    
    def __init__(self, controller):
        super(QWidget, self).__init__()
        self.control = controller
        self.layout = QGridLayout()

        self.setLayout(self.layout)
        
    
    def __init__(self, controller):
        super(QWidget, self).__init__()
        self.control = controller
        self.layout = QGridLayout()

        self.setLayout(self.layout)