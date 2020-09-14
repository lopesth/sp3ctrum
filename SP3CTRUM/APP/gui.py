from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from os import popen

def selectStyle(styleFile):
    f = open("./SP3CTRUM/styles/"+styleFile)
    style = f.read()
    f.close()
    return style

class MainWindow(QMainWindow):
    
     def __init__(self, os_name, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Sp3ctrum Wizard")
        self.table_widget = MyTableWidget(self, os_name)
        self.setCentralWidget(self.table_widget)

        layout = QGridLayout()
        
class MyTableWidget(QWidget):
    
    def __init__(self, parent, os_name):
        super(QWidget, self).__init__(parent)
        if os_name == 'darwin':

            style = popen('defaults read -g AppleInterfaceStyle').read().strip('\n')
            print(style)
            if style == 'Dark':
                self.style = selectStyle("style_dark.qss")
            else:
                self.style = selectStyle("style_normal.qss")
        else:
            self.style = selectStyle("style_normal.qss")
        self.box_title = "QGroupBox::title  { subcontrol-origin: margin; font-size: 12px; subcontrol-position: top ,left; }"
        self.layout = QVBoxLayout(self)
        self.startTabs()
        self.buildTabs()
        
    def makeTab1(self):
        self.tab1.layout = QGridLayout()
        # First Row
        tab1_input = QGroupBox("Input File Type:")
        tab1_input.setStyleSheet(self.box_title)
        b1_input = QRadioButton("Gaussian output")
        b1_input.setChecked(True)
        layout_1 = QVBoxLayout()
        layout_1.addWidget(b1_input)
        tab1_input.setLayout(layout_1)
        tab1_analysis = QGroupBox("Choose the type of input files:")
        tab1_analysis.setStyleSheet(self.box_title)
        b1_analysis = QRadioButton("Independent")
        b2_analysis = QRadioButton("Dependent")
        b1_analysis.setChecked(True)
        layout_2grid = QHBoxLayout() 
        layout_2grid.addWidget(b1_analysis)
        layout_2grid.addWidget(b2_analysis)
        button = QPushButton("Choose Files", self)
        button.clicked.connect(self.selectFiles_click)
        tab1_analysis.setLayout(layout_2grid)
        # Second Row       

        tab1_button = QWidget()
        layout_3 = QVBoxLayout()
        layout_3.addStretch(1)
        layout_3.addWidget(button)
        label_logo = QLabel(self)
        label_name = QLabel(self)
        label_name.setText("Sp3ctrum Wizard!")

        label_name.setStyleSheet("QLabel{font-weight: bold; qproperty-alignment: AlignCenter; font-size: 20px;}")
        pixmap_logo = QPixmap('./SP3CTRUM/styles/icon/sp3ctrum_gray.svg')
        label_logo.setPixmap(pixmap_logo)
        label_logo.setScaledContents(True)
        layout_3.addWidget(label_logo)
        layout_3.addWidget(label_name)
        layout_3.addStretch(1)
        tab1_button.setLayout(layout_3)
        tab1_files = QGroupBox("Selected Files:")
        tab1_files.setStyleSheet(self.box_title)
        layout_4 = QVBoxLayout()
        self.fileList = QListWidget()
        layout_4.addWidget(self.fileList)
        tab1_files.setLayout(layout_4)

        blanckSpace = QWidget()
        blanckLayout = QVBoxLayout()
        blanckSpace.setLayout(blanckLayout)
    
        # Tab1 Set Layout
        self.tab1.layout.setHorizontalSpacing(5)
        self.tab1.layout.setVerticalSpacing(25)
        self.tab1.layout.addWidget(tab1_input, 1, 0) 
        self.tab1.layout.addWidget(tab1_analysis, 1 ,1)
        self.tab1.layout.addWidget(tab1_files, 3 ,0)
        self.tab1.layout.addWidget(tab1_button, 3 ,1)
        self.tab1.setLayout(self.tab1.layout)
        
        
    def selectFiles_click(self):
        self.fileList.insertItem(0,"Teste")
    
    def makeTab2(self):
        pass  
    
    def makeTab3(self):
        pass  
    
    def makeTab4(self):
        pass  
    
    def makeTab5(self):
        pass  
    
    
				
    
    def startTabs(self):
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tabs.addTab(self.tab1,"Files")
        self.tabs.addTab(self.tab2,"Spectrum Parameters")
        self.tabs.addTab(self.tab3,"Plot Details")
        self.tabs.addTab(self.tab4,"Versus Experimental Values")
        self.tabs.addTab(self.tab5,"Advanced Options")
        self.makeTab1()
        self.makeTab2()
        self.makeTab3()
        self.makeTab4()
        self.makeTab5()

    def buildTabs(self):
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)



