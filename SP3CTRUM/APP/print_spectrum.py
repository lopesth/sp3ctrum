# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Ueslei Vasconcelos", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__maintainer__ = ["Thiago Lopes", "Sandro Brito"]
__email__ = ["lopes.th.o@gmail.com", "brittosandro@gmail.com"]
__date__ = "Set 28 of 2018"
__version__ = "1.0.0"

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot
from os import remove
from PIL import Image
from PIL import PngImagePlugin
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from SP3CTRUM.APP.differential import FiniteDifferenceDerivative


class Print_Spectrum(object):

    def __init__(self, dir_target, file_names, start_wl, end_wl, title, resol, osc_color, curve_color,
                  exp_curv_color, log_names, plottypes, exp_abs_lines, exp_wl_lines, expColor, normalize_osc, numberOfFiles = 1):

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
        self.plottypes = plottypes
        self.expChoice = len(expColor)
        self.exp_abs_lines = exp_abs_lines
        self.exp_wl_lines = exp_wl_lines
        self.expColor = expColor
        self.normalize_osc = normalize_osc
        self.numberOfFiles = numberOfFiles

    def print_matplotlib(self):
        if self.plottypes == 0:
            namefiles = []
            for logname in self.log_names:
                namefiles.append(self.dir_target + "/" + (logname.split("/")[-1]).split(".log")[0] + ".png")
            self.singleGraphs(namefiles)
            self.show(self.graph, ["", "", "", ""])
        elif self.plottypes == 1:
            self.overlayGraph([self.dir_target + "/" + self.dir_target.split("/")[-1] + ".png"])
            self.show(self.graph, [""])
        try:
            for i in range(0, len(self.file_names), 1):
                remove(self.dir_target + "/" + self.file_names[i] + "_spectrum.dat")
                remove(self.dir_target + "/" + self.file_names[i] + "_rawData.dat")
        except:
            pass

    def take_osc_str_no_norm(self, name):
        wl = []
        osc = []
        with open(name, encoding="utf8", errors='ignore') as myFile:
            for line in myFile:
                wl.append(float(line.split()[0]))
                osc.append(float(line.split()[1]))
        return [wl, osc]

    def take_osc_str_norm(self, name):
        wl = []
        osc_t = []
        osc = []
        with open(name, encoding="utf8", errors='ignore') as myFile:
            for line in myFile:
                wl.append(float(line.split()[0]))
                osc_t.append(float(line.split()[1]))
        maxOsc = max(osc_t)
        for osc_element in osc_t:
            osc.append(osc_element/ maxOsc)
        return [wl, osc]

    def singleGraphs(self, namefiles):
        self.graph = []
        self.wl_list = []
        self.epslon_list = []
        for i in range(0, len(self.file_names), 1):
            self.graph.append(matplotlib.pyplot.figure(figsize=(8, 6)))
            wl = []
            epslon = []
            wl_ref = []
            osc_ref = []
            with open(self.dir_target + "/" + self.file_names[i] + "_spectrum.dat") as myFile:
                for line in myFile:
                    wl.append(float(line.split()[0]))
                    epslon.append(float(line.split()[1])/self.numberOfFiles)
            if self.normalize_osc == 0:
                list_wl_osc = self.take_osc_str_norm(self.dir_target + "/" + self.file_names[i] + "_rawData.dat")
            else:
                list_wl_osc = self.take_osc_str_no_norm(self.dir_target + "/" + self.file_names[i] + "_rawData.dat")
                with open(self.dir_target+"/"+self.file_names[i]+"_rawData.dat", encoding="utf8", errors='ignore') as myFile:
                    for line in myFile:
                        wl_ref.append(float(line.split()[0]))
                        osc_ref.append(float(line.split()[1]))
            wl_ref = list_wl_osc[0]
            osc_ref = list_wl_osc[1]
            a = self.graph[i].add_subplot(111)
            b = a.twinx()
            line1, = a.plot(wl, epslon, linestyle='solid', color=self.curve_color[i], fillstyle='none')
            line2, = b.plot(wl_ref, osc_ref, visible=False)
            for j in range(len(wl_ref)):
                b.vlines(wl_ref[j], 0, osc_ref[j], colors=self.osc_color[i], lw=1)
            self.graph[i].tight_layout()
            self.wl_list.append(wl)
            self.epslon_list.append(epslon)
            b.yaxis.set_visible(True)
            a.yaxis.set_visible(True)
            if self.normalize_osc == 0:
                b.set_ylabel("Relative Intensity", size=15)
                a.yaxis.set_visible(False)
            else:
                b.set_ylabel("Oscillator Strength (atomic units)", size=15)
                a.set_ylabel("Molar Absorptivity (L/mol.cm)", size=15)
                a.yaxis.set_label_position("right")
            a.set_xlabel("Wavelength (nm)", size=15)
            b.yaxis.tick_left()
            a.yaxis.tick_right()
            b.yaxis.set_label_position("left")
            a.tick_params(axis='both', which='major', labelsize=12)
            b.tick_params(axis='both', which='major', labelsize=12)
            if 0 < len(self.exp_wl_lines) < 5:
                for ref_exp in range(0, len(self.exp_wl_lines), 1):
                    a.vlines(self.exp_wl_lines[ref_exp], 0, self.exp_abs_lines[ref_exp], colors=self.expColor, lw=1)
                    a.annotate(str(self.exp_wl_lines[ref_exp]) + " nm", xy=(self.exp_wl_lines[ref_exp] +1, self.exp_abs_lines[ref_exp] -1), xytext=(self.exp_wl_lines[ref_exp] +30, self.exp_abs_lines[ref_exp] +100),
                    bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=1.0),
                    arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
            elif len(self.exp_wl_lines) > 4:
                line3, = a.plot(self.exp_wl_lines, self.exp_abs_lines, linestyle='solid', color=self.expColor, fillstyle='none')
            if len(self.title) > 0:
                matplotlib.pyplot.title(self.title)
            self.print(self.graph[i], namefiles[i])
            if len(self.file_names) > 1:
                a.axes.xaxis.set_ticklabels([])
                a.axes.yaxis.set_ticklabels([])
                b.axes.yaxis.set_ticklabels([])
                self.graph[i].set_size_inches(4.0, 3.0)


    def overlayGraph(self, namefile):
        self.wl_list = []
        self.epslon_list = []
        num = 0
        self.graph = [matplotlib.pyplot.figure(figsize=(8, 6))]
        for self.file_name in self.file_names:
            wl = []
            epslon = []
            wl_ref = []
            osc_ref = []
            with open(self.dir_target + "/" + self.file_name + "_spectrum.dat", encoding="utf8", errors='ignore') as myFile:
                for line in myFile:
                    wl.append(float(line.split()[0]))
                    epslon.append(float(line.split()[1])/self.numberOfFiles)
            if self.normalize_osc == 0:
                list_wl_osc = self.take_osc_str_norm(self.dir_target + "/" + self.file_name + "_rawData.dat")
            else:
                list_wl_osc = self.take_osc_str_no_norm(self.dir_target + "/" + self.file_name + "_rawData.dat")
                with open(self.dir_target+"/"+self.file_name+"_rawData.dat", encoding="utf8", errors='ignore') as myFile:
                    for line in myFile:
                        wl_ref.append(float(line.split()[0]))
                        osc_ref.append(float(line.split()[1]))
            wl_ref = list_wl_osc[0]
            osc_ref = list_wl_osc[1]
            a = self.graph[0].add_subplot(111)
            b = a.twinx()
            line1, = a.plot(wl, epslon, linestyle='solid', color=self.curve_color[num], fillstyle ='none')
            line2, = b.plot(wl_ref, osc_ref, visible = False)
            for i in range(len(wl_ref)):
                b.vlines(wl_ref[i], 0, osc_ref[i], colors=self.osc_color[num], lw =1)
            self.graph[0].tight_layout()
            b.yaxis.set_visible(False)
            self.wl_list.append(wl)
            self.epslon_list.append(epslon)
        b.yaxis.set_visible(True)
        a.yaxis.set_visible(True)
        if self.normalize_osc == 0:
                b.set_ylabel("Relative Intensity", size=15)
                a.yaxis.set_visible(False)
        else:
            b.set_ylabel("Oscillator Strength (atomic units)", size=15)
            a.set_ylabel("Molar Absorptivity (L/mol.cm)", size=15)
            a.yaxis.set_label_position("right")
        b.yaxis.tick_left()
        a.yaxis.tick_right()
        b.yaxis.set_label_position("left")
        a.set_xlabel("Wavelength (nm)")
        if len(self.title) > 0:
            matplotlib.pyplot.title(self.title)
        self.print(self.graph[0], namefile[0])

    def print(self, graph, name_file):
        graph.subplots_adjust(top=0.9, bottom=0.1, left=0.11, right=0.89, hspace=0.25, wspace=0.35)
        graph.savefig(name_file, transparent=True, dpi=self.resol)
        MetaDataPrint(name_file).reSave()

    def show(self, graph, name):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.root_out)
        self.root.title("Graph")
        if len(graph) == 1:
            self.graph_window = tk.Frame(self.root)
            canvas = FigureCanvasTkAgg(graph[0], master=self.graph_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side="top")
            titlecanvas = tk.Label(self.graph_window, text=name[0]).pack(side="top")
            self.button_cont = tk.Frame(self.graph_window)

        else:
            self.graph_window = tk.Frame(self.root)
            self.line1_canvas_container=tk.Frame(self.graph_window)
            self.canvas1_container = tk.Frame( self.line1_canvas_container)
            canvas1 = FigureCanvasTkAgg(graph[0], master=self.canvas1_container)
            canvas1.draw()
            canvas1.get_tk_widget().pack(side="top")
            titlecanvas1 = tk.Label(self.canvas1_container, text=name[0]).pack(side="top")
            self.canvas1_container.pack(side="left")
            self.canvas2_container = tk.Frame(self.line1_canvas_container)
            canvas2 = FigureCanvasTkAgg(graph[1], master=self.canvas2_container)
            canvas2.draw()
            canvas2.get_tk_widget().pack(side="top")
            titlecanvas2 = tk.Label(self.canvas2_container, text=name[1]).pack(side="top")
            self.canvas2_container.pack(side="left")
            self.line1_canvas_container.pack(side="top")

            if len(graph) > 2:
                self.line2_canvas_container = tk.Frame(self.graph_window)
                self.canvas3_container = tk.Frame(self.line2_canvas_container)
                canvas3 = FigureCanvasTkAgg(graph[2], master=self.canvas3_container)
                canvas3.draw()
                canvas3.get_tk_widget().pack(side="top")
                titlecanvas3 = tk.Label(self.canvas3_container, text=name[2]).pack(side="top")
                self.canvas3_container.pack(side="left")
                if len(graph) > 3:
                    self.canvas4_container = tk.Frame(self.line2_canvas_container)
                    canvas4 = FigureCanvasTkAgg(graph[3], master=self.canvas4_container)
                    canvas4.draw()
                    canvas4.get_tk_widget().pack(side="top")
                    titlecanvas4 = tk.Label(self.canvas4_container, text=name[3]).pack(side="top")
                    self.canvas4_container.pack(side="left")
                self.line2_canvas_container.pack(side="top")

        self.button_cont = tk.Frame(self.graph_window)
        self.quit_button = tk.Button(self.button_cont, text="Quit", command=self.root_out)
        self.quit_button.pack(side="left")
        self.second_derivative = tk.Button(self.button_cont, text="Second Derivative Plots",
                                           command=self.secondDerivative)
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
            derivative = FiniteDifferenceDerivative(self.epslon[i], self.wl[i])
            wlPeaks = derivative.criticalpoints
            second_der = derivative.secondDerivative
            graph = matplotlib.pyplot.figure(figsize=(8, 6))
            counter = 0
            minimalsY = []
            for x in second_der[1]:
                counter +=1
                if x  in wlPeaks:
                    minimalsY.append(second_der[0][counter])
            a = graph.add_subplot(111)
            a.plot(second_der[1], second_der[0], linestyle='solid', color=self.curve_color[i], fillstyle='none')
            for minimalX, minimalY in zip(wlPeaks, minimalsY):
                a.plot(minimalX, minimalY,'ro')
                a.annotate(str(minimalX) + " nm", xy=(minimalX + 2, minimalY - 2), xytext=(minimalX + 30,
                            minimalY + 30), bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                            arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0')
                           )
            graph.tight_layout()
            a.set_xlabel("Wavelength (nm)")
            a.set_ylabel("Second Derivative of Molar Absorptivity")
            a.axes.yaxis.set_ticklabels([])
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
        meta.add_text("Powered by", __credits__[0])
        self.file.save(self.target, 'PNG', pnginfo=meta)

if __name__ == '__main__':
     plot = Print_Spectrum()
