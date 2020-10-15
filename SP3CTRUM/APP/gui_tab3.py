from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIntValidator, QRegExpValidator

box_title = "QGroupBox::title  { subcontrol-origin: margin; font-size: 12px; subcontrol-position: top ,left; }"

class Table3(QWidget):
    
    def __init__(self, parent_guide):
        super(QWidget, self).__init__()
        self.parent = parent_guide
        self.layout = QGridLayout()
        self.__number_of_plots = 0
        self.__plot_settings()
        self.__fig_settings()
        self.setStyleSheet(box_title)
        self.setLayout(self.layout)
    
    def __plot_settings(self):
        tab_part = QGroupBox("Plot Settings:")
        tab_part.setStyleSheet(box_title)
        layout = QVBoxLayout()
        chart_title_text = QLabel()
        
        tab_part1 = QWidget()
        layout1 = QHBoxLayout()
        chart_title_text.setText("Chart Title (optional entry):")
        self.__chart_title = QLineEdit()
        self.__chart_title.setMaximumWidth(500)
        self.__chart_title.setMinimumWidth(300)
        layout1.addStretch()
        layout1.addWidget(chart_title_text)
        layout1.addWidget(self.__chart_title)
        layout1.addStretch()
        
        tab_part2 = QWidget()
        layout2 = QHBoxLayout()
        layout2.addStretch()
        color_curve_text = QLabel()
        color_curve_text.setText("Curve Colors:\n(CSS Hex Style for each plot)")
        color_curve_text.setAlignment(Qt.AlignCenter)
        color_curve_text.setWordWrap(True)
        layout2.addWidget(color_curve_text)
        
        self.__color_curves = [QLineEdit() for x in range(6)]
        default_colors = ['#E01E23', '#573280', '#945055', '#005CB8', '#29000A', '#000000']
        for i in range(6):
            self.__color_curves[i].setMaximumWidth(67)
            self.__color_curves[i].setValidator(QRegExpValidator(QRegExp("^#[A-F1-9_]+$")))
            self.__color_curves[i].setMaxLength(7)
            self.__color_curves[i].setAlignment(Qt.AlignRight)
            self.__color_curves[i].setText(default_colors[i])
            layout2.addWidget(self.__color_curves[i])
        
        for i in range(0,6):
            self.__color_curves[i].setEnabled(False)
    
        layout2.addStretch()
        
        tab_part3 = QWidget()
        layout3 = QHBoxLayout()
        layout3.addStretch()
        label_osc = QLabel()
        label_osc.setText("Show theoretical oscillators on the plot?")
        self.__t_osc_b_yes = QRadioButton("Yes")
        self.__t_osc_b_yes.clicked.connect(self.switch_on_oscillators_colors)
        self.__t_osc_b_no = QRadioButton("No")
        self.__t_osc_b_no.clicked.connect(self.switch_off_oscillators_colors)
        self.__t_osc_b_no.setChecked(True)

        layout3.addWidget(label_osc)
        layout3.addWidget(self.__t_osc_b_yes)
        layout3.addWidget(self.__t_osc_b_no)
        layout3.addStretch()
        
        tab_part4 = QWidget()
        layout4 = QHBoxLayout()
        layout4.addStretch()
        color_osc_text = QLabel()
        color_osc_text.setText("Oscillators Colors:\n(CSS Hex Style for each plot)")
        color_osc_text.setAlignment(Qt.AlignCenter)
        color_osc_text.setWordWrap(True)
        layout4.addWidget(color_osc_text)
        
        self.__color_osc = [QLineEdit() for x in range(6)]
        for i in range(6):
            self.__color_osc[i].setMaximumWidth(67)
            self.__color_osc[i].setValidator(QRegExpValidator(QRegExp("^#[A-F1-9_]+$")))
            self.__color_osc[i].setMaxLength(7)
            self.__color_osc[i].setAlignment(Qt.AlignRight)
            self.__color_osc[i].setText(default_colors[i])
            self.__color_osc[i].setEnabled(False)
            layout4.addWidget(self.__color_osc[i])
            
        layout4.addStretch()

        tab_part5 = QWidget()
        layout5 = QHBoxLayout()
        layout5.addStretch()
        
        tab_part5_1 = QWidget()
        layout5_1 = QHBoxLayout()
        layout5_1.addStretch()
        overlap_label = QLabel()
        overlap_label.setText("Overlapping plots?")
        self.__overlap_b_yes = QRadioButton("Yes")
        self.__overlap_b_no = QRadioButton("No")
        self.__overlap_b_no.setChecked(True)
        layout5_1.addWidget(overlap_label)
        layout5_1.addWidget(self.__overlap_b_yes)
        layout5_1.addWidget(self.__overlap_b_no)
        layout5_1.addStretch()
        
        tab_part5_2 = QWidget()
        layout5_2 = QHBoxLayout()
        layout5_2.addStretch()
        plot_label = QLabel()
        plot_label.setText("Plot labeling?")
        self.__plot_label_yes = QRadioButton("Yes")
        self.__plot_label_no = QRadioButton("No")
        self.__plot_label_no.setChecked(True)
        layout5_2.addWidget(plot_label)
        layout5_2.addWidget(self.__plot_label_yes)
        layout5_2.addWidget(self.__plot_label_no)
        layout5_2.addStretch()
        
        tab_part5_1.setLayout(layout5_1)
        tab_part5_2.setLayout(layout5_2)
        layout5.addWidget(tab_part5_1)
        layout5.addWidget(tab_part5_2)
        layout5.addStretch()
        
        tab_part2.setLayout(layout2)
        tab_part1.setLayout(layout1)
        tab_part3.setLayout(layout3)
        tab_part4.setLayout(layout4)
        tab_part5.setLayout(layout5)
        layout.addWidget(tab_part1)
        layout.addWidget(tab_part2)
        layout.addWidget(tab_part3)
        layout.addWidget(tab_part4)
        layout.addWidget(tab_part5)
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part)
    
    def __fig_settings(self):
        tab_part = QGroupBox("Figure Settings:")
        
        tab_part.setStyleSheet(box_title)
        layout = QVBoxLayout()
        
        tab_part2 = QWidget()
        layout2 = QHBoxLayout()
        layout2.addStretch()
        label_1 = QLabel(self)
        label_1.setText("Base name for output files:")
        self.__base_name_entry = QLineEdit()
        self.__base_name_entry.setMaximumWidth(300)
        self.__base_name_entry.setMinimumWidth(200)
        self.__base_name_entry.setToolTip("Start with a letter and it can be followed by other letters, numbers or underscore.")
        self.__base_name_entry.setMaxLength(15)
        self.__base_name_entry.setValidator(QRegExpValidator(QRegExp("^[a-zA-Z][a-zA-Z1-9_]+$")))
        self.__base_name_entry.setAlignment(Qt.AlignRight)
        layout2.addWidget(label_1)
        layout2.addWidget(self.__base_name_entry)
        label_2_1, label_2_2 = QLabel(self), QLabel(self)
        label_2_1.setText("     Figure Resolution:")
        label_2_2.setText("dpi.")
        self.__dpi_figure = QLineEdit()
        self.__dpi_figure.setText("150")
        self.__dpi_figure.setToolTip("Choose the resolution of the picture to be saved in dpi (Dots Per Inch).")
        self.__dpi_figure.setMaximumWidth(40)
        self.__dpi_figure.setValidator(QIntValidator())
        self.__dpi_figure.setMaxLength(3)
        self.__dpi_figure.setAlignment(Qt.AlignRight)
        layout2.addWidget(label_2_1)
        layout2.addWidget(self.__dpi_figure)
        layout2.addWidget(label_2_2)
        layout2.addStretch()
        
        tab_part3 = QWidget()
        layout3 = QHBoxLayout()
        layout3.addStretch()
        label_3 = QLabel(self)
        label_3.setText("File Format:")
        self.__file_form_b1 = QRadioButton('.png')
        self.__file_form_b1.setToolTip("Portable Network Graphics format file.")
        self.__file_form_b2 = QRadioButton('.pdf')
        self.__file_form_b2.setToolTip("Portable Document Format format file.")
        self.__file_form_b3 = QRadioButton('.ps')
        self.__file_form_b3.setToolTip("format file.")
        self.__file_form_b4 = QRadioButton('.eps')
        self.__file_form_b4.setToolTip("format file.")
        self.__file_form_b5 = QRadioButton('.svg')
        self.__file_form_b5.setToolTip("format file.")
        self.__file_form_b1.setChecked(True)
        layout3.addWidget(label_3)
        layout3.addWidget(self.__file_form_b1)
        layout3.addWidget(self.__file_form_b2)
        layout3.addWidget(self.__file_form_b3)
        layout3.addWidget(self.__file_form_b4)
        layout3.addWidget(self.__file_form_b5)
        layout3.addStretch()
        
        tab_part2.setLayout(layout2)
        tab_part3.setLayout(layout3)
        layout.addWidget(tab_part2)
        layout.addWidget(tab_part3)
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part)
    
    def switch_on_curve_colors(self):
        for i in range(self.__number_of_plots):
            self.__color_curves[i].setEnabled(True)
    
    def switch_on_oscillators_colors(self):
        for i in range(self.__number_of_plots):
            self.__color_osc[i].setEnabled(True)
        
    def switch_off_oscillators_colors(self):
        for i in range(5):
            self.__color_osc[i].setEnabled(False)
        
    @property
    def base_name_file(self):
        return self.__base_name_entry.text()
 
    @property
    def fig_dpi(self):
        return int(self.__dpi_figure)
    
    @property
    def fig_format(self):
        if self.__file_form_b1.isChecked():
            return "png"
        elif self.__file_form_b2.isChecked():
            return "pdf"
        elif self.__file_form_b3.isChecked():
            return "ps"
        elif self.__file_form_b4.isChecked():
            return "eps"
        else:
            return "svg"
        
    @property
    def show_oscillators(self):
        return self.__t_osc_b_yes.isChecked()
    
    @property
    def overlap_plots(self):
        return self.__overlap_b_yes.isChecked()
    
    @property
    def plot_labeleling(self):
        return self.__plot_label_yes.isChecked()
    
    @property
    def n_plots(self):
        return self.__number_of_plots
    
    @n_plots.setter
    def n_plots(self, value):
        self.__number_of_plots = value
    
    @property
    def curve_colors(self):
        color_list = []
        for i in range(self.__number_of_plots):
            color_list.append(self.__color_curves[i].text())
        return color_list
        
    @property
    def curve_colors(self):
        color_list = []
        for i in range(self.__number_of_plots):
            color_list.append(self.__color_osc[i].text())
        return color_list
    
    @property
    def chart_title(self):
        return self.__chart_title.text()
