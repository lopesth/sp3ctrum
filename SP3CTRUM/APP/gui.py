from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
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
        self.table_widget.add_new_tab(Table1, "Spectrum Parameters") # Table 1 in table_list
        self.table_widget.add_new_tab(Table1, "Plot Details") # Table 2 in table_list
        self.table_widget.add_new_tab(Table1, "Versus Experimental Values") # Table 3 in table_list
        self.table_widget.add_new_tab(Table1, "Advanced Options")# Table 4 in table_list
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
        layout = QVBoxLayout()
        layout.addWidget(self.__button_type_file_g09)
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

