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
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.table_widget.add_new_tab(Table1(controller), "Files") # Table 0 in table_list
        self.table_widget.add_new_tab(Table1(controller), "Spectrum Parameters") # Table 1 in table_list
        self.table_widget.add_new_tab(Table1(controller), "Plot Details") # Table 2 in table_list
        self.table_widget.add_new_tab(Table1(controller), "Versus Experimental Values") # Table 3 in table_list
        self.table_widget.add_new_tab(Table1(controller), "Advanced Options")# Table 4 in table_list
        layout = QGridLayout()
        
class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tab_list = []
        self.buildTabs()
        
    def add_new_tab(self, tab, tab_name):
        self.tab_list.append(tab)
        self.tabs.addTab(self.tab_list[-1],tab_name)

    def buildTabs(self):
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

class Table1(QWidget):
    
    def __init__(self, controller):
        super(QWidget, self).__init__()
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
        self.__button_type_files = QRadioButton("Gaussian output")
        self.__button_type_files.setChecked(True)
        layout = QVBoxLayout()
        layout.addWidget(self.__button_type_files)
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part, 1, 0) 

    def __create_type_of_input_files(self):
        tab_part = QGroupBox("Choose the type of input files:")
        tab_part.setStyleSheet(box_title)
        self.__button_indep_files = QRadioButton("Independent")
        self.__button_dep_files = QRadioButton("Dependent")
        self.__button_indep_files.setChecked(True)
        layout = QHBoxLayout() 
        layout.addWidget(self.__button_indep_files)
        layout.addWidget(self.__button_dep_files)
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part, 1 ,1)

    def __file_button_and_logo_area(self):
        self.__button_files = QPushButton("Choose Files", self)
        self.__button_files.clicked.connect(self.selectFiles_click)
        tab_part = QWidget()
        layout = QVBoxLayout()
        layout.addStretch(1)
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
        layout.addStretch(1)
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
        self.fileList.insertItem(0,"Teste")