from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap

box_title = "QGroupBox::title  { subcontrol-origin: margin; font-size: 12px; subcontrol-position: top ,left; }"
input_box_title = "Input File Type"
text_button_type_file_g09 = "Gaussian files"
text_button_type_file_g09_tooltip = "Output files from G09 or G16 with theoretical photophysical data"
input_file_box_text = "Choose the type of input files"
text_button_indep_files = "Independent"
text_button_indep_files_toottip = "For each file a different analysis will be applied, resulting in different results"
text_button_dep_files = "Dependent"
text_button_dep_files_tooltip = "All files will be used for the same analysis, resulting in a single result"
text_button_files_bt = "Choose Files"
text_button_files_bt_tootltip = "Select the files to be used in the analysis"
selected_files_box_text = "Selected Files"
files_to_take_text = "Gaussian Output Files"
open_file_text = 'Open file'
no_files_error_text = "No files were selected, so I won't do anything."
more_then_6_error_text = "Independent input files can only be accepted for a maximum of 6. Therefore, excess files will be ignored."

class Table1(QWidget):
    
    def __init__(self, parent_guide):
        super(QWidget, self).__init__()
        self.parent = parent_guide
        self.layout = QGridLayout()
        self.__create_input_file_box()
        self.__create_type_of_input_files()
        self.__create_file_list_area()
        self.__file_button_and_logo_area()
        self.layout.setHorizontalSpacing(5)
        self.layout.setVerticalSpacing(25)
        self.setStyleSheet(box_title)
        self.setLayout(self.layout)
        self.refresh_values_tab()

    def __create_input_file_box(self):
        tab_part = QGroupBox(input_box_title+":")
        tab_part.setStyleSheet(box_title)
        self.__button_type_file_g09 = QRadioButton(text_button_type_file_g09)
        self.__button_type_file_g09.setToolTip(text_button_type_file_g09_tooltip+".")
        layout = QHBoxLayout()
        layout.addStretch()
        layout.addWidget(self.__button_type_file_g09)
        layout.addStretch()
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part, 1, 0) 

    def __create_type_of_input_files(self):
        tab_part = QGroupBox(input_file_box_text+ ":")
        tab_part.setStyleSheet(box_title)
        self.__button_indep_files = QRadioButton(text_button_indep_files)
        self.__button_indep_files.setToolTip(text_button_indep_files_toottip+".")
        self.__button_dep_files = QRadioButton(text_button_dep_files)
        self.__button_dep_files.setToolTip(text_button_dep_files_tooltip+".")
        self.__button_indep_files.clicked.connect(self.__clear_file_list)
        self.__button_dep_files.clicked.connect(self.__clear_file_list)
        layout = QHBoxLayout()
        layout.addWidget(self.__button_indep_files)
        layout.addWidget(self.__button_dep_files)
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part, 1 ,1)

    def __file_button_and_logo_area(self):
        self.__button_files = QPushButton(text_button_files_bt, self)
        self.__button_files.setToolTip(text_button_files_bt_tootltip+".")
        self.__button_files.clicked.connect(self.__selectFiles_click)
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
        tab_part = QGroupBox(selected_files_box_text+":")
        tab_part.setStyleSheet(box_title)
        layout = QVBoxLayout()
        self.fileList = QListWidget()
        layout.addWidget(self.fileList)
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part, 3 ,0)

    def __selectFiles_click(self):
        self.__clear_file_list()
        self.parent.turn_on_button_make_analysis(False)
        self.parent.realese_tabs(False)
        error_dialog = QMessageBox()
        if self.__button_type_file_g09.isChecked():
            files_to_take = files_to_take_text + " (*.out *.log)"
        else:
            files_to_take = files_to_take_text + " (*.out *.log)"
        limit_files = 200
        if self.__button_indep_files.isChecked():
            limit_files = 6
        fname = QFileDialog.getOpenFileNames(self, open_file_text, '', files_to_take)
        if len(fname[:-1][0]) == 0:
            error_dialog.critical(self, "", no_files_error_text)
        elif len(fname[:-1][0]) <= limit_files:
            self.__fill_file_list(fname[:-1][0])
            self.parent.turn_on_button_make_analysis(True)
            self.parent.realese_tabs(True)
        else:
            error_dialog.critical(self, "", more_then_6_error_text)
            self.__fill_file_list(fname[:-1][0][:5])
            self.parent.turn_on_button_make_analysis(True)
            self.parent.realese_tabs(True)
            
    def __clear_file_list(self):
        self.fileList.clear()

    def __fill_file_list(self, files):
        self.parent.analysis_settings.files = files
        for i in range(0,len(self.parent.analysis_settings.files)):
            size = int(len(files[i]) * .6)
            item = QListWidgetItem()
            item.setText("..."+files[i][size:])
            item.setToolTip(files[i])
            self.fileList.addItem(item)

    def refresh_values_tab(self):
        if self.parent.analysis_settings.dependence_input_files:
            self.__button_dep_files.setChecked(True)
        else:
            self.__button_indep_files.setChecked(True)
        if self.parent.analysis_settings.gaussian_output_files:
            self.__button_type_file_g09.setChecked(True)
            
