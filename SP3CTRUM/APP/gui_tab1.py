from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap

box_title = "QGroupBox::title  { subcontrol-origin: margin; font-size: 12px; subcontrol-position: top ,left; }"

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
        self.__button_indep_files.clicked.connect(self.__clear_file_list)
        self.__button_dep_files.clicked.connect(self.__clear_file_list)
        self.__button_indep_files.setChecked(True)
        layout = QHBoxLayout() 
        layout.addWidget(self.__button_indep_files)
        layout.addWidget(self.__button_dep_files)
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part, 1 ,1)

    def __file_button_and_logo_area(self):
        self.__button_files = QPushButton("Choose Files", self)
        self.__button_files.setToolTip("Select the files to be used in the analysis.")
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
        tab_part = QGroupBox("Selected Files:")
        tab_part.setStyleSheet(box_title)
        layout = QVBoxLayout()
        self.fileList = QListWidget()
        layout.addWidget(self.fileList)
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part, 3 ,0)

    def __selectFiles_click(self):
        self.__clear_file_list()
        error_dialog = QMessageBox()
        if self.__button_type_file_g09.isChecked():
            files_to_take = "Gaussian Output Files (*.out *.log)"
        else:
            files_to_take = "Gaussian Output Files (*.out *.log)"
        limit_files = 200
        if self.__button_indep_files.isChecked():
            limit_files = 6
        fname = QFileDialog.getOpenFileNames(self, 'Open file', '', files_to_take)
        if len(fname[:-1][0]) <= limit_files:
            self.__fill_file_list(fname[:-1][0])
        else:
            error_dialog.critical(self, "", "Independent input files can only be accepted for a maximum of 6. Therefore, excess files will be ignored.")
            self.__fill_file_list(fname[:-1][0][:5])
        self.parent.realese_tabs()
                
    def __clear_file_list(self):
        self.fileList.clear()

    def __fill_file_list(self, files):
        self.__file_list = files
        for i in range(0,len(files)):
            size = int(len(files[i]) * .6)
            item = QListWidgetItem()
            item.setText("..."+files[i][size:])
            item.setToolTip(files[i])
            self.fileList.addItem(item)

    @property
    def file_list(self):
        return self.__file_list

    @property
    def input_file_type(self):
        if self.__button_type_file_g09.isChecked():
            return 0
        
    @property
    def dependence_of_files(self):
        if self.__button_indep_files.isChecked():
            return False
        else:
            return True
