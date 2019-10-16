# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__date__ = "Oct 16 of 2019"
__version__ = "1.0.1"

import matplotlib
from matplotlib import pyplot
from matplotlib import patches
from PIL import Image
from PIL import PngImagePlugin

class PlotTransitions(object):

	def __init__(self, target_dir, output_file_names, title_chart_evolution, step, evol_plot_wl_choice, evol_plot_osc_choice, resol):
		self.target_dir = target_dir
		self.output_file_names = output_file_names
		self.title_chart_evolution = title_chart_evolution
		self.step = step
		self.evol_plot_wl_choice = evol_plot_wl_choice
		self.evol_plot_osc_choice = evol_plot_osc_choice
		self.resol = resol
		osc_list = []
		wl_list = []
		for rawData in output_file_names:
			rawData_osc_list = []
			rawData_wl_list = []
			with open(self.target_dir+"/"+rawData+"_rawData.dat", encoding="utf8", errors='ignore') as myFile:
				for line in myFile:
					y = line.split()
					rawData_osc_list.append(float(y[1]))
					rawData_wl_list.append(float(y[0]))
			osc_list.append(rawData_osc_list)
			wl_list.append(rawData_wl_list)
		temp = []
		for element in osc_list:
			temp.append(len(element))
		self.length_list = sorted(temp)[-1]

		self.dict_osc_wl_list = {}
		for number in range(0, self.length_list, 1):
			temp_list=[]
			for couter in range(0, len(self.output_file_names), 1):
				try:
					temp_list.append([osc_list[couter][number], wl_list[couter][number]])
				except:
					temp_list.append([0, 0])
			self.dict_osc_wl_list.update({str(number+1):temp_list})

	def plot_pyplot(self, states, colors):
		if self.evol_plot_osc_choice == 1:
			name_plot = self.target_dir +"/excitation_evolution_"
			color_num = 0
			graph = matplotlib.pyplot.figure(figsize=(8, 6))
			x = range(1, len(self.step)+1, 1)
			legends = []
			for excitation in states:
				osc = []
				for element in self.dict_osc_wl_list[excitation]:
					osc.append(element[0])
				a = graph.add_subplot(111)
				a.scatter(x, osc, marker=".", s =50, color=colors[color_num])
				a.plot(x, osc, color=colors[color_num])
				a.set_xticks(x)
				a.set_xticklabels(self.step)
				element_legend = matplotlib.patches.Patch(color=colors[color_num], label="State "+excitation)
				legends.append(element_legend)
				color_num =color_num+1
			box = a.get_position()
			a.set_position([box.x0, box.y0, box.width * 0.92, box.height])
			matplotlib.pyplot.xlabel("Time Evolution")
			matplotlib.pyplot.ylabel("Oscillator Strength (arbritary units)")
			matplotlib.pyplot.legend(handles=legends, loc='center left', bbox_to_anchor=(1.0, 0.5), ncol=1, fancybox=True, shadow=True)
			graph.savefig(name_plot+"oscl.png", transparent=True, dpi=self.resol)
		if self.evol_plot_wl_choice == 1:
			name_plot = self.target_dir +"/excitation_evolution_"
			color_num = 0
			graph = matplotlib.pyplot.figure(figsize=(8, 6))
			x = range(1, len(self.step)+1, 1)
			legends = []
			for excitation in states:
				wl = []
				for element in self.dict_osc_wl_list[excitation]:
					wl.append(element[1])
				a = graph.add_subplot(111)
				a.scatter(x, wl, marker=".", s =50, color=colors[color_num])
				a.plot(x, wl, color=colors[color_num])
				a.set_xticks(x)
				a.set_xticklabels(self.step)
				element_legend = matplotlib.patches.Patch(color=colors[color_num], label="State "+excitation)
				legends.append(element_legend)
				color_num =color_num+1
			box = a.get_position()
			a.set_position([box.x0, box.y0, box.width * 0.92, box.height])
			matplotlib.pyplot.xlabel("Time Evolution")
			matplotlib.pyplot.ylabel("Wavelength (nm)")
			matplotlib.pyplot.legend(handles=legends, loc='center left', bbox_to_anchor=(1.0, 0.5), ncol=1, fancybox=True, shadow=True)
			graph.savefig(name_plot+"wl.png", transparent=True, dpi=self.resol)
