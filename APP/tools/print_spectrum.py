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
from PIL import Image
from PIL import PngImagePlugin
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from APP.tools.differential import FiniteDifferenceDerivative


class Print_Spectrum(object):

    def __init__(self, dir_target, file_names, start_wl, end_wl, title, resol, osc_color, curve_color, exp_curv_color, log_names):
        self.file_names = file_names
        self.resol = resol
        self.start_wl = start_wl
        self.end_wl = end_wl
        self.title = title
        self.dir_target = dir_target
        self.osc_color = osc_color
        self.curve_color = curve_color
        self.exp_curv_color = exp_curv_color
        self.log_names = log_names


    def print_matplotlib(self):
        self.wl_list = []
        self.epslon_list = []
        num = 0
        self.graph = matplotlib.pyplot.figure(figsize=(8, 6))
        for self.file_name in self.file_names:
            wl = []
            epslon = []
            wl_ref = []
            osc_ref = []
            with open(self.dir_target+"/"+self.file_name+"_spectrum.dat") as myFile:
                for line in myFile:
                    wl.append(float(line.split()[0]))
                    epslon.append(float(line.split()[1]))
            with open(self.dir_target+"/"+self.file_name+"_rawData.dat") as myFile:
                for line in myFile:
                    wl_ref.append(float(line.split()[0]))
                    osc_ref.append(float(line.split()[1]))
            a = self.graph.add_subplot(111)
            b = a.twinx()
            line1, = a.plot(wl, epslon, linestyle = 'solid', color=self.curve_color[num], fillstyle ='none')
            line2, = b.plot(wl_ref, osc_ref, visible = False)
            for i in range(len(wl_ref)):
                b.vlines(wl_ref[i], 0, osc_ref[i], colors=self.osc_color[num], lw =2)
            self.graph.tight_layout()
            b.yaxis.set_visible(False)
            self.wl_list.append(wl)
            self.epslon_list.append(epslon)
            num+=1
        b.yaxis.set_visible(True)
        b.set_ylabel("Oscillator Strength (arbitrary unit)")
        a.set_ylabel("Molar Absorptivity (L/mol.cm)")
        a.set_xlabel("Wavelength (nm)")
        if len(self.title) > 0:
            matplotlib.pyplot.title(self.title)
        self.name_file = self.dir_target+"/"+self.dir_target.split("/")[-1]+".png"
        self.graph.subplots_adjust(top=0.9, bottom=0.1, left=0.11, right=0.89, hspace=0.25,wspace=0.35)
        self.graph.savefig(self.name_file, transparent=True, dpi=self.resol)
        MetaDataPrint(self.name_file).reSave()

    def show(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.root_out)
        self.root.title("Graph")
        canvas = FigureCanvasTkAgg(self.graph, master=self.root)
        canvas.show()
        canvas.get_tk_widget().pack(side="top")
        self.graph_window = tk.Frame(self.root)
        self.button_cont = tk.Frame(self.graph_window)
        self.quit_button = tk.Button(self.button_cont, text = "Quit", command=self.root_out)
        self.quit_button.pack(side = "left")
        self.second_derivative = tk.Button(self.button_cont, text = "Second Derivative Plots", command=self.secondDerivative)
        self.second_derivative.pack(sid="left")
        self.button_cont.pack()
        self.graph_window.pack(side="top")
        tk.mainloop()

    def root_out(self):
        self.root.quit()
        self.root.destroy()

    def secondDerivative(self):
        x = SecondDerivative(
                self.log_names, self.dir_target, self.start_wl, self.end_wl, self.title,
                self.resol,  self.curve_color, self.epslon_list, self.wl_list
            )
        tk.messagebox.showinfo("2nd Derivative Plots", "Second derivative images saved in working directory")


class SecondDerivative(object):

    def __init__(self, file_name, dir_target, start_wl, end_wl, title, resol, curve_color, epslon, wl):
        self.file_name = file_name
        self.dir_target = dir_target
        self.start_wl = start_wl
        self.end_wl = end_wl
        self.title = title
        self.resol = resol
        self.curve_color = curve_color
        self.epslon = epslon
        self.wl = wl
        self.graph = []
        for i in range(0, len(self.file_name), 1):
            Derivative = FiniteDifferenceDerivative(self.epslon[i], self.wl[i]).symmetricDerivative()
            SecondDerivative = FiniteDifferenceDerivative(Derivative[0], Derivative[1]).symmetricDerivative()
            graph = matplotlib.pyplot.figure(figsize=(8, 6))
            a = graph.add_subplot(111)
            a.plot(SecondDerivative[1], SecondDerivative[0], linestyle='solid', color=self.curve_color[i], fillstyle='none')
            graph.tight_layout()
            a.set_xlabel("Wavelength (nm)")
            a.set_ylabel("Second Derivative of Molar Absorptivity (L/mol.cm)")
            name_file = self.dir_target + "/" + (self.file_name[i].split("/")[-1]).split(".")[0] + "_2derivative.png"
            graph.subplots_adjust(top=0.9, bottom=0.1, left=0.11, right=0.89, hspace=0.25, wspace=0.35)
            graph.savefig(name_file, transparent=True, dpi=self.resol)
            MetaDataPrint(name_file).reSave()

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


