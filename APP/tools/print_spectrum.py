# -*- coding: utf-8 -*-
__author__ = ["Thiago Lopes", "Daniel Machado", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasilia"
__maintainer__ = "Thiago Lopes"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Nov 17 of 2017"
__version__ = "3.0"

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot
import os, sys
from PIL import Image
from PIL import PngImagePlugin
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Print_Spectrum(object):

    def __init__(self, dir_target, file_name, start_wl, end_wl, end_epslon, end_osc, title, resol = 600, osc_color = "#4F4233", curve_color = "#020041", exp_curv_color = "#76449C"):
        self.file_name = file_name
        self.resol = resol
        self.start_wl = start_wl
        self.end_wl = end_wl
        self.end_osc = end_osc
        self.end_epslon = end_epslon
        self.title = title
        self.dir_target = dir_target
        self.osc_color = osc_color
        self.curve_color = curve_color
        self.exp_curv_color = exp_curv_color


    def print_matplotlib(self):
        wl = []
        epslon = []
        wl_ref = []
        osc_ref = []
        matplotlib.use("TkAgg")
        with open(self.dir_target+"/"+self.file_name+"_spectrum.dat") as myFile:
            for line in myFile:
                wl.append(float(line.split()[0]))
                epslon.append(float(line.split()[1]))
        with open(self.dir_target+"/"+self.file_name+"_rawData.dat") as myFile:
            for line in myFile:
                wl_ref.append(float(line.split()[0]))
                osc_ref.append(float(line.split()[1]))
        self.graph = matplotlib.pyplot.figure(figsize=(8,6))
        a = self.graph.add_subplot(111)
        b = a.twinx()
        line1, = a.plot(wl, epslon, linestyle = 'solid', color=self.curve_color, fillstyle ='none')
        line2, = b.plot(wl_ref, osc_ref, visible = False)
        for i in range(len(wl_ref)):
            b.vlines(wl_ref[i], 0, osc_ref[i], colors=self.osc_color, lw =2)
        self.graph.tight_layout()
        b.set_ylabel("Oscillator Strength (arbitrary unit)")
        a.set_ylabel("Molar Absorptivity (L/mol.cm)")
        a.set_xlabel("Wavelength (nm)")
        if len(self.title) > 0:
            matplotlib.pyplot.title(self.title)
        self.name_file = self.dir_target+"/"+self.file_name+".png"
        self.graph.subplots_adjust(top=0.9, bottom=0.1, left=0.11, right=0.89, hspace=0.25,
                    wspace=0.35)
        self.graph.savefig(self.name_file, transparent=True, dpi=self.resol)
        MetaDataPrint(self.name_file).reSave()

    def show(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.root_out())
        self.root.title("self.fraph " + self.name_file)
        canvas = FigureCanvasTkAgg(self.graph, master=self.root)
        canvas.show()
        canvas.get_tk_widget().pack(side="top")

        y = tk.Frame(self.root)
        x = tk.Button(y, text = "Quit", command=self.root_out)
        x.pack()
        y.pack(side="top")
        tk.mainloop()

    def root_out(self):
        self.root.quit()
        self.root.destroy()

class MetaDataPrint(object):

    def __init__(self, target):
        self.target = target
        self.file = Image.open(self.target)

    def reSave(self):
        meta = PngImagePlugin.PngInfo()
        meta.add_text("Created by", "UV-Vis Sp3ctrum P4tronum")
        meta.add_text("Version", __version__)
        meta.add_text("Powered by", __credits__)
        self.file.save(self.target, pnginfo=meta)


