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
        self.toplevel.config(bg='#FFFFFF')
        self.toplevel.geometry('800x600')
        self.toplevel.resizable(width=False, height=False)
        self.menu = Menu(self.toplevel)
        self.toplevel.configure(menu=self.menu)
        self.filemenufile= Menu(self.menu, tearoff=0, fg="#62338C")
        self.filemenufile.add_separator()
        self.menu.add_cascade(label="File", menu=self.filemenufile)
        self.filemenufile.add_command(label="Open", command=self.select_files)
        self.filemenufile.add_separator()
        self.filemenufile.add_command(label="Clear", command=self.restart)
        self.filemenufile.add_separator()
        self.filemenufile.add_command(label="Exit", command=self.leave)
        self.filemenufilapp = Menu(self.menu, fg="#62338C")
        self.menu.add_cascade(label="UV-vis Sp3ctrum P4tronum", menu=self.filemenufilapp)
        self.filemenufilapp.add_command(label="Version", command=self.show_version)
        self.filemenufilapp.add_command(label="About us", command=self.tell_about_us)
        self.filemenufilehelp = Menu(self.menu, fg="#62338C")
        self.menu.add_cascade(label="Help", menu=self.filemenufilehelp)
        self.filemenufilehelp.add_command(label="Manual", command=self.open_manual)
        self.filemenufilehelp.add_command(label="Tutorial Video", command=self.tutorial)
        self.box_container_interval_1 = Frame(self.toplevel)
        self.box_container_interval_1.pack()
        self.run_but_container = Frame(self.toplevel)
        self.run_call_bt = Button(self.run_but_container, text="Open files", font="Helvetica",
                                 command=self.select_files)
        self.run_call_bt.pack(side="left")
        self.make_spec_bt = Button(self.run_but_container, text="Calculate the spectrum", font="Helvetica",
                                   command=self.make_spectrum)
        self.make_spec_bt.configure(state=DISABLED)
        self.make_spec_bt.pack(side="left")
        self.save_csv_bt = Button(self.run_but_container, text="Save in a .csv file", font="Helvetica",
                                  command=self.csv_file)
        self.save_csv_bt.configure(state=DISABLED)
        self.save_csv_bt.pack(side="left")
        self.save_dat_bt = Button(self.run_but_container, text="Save in a .dat file", font="Helvetica",
                                  command=self.dat_file)
        self.save_dat_bt.configure(state=DISABLED)
        self.save_dat_bt.pack(side="left")
        self.gnuplot_bt = Button(self.run_but_container, text="Plot with Gnuplot", font="Helvetica",
                                 command=self.gnuplot)
        self.gnuplot_bt.configure(state=DISABLED)
        self.gnuplot_bt.pack(side="left")
        self.pyplot_bt = Button(self.run_but_container, text="Plot with Pyplot", font="Helvetica",
                                command=self.pyplot)
        self.pyplot_bt.configure(state=DISABLED)
        self.pyplot_bt.pack(side="left")
        self.run_but_container.pack()
        self.file_container = Frame(self.toplevel)
        self.file_titles = Label(self.file_container, text="Selected Files:", font="Helvetica 25 bold",
                                 fg="#263A90").pack(anchor=NW)
        self.file_name_box = Listbox(self.file_container, relief=RIDGE, borderwidth=3, width=84,
                                     height=10, background="#8EF0F7", fg="#263A90")
        self.file_name_box.pack()
        self.file_container.pack()
        self.box_container_interval_2 = Frame(self.toplevel, height=10)
        self.box_container_interval_2.pack()
        self.box_container_out = Frame(self.toplevel, relief=FLAT, borderwidth=1)
        self.box_container_in1 = Frame(self.box_container_out)
        self.box_container_line1 = Frame(self.box_container_in1,  relief=FLAT, borderwidth=1)
        self.box_container_line1_1 = Frame(self.box_container_line1)
        self.box_container_wl = Frame(self.box_container_line1_1, relief=FLAT, borderwidth=1)
        self.wl_rang_name = Label (self.box_container_line1_1, text="Wavelength Range ( nm ):", font="Helvetica 16 bold", fg="#DF0027").pack(fill=X)
        self.box_container_line1_1.pack()
        self.box_container_line1_2 = Frame(self.box_container_line1)
        self.wl_rang_name_s = Label(self.box_container_line1_2, text="Start", font="Helvetica 14", fg="#DF0027").pack(side="left")
        self.wl_rang_start_entry = Entry(self.box_container_line1_2, width= 4, fg="#263A90")
        self.wl_rang_start_entry.insert(END, '150')
        self.wl_rang_start_entry.pack(side="left")
        self.wl_rang_name_e = Label(self.box_container_line1_2, text="End", font="Helvetica 14", fg="#DF0027").pack(side="left")
        self.wl_rang_end_entry = Entry(self.box_container_line1_2, width= 4, fg="#263A90" )
        self.wl_rang_end_entry.insert(END, '350')
        self.wl_rang_end_entry.pack(side="left")
        self.box_container_line1_2.pack()
        self.box_container_line1_2 = Frame(self.box_container_line1)
        self.wl_n_points_name = Label(self.box_container_line1_2 , text="Number of points", fg="#DF0027", font="Helvetica 14").pack()
        self.wl_n_points_entry = Entry(self.box_container_line1_2 , width= 5, fg="#263A90")
        self.wl_n_points_entry.insert(END, '2000')
        self.wl_n_points_entry.pack()
        self.box_container_line1_2 .pack()
        self.box_container_line1.pack(side="left")
        self.box_container_line2 = Frame(self.box_container_in1,  relief=FLAT, borderwidth=1)
        self.box_container_div = Frame(self.box_container_in1, relief=FLAT, borderwidth=1)
        self.wl_n_points_name = Label(self.box_container_div, text="                                     ", font="Helvetica 14").pack()
        self.box_container_div.pack(side="left")
        self.box_container_fwhm = Frame(self.box_container_line2,relief=FLAT, borderwidth=1)
        self.fwhm_name = Label(self.box_container_fwhm, text='Full Width at Half Maximum', font="Helvetica 16 bold", fg="#DF0027").pack(fill=X)
        self.fwhm_name2 = Label(self.box_container_fwhm, text=u'FWHM ( cm\u207B\u2071 ):', font="Helvetica 16 bold", fg="#DF0027").pack(fill=X)
        self.fwhm_entry = Entry(self.box_container_fwhm, width=7, fg="#263A90")
        self.fwhm_entry.insert(END, '3226.22')
        self.fwhm_entry.pack()
        self.box_container_fwhm.pack(side="left")
        self.box_container_line2.pack(side="left")
        self.box_container_in1.grid(row=0)
        self.box_container_in2 = Frame(self.box_container_out)
        self.box_container_line3 = Frame(self.box_container_in2,  relief=FLAT, borderwidth=1)
        self.box_container_name_output = Frame(self.box_container_line3)
        self.name_output = Label(self.box_container_name_output, text="Output Name:", font="Helvetica 14 bold", fg="#DF0027").pack()
        self.output_entry = Entry(self.box_container_name_output, width=40, fg="#263A90")
        self.output_entry.pack()
        self.box_container_name_output.pack(side="left")
        self.box_container_name_title = Frame(self.box_container_line3)
        self.name_title = Label(self.box_container_name_title, text="Title of the Plots (Optional):", font="Helvetica 14 bold", fg="#DF0027").pack()
        self.title_entry = Entry(self.box_container_name_title, width=40, fg="#263A90")
        self.title_entry.pack()
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
        self.lg1_title = Label(self.logos_title_container, text="UV-Vis", background="#8EF0F7", font="Helvetica 23 bold italic", fg="#62338C").grid(row=0, column=0)
        self.lg1_title = Label(self.logos_title_container, text="Sp3ctrum P4tronus", background="#8EF0F7", font="Helvetica 23 bold italic", fg="#62338C").grid(row=1, column=0)
        self.lg2_title = Label(self.logos_title_container, text="Powered by:", background="#8EF0F7", font="Helvetica 16 italic", fg="#62338C").grid(row=2, column=0)
        self.lg2_title = Label(self.logos_title_container, text="LEEDMOL Group:", background="#8EF0F7", font="Helvetica 20 bold italic", fg="#62338C").grid(row=3, column=0)
        self.logos_title_container.grid(row=0, column=0)
        self.lg1 = Label(self.all_logos_container, image=self.logo1, background="#8EF0F7", height=150, width=250).grid(row=0, column=1)
        self.lg2 = Label(self.all_logos_container, image=self.logo2, background="#8EF0F7", height=150, width=250).grid(row=0, column=2)
        self.all_logos_container.pack()

    def select_files(self):
        self.filenames = filedialog.askopenfilenames(initialdir="/", filetypes=[("Gaussian LOG files","*.log"), ("Gaussian OUTPUTS files","*.out")])
        for filename in self.filenames:
            self.file_name_box.insert(END, ".../"+filename.split('/')[-3]+"/"+filename.split('/')[-2]+"/"+filename.split('/')[-1])
        self.make_spec_bt.configure(state=NORMAL)
        self.output_entry.insert(END, filename.split('/')[-2].lower())

    def make_spectrum(self):
        self.save_csv_bt.configure(state=NORMAL)
        self.save_dat_bt.configure(state=NORMAL)
        self.run_call_bt.configure(state=DISABLED)
        try:
            self.wl_rang = [float(self.wl_rang_start_entry.get()), float(self.wl_rang_end_entry.get())]
        except:
            pass
        try:
            self.wl_n_points = int(self.wl_n_points_entry.get())
        except:
            pass
        try:
            self.fwhm = float(self.fwhm_entry.get())
        except:
            pass
        self.output_file_name = self.output_entry.get()
        if len(self.output_file_name) == 0:
            self.output_file_name = "void_name"
        self.title_chart = self.title_entry.get()

    def csv_file(self):
        self.gnuplot_bt.configure(state=NORMAL)
        self.pyplot_bt.configure(state=NORMAL)
        self.make_spec_bt.configure(state=DISABLED)

    def dat_file(self):
        self.gnuplot_bt.configure(state=NORMAL)
        self.pyplot_bt.configure(state=NORMAL)
        self.make_spec_bt.configure(state=DISABLED)

    def gnuplot(self):
        pass

    def pyplot(self):
        pass

    def restart(self):
        self.save_csv_bt.configure(state=DISABLED)
        self.save_dat_bt.configure(state=DISABLED)
        self.gnuplot_bt.configure(state=DISABLED)
        self.pyplot_bt.configure(state=DISABLED)
        self.make_spec_bt.configure(state=DISABLED)
        self.run_call_bt.configure(state=NORMAL)
        self.file_name_box.delete(0, END)
        self.wl_rang_start_entry.delete(0, END)
        self.wl_rang_end_entry.delete(0, END)
        self.wl_n_points_entry.delete(0, END)
        self.fwhm_entry.delete(0, END)
        self.output_entry.delete(0, END)
        self.title_entry.delete(0, END)
        self.wl_rang_start_entry.insert(END, '150')
        self.wl_rang_end_entry.insert(END, '350')
        self.wl_n_points_entry.insert(END, '2000')
        self.fwhm_entry.insert(END, '3226.22')
        self.filenames = 0

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

