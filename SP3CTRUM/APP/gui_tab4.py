from sys import setdlopenflags
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtGui import QIntValidator, QDoubleValidator

box_title = "QGroupBox::title  { subcontrol-origin: margin; font-size: 12px; subcontrol-position: top ,left; }"

text_chosen = "Chosen file: "
text_choose_the_exp_file = "Choose the file with the Experimental data"
text_plot_overlap = "Plot with overlapping experimental data?"
text_yes = "Yes"
text_no = "No"
text_open_file = "Open file"
text_no_exp_file_selected = "No files with experimental data were selected"
text_type_files_exp_data = "Files with experimental data (*.dat *csv *txt)"
text_exp_type = "Type of experimental data to be plotted?"
text_exp_data_plot_color = "Experimental data plot color"
text_curve_plot_tooltip = "Curve plot"
text_ref_plot_tooltip = "Plot of maximum intensity droplets"
text_curve_plot = "Curve"
text_ref_plot = "Reference"
fwhm_search = "Find the best FWHM for the theoretical values that fits the experimental values?"
pt_exp_values_label = "Points of the experimental values:"
wl_label = "Wavelength:"
wl_label_unit = "(nm)"
molar_abs_label = "Molar Absortivity:"
molar_abs_label_unit = "(L/mol.cm)"

class Table4(QWidget):
    
    def __init__(self, parent_guide):
        super(QWidget, self).__init__()
        self.parent = parent_guide
        self.tab = QGroupBox("Experimental Plot Settings")
        self.layout = QVBoxLayout()
        self.layout_top = QVBoxLayout()
        self.layout_top.addStretch()
        self.__question_exp_data()
        self.__exp_file = ""
        self.__fwhm_search()
        self.__exp_plot_settings()
        self.__pts_exp_values()
        self.layout_top.addWidget(self.tab)
        self.layout_top.addStretch()
        self.tab.setLayout(self.layout)
        self.setLayout(self.layout_top)
        self.setStyleSheet(box_title)
        self.__self_turn_off_exp_file()
        self.__turn_pt_exp_value_off()
        
    def __question_exp_data(self):
        layout = QHBoxLayout()
        tab_part = QWidget()
        tab_part.setStyleSheet(box_title)
        label = QLabel()
        label.setText(text_plot_overlap)
        self.__exp_data_yes = QRadioButton(text_yes)
        self.__exp_data_no = QRadioButton(text_no)
        self.__exp_data_no.setChecked(True)
        self.__exp_data_yes.clicked.connect(self.__self_turn_on_exp_file)
        self.__exp_data_no.clicked.connect(self.__self_turn_off_exp_file)
        
        tab_part1 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addStretch()
        self.__exp_file_button = QPushButton()
        self.__exp_file_button.setText(text_choose_the_exp_file)
        self.__exp_file_button.clicked.connect(self.__choosen_exp_file)
        self.__label_choose_file = QLabel()
        self.__label_choose_file.setAlignment(Qt.AlignCenter)
        layout1.addWidget(self.__exp_file_button)
        layout1.addWidget(self.__label_choose_file)
        layout1.addStretch()
        tab_part1.setLayout(layout1)
        
        layout.addStretch()
        layout.addWidget(label)
        layout.addWidget(self.__exp_data_yes)
        layout.addWidget(self.__exp_data_no)
        layout.addStretch()
        layout.addWidget(tab_part1)
        layout.addStretch()
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part)
        
    def __fwhm_search(self):
        layout = QHBoxLayout()
        tab_part = QWidget()
        tab_part.setStyleSheet(box_title)
        self.__label_fwhm = QLabel()
        self.__label_fwhm.setText(fwhm_search)
        self.__fwhm_s_yes = QRadioButton(text_yes)
        self.__fwhm_s_no = QRadioButton(text_no)
        self.__fwhm_s_no.setChecked(True)
        self.__fwhm_s_yes.clicked.connect(self.__fwhm_turn_off)
        self.__fwhm_s_no.clicked.connect(self.__fwhm_turn_on)
        layout.addStretch()
        layout.addWidget(self.__label_fwhm)
        layout.addWidget(self.__fwhm_s_yes)
        layout.addWidget(self.__fwhm_s_no)
        layout.addStretch()
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part)
    
    def __exp_plot_settings(self):
        layout = QHBoxLayout()
        tab_part = QWidget()
        tab_part.setStyleSheet(box_title)
        self.__label_exp_plot_settings, self.__label_color_exp = QLabel(), QLabel()
        self.__label_color_exp.setText(text_exp_data_plot_color)
        self.__label_exp_plot_settings.setText(text_exp_type)
        self.__exp_type_button_curve = QRadioButton(text_curve_plot)
        self.__exp_type_button_ref = QRadioButton(text_ref_plot)
        self.__exp_type_button_curve.setToolTip(text_curve_plot_tooltip)
        self.__exp_type_button_ref.setToolTip(text_ref_plot_tooltip)
        self.__exp_type_button_ref.clicked.connect(self.__turn_pt_exp_value_on)
        self.__exp_type_button_curve.clicked.connect(self.__turn_pt_exp_value_off)
        
        self.__color = QLineEdit()
        
        self.__color.setMaximumWidth(67)
        self.__color.setValidator(QRegExpValidator(QRegExp("^#[A-F1-9_]+$")))
        self.__color.setMaxLength(7)
        self.__color.setAlignment(Qt.AlignRight)
        
        layout.addStretch()
        layout.addWidget(self.__label_exp_plot_settings)
        layout.addWidget(self.__exp_type_button_curve)
        layout.addWidget(self.__exp_type_button_ref)
        layout.addStretch()
        layout.addWidget(self.__label_color_exp)
        layout.addWidget(self.__color)
        layout.addStretch()
        tab_part.setLayout(layout)
        
        self.layout.addWidget(tab_part)
    
    def __pts_exp_values(self):
        layout = QHBoxLayout()
        tab_part = QWidget()
        tab_part.setStyleSheet(box_title)
        self.__points_exp_values = QLabel()
        self.__points_exp_values.setText(pt_exp_values_label)
        layout.setAlignment(Qt.AlignCenter)
        
        layout1 = QVBoxLayout()
        tab_part1 = QWidget()
        tab_part1.setLayout(layout1)
        layout1.addStretch()
        layout1.addWidget(self.__points_exp_values)
        layout1.addStretch()
        layout1.setAlignment(Qt.AlignCenter)
        
        layout2 = QVBoxLayout()
        tab_part2 = QWidget()
        layout2.setAlignment(Qt.AlignHCenter)
        tab_part2.setLayout(layout2)
        
        layout2.addStretch()
        self.__wl_label = QLabel()
        
        self.__wl_label.setText(wl_label)
        self.__wl_label.setAlignment(Qt.AlignCenter)
        self.__wl_entries = []
        self.__wl_unit_label = QLabel()
        self.__wl_unit_label.setText(wl_label_unit)
        self.__wl_unit_label.setAlignment(Qt.AlignCenter)
        layout2.addWidget(self.__wl_label)
        layout2.addWidget(self.__wl_unit_label)
        
        for i in range(4):
            self.__wl_entries.append(QLineEdit())
            self.__wl_entries[i].setAlignment(Qt.AlignCenter)
            self.__wl_entries[i].setValidator(QIntValidator())
            self.__wl_entries[i].setMaxLength(3)
            layout2.addWidget(self.__wl_entries[i])

        layout2.addStretch()
        
        layout3 = QVBoxLayout()
        tab_part3 = QWidget()
        tab_part3.setLayout(layout3)
        layout3.addStretch()
        layout3.setAlignment(Qt.AlignCenter)
        self.__ma_label = QLabel()
        self.__ma_label.setText(molar_abs_label)
        self.__ma_label.setAlignment(Qt.AlignCenter)
        self.__ma_unit_label = QLabel()
        self.__ma_unit_label.setText(molar_abs_label_unit)
        self.__ma_unit_label.setAlignment(Qt.AlignCenter)
        self.__abs_entries = []
        layout3.addWidget(self.__ma_label)
        layout3.addWidget(self.__ma_unit_label)
        for i in range(4):
            self.__abs_entries.append(QLineEdit())
            layout3.addWidget(self.__abs_entries[i])
            self.__abs_entries[i].setAlignment(Qt.AlignCenter)
            self.__abs_entries[i].setValidator(QDoubleValidator())
            self.__abs_entries[i].setMaxLength(8)
            layout3.addStretch()
        
        layout3.addStretch()
        
        layout.addStretch()
        layout.addWidget(tab_part1)
        layout.addWidget(tab_part2)
        layout.addWidget(tab_part3)
        layout.addStretch()
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part)
        
   
    def __turn_pt_exp_value_off(self):
        self.__points_exp_values.setEnabled(False)
        self.__wl_label.setEnabled(False)
        self.__wl_unit_label.setEnabled(False)
        self.__ma_label.setEnabled(False)
        self.__ma_unit_label.setEnabled(False)
        for i in range(4):
            self.__abs_entries[i].setEnabled(False)
            self.__wl_entries[i].setEnabled(False)
            self.__abs_entries[i].setText("")
            self.__wl_entries[i].setText("")
    
    def __turn_pt_exp_value_on(self):
        self.__points_exp_values.setEnabled(True)
        self.__wl_label.setEnabled(True)
        self.__wl_unit_label.setEnabled(True)
        self.__ma_label.setEnabled(True)
        self.__ma_unit_label.setEnabled(True)
        for i in range(4):
            self.__abs_entries[i].setEnabled(True)
            self.__wl_entries[i].setEnabled(True)
    
    def __self_turn_on_exp_file(self):
        self.__exp_file_button.setEnabled(True)
        self.__label_choose_file.setEnabled(True)
        self.__label_exp_plot_settings.setEnabled(True)
        self.__label_color_exp.setEnabled(True)
        self.__exp_type_button_curve.setEnabled(True)
        self.__exp_type_button_ref.setEnabled(True)
        self.__exp_type_button_curve.setChecked(True)
        self.__label_fwhm.setEnabled(True)
        self.__fwhm_s_no.setEnabled(True)
        self.__fwhm_s_no.setChecked(True)
        self.__color.setEnabled(True)
        self.__fwhm_s_yes.setEnabled(True)
            
    def __self_turn_off_exp_file(self):
        self.__exp_file_button.setEnabled(False)
        self.__color.setEnabled(False)
        self.__label_choose_file.setEnabled(False)
        self.__label_exp_plot_settings.setEnabled(False)
        self.__label_color_exp.setEnabled(False)
        self.__exp_type_button_curve.setEnabled(False)
        self.__exp_type_button_ref.setEnabled(False)
        self.__label_fwhm.setEnabled(False)
        self.__fwhm_s_no.setEnabled(False)
        self.__fwhm_s_yes.setEnabled(False)
        self.__clean_choose_file_text_label()
        self.__turn_pt_exp_value_off()
    
    def __choosen_exp_file(self):
        self.__clean_choose_file_text_label()
        fname = QFileDialog.getOpenFileName(self, text_open_file, '', text_type_files_exp_data)
        print(fname)
        self.__exp_file = fname[0]
        self.__label_choose_file.setText(text_chosen + "..." + self.__exp_file[-30:])
        
    def __clean_choose_file_text_label(self):
        self.__label_choose_file.setText(text_no_exp_file_selected)
        self.__exp_file = ""
        
    def __fwhm_turn_on(self):
        self.parent.tab2.fhwm_turn_on_off(True)
    
    def __fwhm_turn_off(self):
        self.parent.tab2.fhwm_turn_on_off(False)
    
    @property
    def exp_data(self):
        return self.__exp_data_yes.isChecked()
    
    @property
    def exp_file(self):
        if self.__exp_file == "":
            return None
        return self.__exp_file
    
    @property
    def fwhm_search(self):
        self.__fwhm_s_yes.isChecked()
        
    @property
    def type_exp_data(self):
        return self.__exp_data_yes.isChecked()
    
    @property
    def exp_dat_color(self):
        return self.__color.text()
    
    @property
    def points_exp_values(self):
        result = {}
        for i in range(4):
            result.update({self.__wl_entries[i] : self.__abs_entries[i]})
        return result
        
    
    