# -*- coding: utf-8 -*-
__author__ = ["Thiago Lopes", "Daniel Machado", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasilia"
__maintainer__ = "Thiago Lopes"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Nov 14 of 2017"
__version__ = "2.0.1"

from tkinter import *
from tkinter import filedialog


class Application(Frame):
    def __init__(self, toplevel):
        self.toplevel = toplevel
        self.toplevel.geometry('800x600')
        self.toplevel.resizable(width=False, height=False)
        self.menu = Menu(self.toplevel)
        self.toplevel.configure(menu=self.menu)
        self.filemenufile= Menu(self.menu)
        self.filemenufile.add_separator()
        self.menu.add_cascade(label="File", menu=self.filemenufile)
        self.filemenufile.add_command(label="New", command=self.restart)
        self.filemenufile.add_command(label="Open...", command=self.select_files)
        self.filemenufile.add_separator()
        self.filemenufile.add_command(label="Exit", command=self.leave)
        self.filemenufilapp = Menu(self.menu)
        self.menu.add_cascade(label="UV-vis Sp3ctrum P4tronum", menu=self.filemenufilapp)
        self.filemenufilapp.add_command(label="Version", command=self.show_version)
        self.filemenufilapp.add_command(label="About us", command=self.tell_about_us)
        self.filemenufilehelp = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.filemenufilehelp)
        self.filemenufilehelp.add_command(label="Manual", command=self.open_manual)
        self.filemenufilehelp.add_command(label="Tutorial Video", command=self.tutorial)
        self.box_container_interval_1 = Frame(self.toplevel, height=10)
        self.box_container_interval_1.pack()
        self.run_but_container = Frame(self.toplevel)
        Button(self.run_but_container, text="Open files", font="Helvetica", command=self.select_files).grid(row=0, column=0)
        Button(self.run_but_container, text="Calculate the spectrum", font="Helvetica", command=self.make_spectrum).grid(row=0, column=1)
        Button(self.run_but_container, text="Save in a .csv file", font="Helvetica", command=self.csv_file).grid(row=0, column=2)
        Button(self.run_but_container, text="Save in a .dat file", font="Helvetica", command=self.dat_file).grid(row=0, column=3)
        Button(self.run_but_container, text="Plot with Gnuplot", font="Helvetica", command=self.gnuplot, ).grid(row=0, column=4)
        Button(self.run_but_container, text="Plot with Pyplot", font="Helvetica", command=self.pyplot).grid(row=0, column=5)
        self.run_but_container.pack()
        self.file_container = Frame(self.toplevel)
        self.file_titles = Label(self.file_container, text="Selected Files:", font="Helvetica 25 bold").pack(anchor=NW)
        self.file_name_box = Listbox(self.file_container, relief=RIDGE, borderwidth=3, width=84, height=10, background="#8EF0F7", fg="#020041")
        self.file_name_box.pack()
        self.file_container.pack()
        self.box_container_interval_2 = Frame(self.toplevel, height=10)
        self.box_container_interval_2.pack()
        self.box_container_out = Frame(self.toplevel, relief=FLAT, borderwidth=1)
        self.box_container_in1 = Frame(self.box_container_out)
        self.box_container_line1 = Frame(self.box_container_in1,  relief=FLAT, borderwidth=1)
        self.box_container_line1_1 = Frame(self.box_container_line1)
        self.box_container_wl = Frame(self.box_container_line1_1, relief=FLAT, borderwidth=1)
        self.wl_rang_name = Label (self.box_container_line1_1, text="Wavelength Range ( nm ):", font="Helvetica 16 bold").pack(fill=X)
        self.box_container_line1_1.pack()
        self.box_container_line1_2 = Frame(self.box_container_line1)
        self.wl_rang_name_s = Label(self.box_container_line1_2, text="Start", font="Helvetica 14").pack(side="left")
        self.wl_rang_start = Entry(self.box_container_line1_2, width= 4).pack(side="left")
        self.wl_rang_name_e = Label(self.box_container_line1_2, text="End", font="Helvetica 14").pack(side="left")
        self.wl_rang_end = Entry(self.box_container_line1_2, width= 4, ).pack(side="left")
        self.box_container_line1_2.pack()
        self.box_container_line1_2 = Frame(self.box_container_line1)
        self.wl_n_points_name = Label(self.box_container_line1_2 , text="Number of points", font="Helvetica 14").pack()
        self.wl_n_points = Entry(self.box_container_line1_2 , width= 5).pack()
        self.box_container_line1_2 .pack()
        self.box_container_line1.pack(side="left")
        self.box_container_line2 = Frame(self.box_container_in1,  relief=FLAT, borderwidth=1)
        self.box_container_div = Frame(self.box_container_in1, relief=FLAT, borderwidth=1)
        self.wl_n_points_name = Label(self.box_container_div, text="                                     ", font="Helvetica 14").pack()
        self.box_container_div.pack(side="left")
        self.box_container_fwhm = Frame(self.box_container_line2,relief=FLAT, borderwidth=1)
        self.wl_rang_name_e = Label(self.box_container_fwhm, text='Full width at half maximum', font="Helvetica 16 bold").pack(fill=X)
        self.wl_rang_name_e = Label(self.box_container_fwhm, text=u'( cm\u207B\u2071 )', font="Helvetica 16 bold").pack(fill=X)
        self.fwhm = Entry(self.box_container_fwhm, width=5).pack()
        self.box_container_fwhm.pack(side="left")
        self.box_container_line2.pack(side="left")
        self.box_container_in1.grid(row=0)
        self.box_container_in2 = Frame(self.box_container_out)
        self.box_container_line3 = Frame(self.box_container_in2,  relief=FLAT, borderwidth=1)
        self.box_container_name_output = Frame(self.box_container_line3)
        self.name_output = Label(self.box_container_name_output, text="Output Name:", font="Helvetica 14 bold").pack()
        self.output = Entry(self.box_container_name_output, width=40).pack()
        self.box_container_name_output.pack(side="left")
        self.box_container_name_title = Frame(self.box_container_line3)
        self.name_title = Label(self.box_container_name_title, text="Title os the Plots:", font="Helvetica 14 bold").pack()
        self.title = Entry(self.box_container_name_title, width=40).pack()
        self.box_container_name_title.pack(side="left")
        self.box_container_line3.pack()
        self.box_container_in2.grid(row=1)
        self.box_container_out.pack()
        self.box_container_interval_3 = Frame(self.toplevel, height=10)
        self.box_container_interval_3.pack()
        self.all_logos_container = Frame(self.toplevel, background="#8EF0F7", relief=RIDGE, borderwidth=3)
        self.logo1 = PhotoImage(file="/Users/thiagolopes/Desktop/teste_gui/sp3ctrum.gif")
        self.logo2 = PhotoImage(file="/Users/thiagolopes/Desktop/teste_gui/leedmol.gif")
        self.logos_title_container = Frame(self.all_logos_container, background="#8EF0F7", borderwidth=5, width=300)
        self.lg1_title = Label(self.logos_title_container, text="UV-Vis", background="#8EF0F7", font="Helvetica 23 bold italic", fg="#020041").grid(row=0, column=0)
        self.lg1_title = Label(self.logos_title_container, text="Sp3ctrum P4tronus", background="#8EF0F7", font="Helvetica 23 bold italic", fg="#020041").grid(row=1, column=0)
        self.lg2_title = Label(self.logos_title_container, text="Powered by:", background="#8EF0F7", font="Helvetica 16 italic", fg="#020041").grid(row=2, column=0)
        self.lg2_title = Label(self.logos_title_container, text="LEEDMOL Group:", background="#8EF0F7", font="Helvetica 20 bold italic", fg="#020041").grid(row=3, column=0)
        self.logos_title_container.grid(row=0, column=0)
        self.lg1 = Label(self.all_logos_container, image=self.logo1, background="#8EF0F7", height=150, width=250).grid(row=0, column=1)
        self.lg2 = Label(self.all_logos_container, image=self.logo2, background="#8EF0F7", height=150, width=250).grid(row=0, column=2)
        self.all_logos_container.pack()

    def select_files(self):
        self.filenames = filedialog.askopenfilenames(initialdir="/", filetypes=[("Gaussian LOG files","*.log"), ("Gaussian OUTPUTS files","*.out")])
        for filename in self.filenames:
            self.file_name_box.insert(END, ".../"+filename.split('/')[-3]+"/"+filename.split('/')[-2]+"/"+filename.split('/')[-1])

    def make_spectrum(self):
        pass

    def csv_file(self):
        pass

    def dat_file(self):
        pass

    def gnuplot(self):
        pass

    def pyplot(self):
        pass

    def restart(self):
        pass

    def leave(self):
        pass

    def show_version(self):
        pass

    def tell_about_us(self):
        pass

    def open_manual(self):
        pass

    def tutorial(self):
        pass

