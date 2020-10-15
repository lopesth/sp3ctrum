from PyQt5.QtWidgets import *
from os import popen
from SP3CTRUM.APP.gui_tab1 import Table1
from SP3CTRUM.APP.gui_tab2 import Table2
from SP3CTRUM.APP.gui_tab3 import Table3
from SP3CTRUM.APP.gui_tab4 import Table4

box_title = "QGroupBox::title  { subcontrol-origin: margin; font-size: 12px; subcontrol-position: top ,left; }"

def selectStyle(styleFile):
    f = open("./SP3CTRUM/styles/"+styleFile)
    style = f.read()
    f.close()
    return style

class MainWindow(QMainWindow):
    
     def __init__(self, os_name, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Sp3ctrum Wizard")
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.setMinimumWidth(800)
        self.table_widget.add_new_tab(Table1, "Files", True) # Table 0 in table_list
        self.table_widget.add_new_tab(Table2, "Spectrum Parameters", False) # Table 1 in table_list
        self.table_widget.add_new_tab(Table3, "Plot Details", False) # Table 2 in table_list
        self.table_widget.add_new_tab(Table4, "Versus Experimental Values", False) # Table 3 in table_list
        layout = QGridLayout()
        
class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.__tab_list = []
        self.__buildTabs()
        self.__make_final_buttons_area()
        
    def add_new_tab(self, tab, tab_name, first_tab = True):
        if first_tab:
            self.__tab_list.append(tab(self))
        else:
            x = tab(self)
            #x.setEnabled(False)
            self.__tab_list.append(x)
        self.tabs.addTab(self.__tab_list[-1],tab_name)

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

    def realese_tabs(self):
        for i in range(1, len(self.__tab_list)):
            self.__tab_list[i].setEnabled(True)
        if self.__tab_list[0].dependence_of_files:
            self.__tab_list[2].n_plots = 1
        else:
            self.__tab_list[2].n_plots = len(self.__tab_list[0].file_list)
        self.__tab_list[2].switch_on_curve_colors()

    def __make_analysis(self):
        pass

    def __plot_results(self):
        pass

    def __save_as(self):
        pass

    def __save_data(self):
        pass

    
    @property
    def tab1(self):
        return self.__tab_list[0]
    
    @property
    def tab2(self):
        return self.__tab_list[1]

    @property
    def tab3(self):
        return self.__tab_list[2]

    @property
    def tab4(self):
        return self.__tab_list[3]

    def __create_final_buttons_area2(self):
        tab_part = QWidget()
        layout = QVBoxLayout()

        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part, 4 ,1)

