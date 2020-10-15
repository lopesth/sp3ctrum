from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator

box_title = "QGroupBox::title  { subcontrol-origin: margin; font-size: 12px; subcontrol-position: top ,left; }"

fwhm_tooltip = "The 'Find the best FWHM for the theoretical values that fits the experimental values?' button\n(in 'Versus Experimental Values' tab) is marked as Yes, so this option is disabled!"


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
        self.__fwhm_label1,  self.__fwhm_label2, self.__hwhm_entry = QLabel(self), QLabel(self), QLineEdit()
        self.__fwhm_label1.setText("FWHM value: ")
        self.__fwhm_label2.setText("cm<sup>-1</sup>")
        self.__hwhm_entry.setText('3226.22')
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
    
    @fwhm.setter
    def fwhm(self, value):
        self.__hwhm_entry.setText(value)
    
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
    

