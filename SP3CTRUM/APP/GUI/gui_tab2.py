from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator

box_title = "QGroupBox::title  { subcontrol-origin: margin; font-size: 12px; subcontrol-position: top ,left; }"

fwhm_tooltip = "The 'Find the best FWHM for the theoretical values that fits the experimental values?' button\n(in 'Versus Experimental Values' tab) is marked as Yes, so this option is disabled!"
to = "to"
wl_range_group = "Parameters of the wavelength range"
range_text = "The analysis and plot will be done using the range from"
grid_points_1 = "The analysis must be done with a grid of"
grid_points_2 = "points"
fwhm_box_tex = "Full Width at Half Maximum"
fwhm_text = "FWHM value"
spec_box_text = "Spectrum Intensity Method"
spectrum_method_b1_text = "Relative Intensity"
spectrum_method_b2_text = "Estimated Molar Attenuation Coefficient"
spectrum_method_b3_text = "Estimated Absorbance"
spectrum_method_b1_text_tooltip_text = "In this method, the ordinate axis is shown with a relative intensity, normalized by the highest value oscillator."
spectrum_method_b2_text_tooltip_text = "In this method the ordinate axis is shown with an estimated (molar absorptivity, using the fwhm and the oscillators of the analysis."
spectrum_method_b3_text_tooltip_text = "In this method, there is a previous calculation of molar absorptivity and this value is used, via Beer's law, to calculate the Absorbance for each point on the graph."
concentration = "Concentration"
pathlength = "Pathlength"
beer_law_box_text = "Beer's Law Parameters"

class Table2(QWidget):
    
    def __init__(self, parent_guide):
        super(QWidget, self).__init__()
        self.parent = parent_guide
        self.layout = QVBoxLayout()
        self.__create_wavelenght_box()
        self.__fwhm_box()
        self.__spectum_method_box()
        self.__beers_law_box()
        self.setStyleSheet(box_title)
        self.setLayout(self.layout)
        self.refresh_values_tab()
        
    def __create_wavelenght_box(self):
        tab_part = QGroupBox(wl_range_group+":")
        tab_part.setStyleSheet(box_title)
        layout = QVBoxLayout()
        tab_part2 = QWidget()
        layout2 = QHBoxLayout()
        layout2.addStretch()
        nm_label, start_nm_text, end_nm_text = QLabel(self), QLabel(self), QLabel(self)
        nm_label.setText("nm. ")
        start_nm_text.setText(range_text + " ")
        end_nm_text.setText("nm "+to)
        self.__n_points_label1, self.__n_points_label2 = QLabel(self), QLabel(self)
        self.__n_points_label1.setText(grid_points_1)
        self.__n_points_label2.setText(grid_points_2 + ".")
        self.__r_start, self.__r_end = QLineEdit(), QLineEdit()
        self.__r_start.setMaximumWidth(45)
        self.__r_start.setValidator(QIntValidator())
        self.__r_start.setMaxLength(4)
        self.__r_start.setAlignment(Qt.AlignRight)
        layout2.addWidget(start_nm_text)
        layout2.addWidget(self.__r_start)
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
        tab_part = QGroupBox(fwhm_box_tex+":")
        tab_part.setStyleSheet(box_title)
        layout = QHBoxLayout()
        self.__fwhm_label1,  self.__fwhm_label2, self.__hwhm_entry = QLabel(self), QLabel(self), QLineEdit()
        self.__fwhm_label1.setText(fwhm_text  + ": ")
        self.__fwhm_label2.setText("cm<sup>-1</sup>")
        self.__hwhm_entry.setMaximumWidth(70)
        self.__hwhm_entry.setValidator(QDoubleValidator())
        self.__hwhm_entry.setMaxLength(8)
        self.__hwhm_entry.setAlignment(Qt.AlignRight)
        layout.addStretch()
        layout.addWidget(self.__fwhm_label1)
        layout.addWidget(self.__hwhm_entry)
        layout.addWidget( self.__fwhm_label2)
        layout.addStretch()
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part)
    
    def __spectum_method_box(self):
        tab_part = QGroupBox(spec_box_text+":")
        tab_part.setStyleSheet(box_title)
        layout = QHBoxLayout()
        self.__spectrum_method_b1 = QRadioButton(spectrum_method_b1_text)
        self.__spectrum_method_b1.setToolTip(spectrum_method_b1_text_tooltip_text)
        self.__spectrum_method_b1.clicked.connect(self.__turn_off_beer_law)
        self.__spectrum_method_b2 = QRadioButton(spectrum_method_b2_text)
        self.__spectrum_method_b2.setToolTip(spectrum_method_b2_text_tooltip_text)
        self.__spectrum_method_b2.clicked.connect(self.__turn_off_beer_law)
        self.__spectrum_method_b3 = QRadioButton(spectrum_method_b3_text)
        self.__spectrum_method_b3.setToolTip(spectrum_method_b2_text_tooltip_text)
        self.__spectrum_method_b3.clicked.connect(self.__turn_on_beer_law)
        layout = QHBoxLayout() 
        layout.addStretch()
        layout.addWidget(self.__spectrum_method_b1)
        layout.addWidget(self.__spectrum_method_b2)
        layout.addWidget(self.__spectrum_method_b3)
        layout.addStretch()
        tab_part.setLayout(layout)
        self.layout.addWidget(tab_part)
        
        
    def __beers_law_box(self):
        tab_part = QGroupBox(beer_law_box_text+":")
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
        label1.setText(concentration + ":")
        label2.setText("x 10^(")
        label3.setText(") mol.L<sup>-1</sup>")
        label4.setText("        "+pathlength+":")
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

    def fhwm_turn_on_off(self, on = True):
        self.__fwhm_label1.setEnabled(on)
        self.__fwhm_label2.setEnabled(on)
        self.__hwhm_entry.setEnabled(on)
        if on:
            self.__hwhm_entry.setToolTip("")
        else:
            self.__hwhm_entry.setToolTip(fwhm_tooltip)
    
    def __turn_on_beer_law(self):
        self.__concentration_entry_1.setEnabled(True)
        self.__concentration_entry_2.setEnabled(True)
        self.__pathlength.setEnabled(True)
    
    def __turn_off_beer_law(self):
        self.__concentration_entry_1.setEnabled(False)
        self.__concentration_entry_2.setEnabled(False)
        self.__pathlength.setEnabled(False)
    
    def refresh_values_tab(self):
        self.__r_start.setText(str(self.parent.analysis_settings.start_of_wl_interval))
        self.__r_end.setText(str(self.parent.analysis_settings.end_of_wl_interval))
        self.__n_points.setText(str(self.parent.analysis_settings.grid_points))
        self.__hwhm_entry.setText(str(self.parent.analysis_settings.fwhm))
        if self.parent.analysis_settings.spectrum_intensity_method == 0:
            self.__spectrum_method_b1.setChecked(True)
        elif self.parent.analysis_settings.spectrum_intensity_method == 1:
            self.__spectrum_method_b2.setChecked(True)
        else:
            self.__spectrum_method_b3.setChecked(True)
        self.__concentration_entry_1.setText(str(self.parent.analysis_settings.beer_s_law_concetration[0]))
        self.__concentration_entry_2.setText(str(self.parent.analysis_settings.beer_s_law_concetration[1]))
        self.__pathlength.setText(str(self.parent.analysis_settings.beer_s_law_pathlength))
        
