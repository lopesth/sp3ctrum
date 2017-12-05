# -*- coding: utf-8 -*-
__author__ = ["Thiago Lopes", "Daniel Machado", "Heibbe Oliveira"]
__credits__ = "LEEDMOL group - Institute of Chemistry at Universidade de Brasilia"
__maintainer__ = "Thiago Lopes"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Nov 17 of 2017"
__version__ = "2.0.1"

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import Button
import sys, os, webbrowser
from APP.tools.gaussian_conv import Gaussian_Convolution
from APP.tools.get_osc import Get_Osc
from APP.tools.print_spectrum import Print_Spectrum

class Application(Frame):
    def __init__(self, toplevel):
        Frame.__init__(self, toplevel)
        if sys.platform == "win32":
            self.src = os.path.realpath(__file__).replace("tools\sp3ctrum_gui.py", "")
        else:
            self.src = os.path.realpath(__file__).replace("tools/sp3ctrum_gui.py", "")
        self.toplevel = toplevel
        self.toplevel.protocol("WM_DELETE_WINDOW", self.leave)
        self.toplevel.configure(bg="#8EF0F7")
        Frame.__init__(self)
        self.dir = os.getcwd()
        self.filenames = []
        self.toplevel.config()
        self.toplevel.geometry("800x650")
        self.toplevel.resizable(width=False, height=False)
        self.setMenu()
        self.setStyle()
        self.noteStructures()
        self.guiTab1()
        self.guiTab2()
        self.guiTab3()
        self.guiTab4()
        self.guiTab5()
        self.guiTab6()
        self.guiButtons()
        self.guiLogos()


    def setStyle(self):
        self.style = ttk.Style()

        self.style.theme_create("leedmol", settings={
            "TNotebook": {
                "configure": {
                    "background": "#8EF0F7",
                    "borderwidth": "2",
                    "relief": "RIDGE",
                    "padding": "10"
                }
            },
            "TNotebook.Tab": {
                "configure": {
                    "padding": "2",
                    "relief": "RIDGE", "borderwidth": "2",
                    "background": "#DF0027",
                    "foreground": "#FFFFFF",
                    "expand": [("selected", [1, 1, 1, 0])]
                },
                "map": {
                    "background": [("selected", "#62338C"), ("disabled", "#8EF0F7")],
                    "foreground": [("selected", "#FFFFFF"), ("disabled", "#828585")]},
                "expand": [("selected", [1, 1, 1, 0])],
            }
        })
        self.style.theme_use("leedmol")

    def setMenu(self):
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
        self.filemenufilapp.add_command(label="About us", command=Second_Window(self.toplevel, self.src).tell_about_us)
        self.filemenufilehelp = Menu(self.menu, fg="#62338C")
        self.menu.add_cascade(label="Help", menu=self.filemenufilehelp)
        self.filemenufilehelp.add_command(label="Manual", command=self.open_manual)
        self.filemenufilehelp.add_command(label="Tutorial Video", command=self.tutorial)

    def noteStructures(self):
        self.note = ttk.Notebook(self.toplevel, height=400)
        self.note.pack(fill='both', padx=5, pady=5)
        self.note1_struct = Frame(self.note, background="#FFFFFF")
        self.note1_struct.pack()
        self.note2_struct = Frame(self.note, background="#FFFFFF")
        self.note2_struct.pack()
        self.note3_struct = Frame(self.note, background="#FFFFFF")
        self.note3_struct.pack()
        self.note4_struct = Frame(self.note, background="#FFFFFF")
        self.note4_struct.pack()
        self.note5_struct = Frame(self.note, background="#FFFFFF")
        self.note5_struct.pack()
        self.note6_struct = Frame(self.note, background="#FFFFFF")
        self.note6_struct.pack()
        self.note.add(self.note1_struct, text="Files")
        self.note.add(self.note2_struct, text="Spectrum Parameters")
        self.note.add(self.note3_struct, text="Plot Details")
        self.note.add(self.note4_struct, text="Versus Experimental Values")
        self.note.add(self.note5_struct, text="MD Options")
        self.note.add(self.note6_struct, text="Advanced Options")
        self.note.tab(self.note2_struct, state="disabled")
        self.note.tab(self.note3_struct, state="disabled")
        self.note.tab(self.note4_struct, state="disabled")
        self.note.tab(self.note5_struct, state="disabled")
        self.note.tab(self.note6_struct, state="disabled")

    def guiButtons(self):
        self.run_but_container = Frame(self.toplevel, bg="#8EF0F7")
        self.make_spec_bt = Button(
            self.run_but_container, text="Calculate Spectrum", font="Helvetica", command=self.make_spectrum,
            highlightbackground="#8EF0F7", pady=2, relief=FLAT, borderwidth=0
        )
        self.make_spec_bt.configure(state=DISABLED)
        self.make_spec_bt.grid(row = 0, column = 0, padx=5)
        self.save_adv_bt = Button(
            self.run_but_container, text="Save advanced data", font="Helvetica", command=self.adv_file,
            highlightbackground="#8EF0F7", pady=2, relief=FLAT
        )
        self.save_adv_bt.configure(state=DISABLED)
        self.save_adv_bt.grid(row = 0, column = 1, padx=5)
        self.save_simp_bt = Button(
            self.run_but_container, text="Save simple data", font="Helvetica", command=self.simple_file,
            highlightbackground="#8EF0F7", pady=2, relief=FLAT
        )
        self.save_simp_bt.configure(state=DISABLED)
        self.save_simp_bt.grid(row = 0, column = 2, padx=5)
        self.pyplot_bt = Button(
            self.run_but_container, text="Plot Spectrum", font="Helvetica", command=self.pyplot,
            highlightbackground ="#8EF0F7", pady=2,
            relief=FLAT
        )
        self.pyplot_bt.configure(state=DISABLED)
        self.pyplot_bt.grid(row = 0, column = 4, padx=5)
        self.run_but_container.pack()

    def guiTab1(self):
        self.choice_file_type = IntVar()
        self.choice_log_type = IntVar()
        self.choice_file_type.set(0)
        self.choice_log_type.set(0)
        self.choice_log_type=Label(
            self.note1_struct, text="Output Type Files:", font="Helvetica 14 bold", fg="#263A90", background="#FFFFFF"
        ).pack(anchor=NW, pady=5, padx=20)
        self.rb1_choice_log_type = Radiobutton(
            self.note1_struct, text="Gaussian (G09 and G16)", variable=self.choice_log_type,
            value=0, background="#FFFFFF"
        )
        self.rb1_choice_log_type.pack(anchor=NW, padx=20)
        self.rb1_choice_log_type.select()
        self.choice_files_type = Label(
            self.note1_struct, text="Choose the type of analysis (with one file or with multiple file overlay):",
            font="Helvetica 14 bold", fg="#263A90", background="#FFFFFF"
        ).pack(anchor=NW, pady=5, padx=20)
        self.open_files_BT = Frame(self.note1_struct, background="#FFFFFF")

        self.rb2_choice_file_type = Radiobutton(
            self.open_files_BT, text="Independent Files", variable=self.choice_file_type,
            value=1, command=self.enable_file_bt, background="#FFFFFF"
        )
        self.rb2_choice_file_type.pack(side="left")

        self.rb3_choice_file_type = Radiobutton(
            self.open_files_BT, text="Multiple Files from MD", variable=self.choice_file_type,
            value=2, command=self.enable_file_bt, background="#FFFFFF"
        )
        self.rb3_choice_file_type.pack(side="left")

        self.run_call_bt = Button(
            self.open_files_BT, text="Open files", font="Helvetica",
            state=DISABLED, command=self.select_files, background="#FFFFFF"
        )
        self.run_call_bt.pack(side="left")
        self.open_files_BT.pack(anchor=NW, pady=5, padx=20)

        self.file_container = Frame(self.note1_struct, background="#FFFFFF")
        self.file_titles = Label(
            self.file_container, text="Selected Files:", font="Helvetica 25 bold", fg="#263A90", background="#FFFFFF"
        )
        self.file_titles.pack(anchor=NW, pady=5, padx=20)
        self.file_name_box = Listbox(
            self.file_container, relief=RIDGE, borderwidth=3, width=82,height=11, background="#8EF0F7", fg="#263A90"
        )
        self.file_name_box.pack(anchor=NW, pady=5, padx=20)
        self.file_container.pack()

    def guiTab2(self):
        self.box_container_interval_2 = Frame(self.note2_struct, background="#FFFFFF")
        self.box_container_interval_2.pack()
        self.box_container_out = Frame(self.note2_struct, relief=FLAT, borderwidth=1, background="#FFFFFF")
        self.box_container_in1 = Frame(self.box_container_out, background="#FFFFFF")
        self.box_container_line1 = Frame(self.box_container_in1, relief=FLAT, borderwidth=1, background="#FFFFFF")
        self.box_container_line1_1 = Frame(self.box_container_line1, background="#FFFFFF")
        self.box_container_wl = Frame(self.box_container_line1_1, relief=FLAT, borderwidth=1, background="#FFFFFF")
        self.wl_rang_name = Label(
            self.box_container_line1_1, text="Wavelength Range ( nm ):",
            font="Helvetica 16 bold", fg="#DF0027", bg="#FFFFFF"
        ).pack(fill=X)
        self.box_container_line1_1.pack()
        self.box_container_line1_2 = Frame(self.box_container_line1, background="#FFFFFF")
        self.wl_rang_name_s = Label(self.box_container_line1_2, text="Start", font="Helvetica 14",
                                    fg="#DF0027", background="#FFFFFF").pack(side="left")
        self.wl_rang_start_entry = Entry(
            self.box_container_line1_2, width=4, fg="#263A90", borderwidth=2, relief=RIDGE, background="#FFFFFF"
        )
        self.wl_rang_start_entry.insert(END, '150')
        self.wl_rang_start_entry.pack(side="left")
        self.wl_rang_name_e = Label(self.box_container_line1_2, text="End", font="Helvetica 14",
                                    fg="#DF0027", background="#FFFFFF").pack(side="left")
        self.wl_rang_end_entry = Entry(
            self.box_container_line1_2, width=4, fg="#263A90", borderwidth=2, relief=RIDGE, background="#FFFFFF"
        )
        self.wl_rang_end_entry.insert(END, '350')
        self.wl_rang_end_entry.pack(side="left")
        self.box_container_line1_2.pack()
        self.box_container_line1_2 = Frame(self.box_container_line1, background="#FFFFFF")
        self.wl_n_points_name = Label(
            self.box_container_line1_2, text="Number of points", fg="#DF0027",
            font="Helvetica 14", background="#FFFFFF"
        ).pack()
        self.wl_n_points_entry = Entry(
            self.box_container_line1_2, width=5, fg="#263A90", borderwidth=2, relief=RIDGE, background="#FFFFFF"
        )
        self.wl_n_points_entry.insert(END, '10000')
        self.wl_n_points_entry.pack()
        self.box_container_line1_2.pack()
        self.box_container_line1.pack(side="left")
        self.box_container_line2 = Frame(self.box_container_in1, relief=FLAT, borderwidth=1, background="#FFFFFF")
        self.box_container_div = Frame(self.box_container_in1, relief=FLAT, borderwidth=1, background="#FFFFFF")
        self.wl_n_points_name = Label(
            self.box_container_div, text="                                     ",
            font="Helvetica 14", background="#FFFFFF"
        ).pack()
        self.box_container_div.pack(side="left")
        self.box_container_fwhm = Frame(self.box_container_line2, relief=FLAT, borderwidth=1, background="#FFFFFF")
        self.fwhm_name = Label(
            self.box_container_fwhm, text='Full Width at Half Maximum',
            font="Helvetica 16 bold", fg="#DF0027", background="#FFFFFF"
        ).pack(fill=X)
        self.fwhm_name2 = Label(self.box_container_fwhm, text=u'FWHM (cm\u207B\u00B9):',
                                font="Helvetica 16 bold", fg="#DF0027", background="#FFFFFF").pack(fill=X)
        self.fwhm_entry = Entry(
            self.box_container_fwhm, width=7, fg="#263A90", borderwidth=2, relief=RIDGE, background="#FFFFFF")
        self.fwhm_entry.insert(END, '3226.22')
        self.fwhm_entry.pack()
        self.box_container_fwhm.pack(side="left")
        self.box_container_line2.pack(side="left")
        self.box_container_in1.grid(row=0)
        self.box_container_out.pack()

    def guiTab3(self):
        self.box_container_plot = Frame(self.note3_struct, relief=FLAT, borderwidth=0, background="#FFFFFF")
        self.name_title = Label(self.box_container_plot, text="Title of the Plots (Optional):",
                                font="Helvetica 14 bold", fg="#DF0027", background="#FFFFFF").pack(side="left")
        self.title_entry = Entry(
            self.box_container_plot, width=60, fg="#263A90", borderwidth=2, relief=RIDGE, background="#FFFFFF")
        self.title_entry.pack(side="left")
        self.box_container_plot.pack(pady=5)
        self.box_container_curve_colors = Frame(self.note3_struct, relief=FLAT, borderwidth=0, background="#FFFFFF")

        self.title_color_curve = Label(
            self.box_container_curve_colors, text="Color of Curve (CSS Hex Style, for each .log file):",
            font="Helvetica", fg="#DF0027", background="#FFFFFF").pack(side="left")
        self.entry_color_curve_list = []

        for i in range(0, 5, 1):
            entry_color_curve1 = Entry(
                self.box_container_curve_colors, width=8, fg="#263A90", borderwidth=2,
                relief=RIDGE, background="#FFFFFF")
            entry_color_curve1.insert(END, '#020041')
            entry_color_curve1.pack(side="left")
            self.entry_color_curve_list.append(entry_color_curve1)

        self.box_container_curve_colors.pack(side="top", pady=5, anchor=W, padx=10)

        self.box_container_drop_colors = Frame(self.note3_struct, relief=FLAT, borderwidth=0, background="#FFFFFF")
        self.title_color_drop = Label(
            self.box_container_drop_colors, text="Color of Oscillators (CSS Hex Style, for each .log file):",
                                font="Helvetica", fg="#DF0027", background="#FFFFFF").pack(side="left")
        self.entry_color_drop_list = []

        for i in range(0, 5, 1):
            entry_color_drop = Entry(
                self.box_container_drop_colors, width=8, fg="#263A90",
                borderwidth=2, relief=RIDGE, background="#FFFFFF")
            entry_color_drop.insert(END, '#4F4233')
            entry_color_drop.pack(side="left")
            self.entry_color_drop_list.append(entry_color_drop)
        self.box_container_drop_colors.pack(side="top", pady=5, anchor=W, padx=10)

        for i in range(1, 5, 1):
            self.entry_color_drop_list[i].delete(0, END)
            self.entry_color_curve_list[i].delete(0, END)
            self.entry_color_curve_list[i].configure(state="disabled", borderwidth=0, background="#FFFFFF")
            self.entry_color_drop_list[i].configure(state="disabled", borderwidth=0, background="#FFFFFF")


        self.box_container_res = Frame(self.note3_struct, relief=FLAT, borderwidth=0, background="#FFFFFF")
        self.title_res = Label(self.box_container_res, text="Resolution of Plot (dpi):",
                                font="Helvetica", fg="#DF0027", background="#FFFFFF").pack(side="left")
        self.entry_res = Entry(
            self.box_container_res, width=4, fg="#263A90", borderwidth=2, relief=RIDGE, background="#FFFFFF")
        self.entry_res.insert(END, '300')
        self.entry_res.pack()
        self.box_container_res.pack(side="top", pady=5, anchor=W, padx=10)
        self.checkbuttonplot_box=Frame(self.note3_struct, relief=FLAT, borderwidth=0, background="#FFFFFF")
        self.plottypes = IntVar(0)
        self.checkbuttonplot_name=Label(
            self.checkbuttonplot_box, text="Plot Types:", fg="#DF0027", background="#FFFFFF").pack(side="left")
        self.checkbuttonplot1 = Radiobutton(
            self.checkbuttonplot_box, text="Independent Plots", variable=self.plottypes,
            value=0, background="#FFFFFF")
        self.checkbuttonplot2 = Radiobutton(
            self.checkbuttonplot_box, text="Overlay Plots", variable=self.plottypes,
            value=1, background="#FFFFFF")
        self.checkbuttonplot1.pack(side="left")
        self.checkbuttonplot2.pack(side="left")
        self.checkbuttonplot_box.pack(side="top", pady=5, anchor=W, padx=10)


    def guiTab4(self):
        pass

    def guiTab5(self):
        self.evol_plot_osc_choice = IntVar(0)
        self.evol_plot_wl_choice = IntVar(0)
        self.box_evoltuionOption = Frame( self.note5_struct,relief=FLAT, borderwidth=0, bg = "#FFFFFF")
        self.box_evoltuionOption_oscillator = Frame(
            self.box_evoltuionOption, relief=FLAT, borderwidth=0, bg = "#FFFFFF")
        self.text_oscillator_evolution = Label(
            self.box_evoltuionOption_oscillator,text="Evolution Plot for Oscillator Forces:", bg = "#FFFFFF"
        ).pack(side="left", padx=10)
        self.evol_plot_osc_Nbt = Radiobutton(
            self.box_evoltuionOption_oscillator, text="No", variable=self.evol_plot_osc_choice,
            value=0, background="#FFFFFF"
        )
        self.evol_plot_osc_Ybt = Radiobutton(
            self.box_evoltuionOption_oscillator, text="Yes", variable=self.evol_plot_osc_choice,
            value=1, background="#FFFFFF"
        )
        self.evol_plot_osc_Nbt.pack(side="left")
        self.evol_plot_osc_Ybt.pack(side="left")
        self.box_evoltuionOption_oscillator.pack(side="top", padx=10, pady=5)
        self.box_evoltuionOption_wl = Frame(
            self.box_evoltuionOption, relief=FLAT, borderwidth=0, bg="#FFFFFF")
        self.text_wl_evolution = Label(
            self.box_evoltuionOption_wl, text="Evolution Plot for Wavelength:", bg="#FFFFFF"
        ).pack(side="left", padx=27)
        self.evol_plot_wl_Nbt = Radiobutton(
            self.box_evoltuionOption_wl, text="No", variable=self.evol_plot_wl_choice,
            value=0, background="#FFFFFF"
        )
        self.evol_plot_wl_Ybt = Radiobutton(
            self.box_evoltuionOption_wl, text="Yes", variable=self.evol_plot_wl_choice,
            value=1, background="#FFFFFF"
        )
        self.evol_plot_wl_Nbt.pack(side="left")
        self.evol_plot_wl_Ybt.pack(side="left")
        self.box_evoltuionOption_wl.pack(side="top", padx=10, pady=5, anchor=W)
        self.box_evoltuionOption.pack(side="top", anchor=W)


    def guiTab6(self):
        self.box_container_adv = Frame(self.note6_struct, relief=FLAT, borderwidth=0, background="#FFFFFF")
        self.name_output = Label(self.box_container_adv, text="Base of Output Names:",
                                 font="Helvetica 14 bold", fg="#DF0027", background="#FFFFFF").pack(side="left")
        self.output_entry = Entry(
            self.box_container_adv, width=60, fg="#263A90", borderwidth=2, relief=RIDGE, background="#FFFFFF")
        self.output_entry.pack(side="left")
        self.box_container_adv.pack(pady=5)


    def guiLogos(self):
        self.all_logos_container = Frame(self.toplevel, background="#8EF0F7", borderwidth=0)
        self.logo1 = PhotoImage(file=self.src+"icons/sp3ctrum_b.gif")
        self.logo2 = PhotoImage(file=self.src+"icons/leedmol_b.gif")
        self.logos_title_container = Frame(self.all_logos_container, background="#8EF0F7", borderwidth=5, width=300)
        self.lg1_title = Label(self.logos_title_container,   text="UV-Vis", background="#8EF0F7",
                               font="Helvetica 23 bold italic", fg="#62338C").grid(row=0, column=0)
        self.lg1_title = Label(self.logos_title_container,   text="Sp3ctrum P4tronus", background="#8EF0F7",
                               font="Helvetica 23 bold italic", fg="#62338C").grid(row=1, column=0)
        self.lg2_title = Label(self.logos_title_container,   text="Powered by:", background="#8EF0F7",
                               font="Helvetica 16 italic", fg="#62338C").grid(row=2, column=0)
        self.lg2_title = Label(self.logos_title_container,   text="LEEDMOL Group:", background="#8EF0F7",
                               font="Helvetica 20 bold italic", fg="#62338C").grid(row=3, column=0)
        self.logos_title_container.grid(row=0, column=0)
        self.lg1 = Label(self.all_logos_container,  image=self.logo1, background="#8EF0F7",
                         height=150, width=250).grid(row=0, column=1)
        self.lg2 = Label(self.all_logos_container, image=self.logo2, background="#8EF0F7",
                         height=150, width=250).grid(row=0, column=2)
        self.all_logos_container.pack()

    def select_files(self):
        self.file_name_box.delete(0, END)
        self.operationMode = self.choice_file_type.get()
        if self.choice_file_type.get() == 1:
            self.filenames = []
            self.filenames_ = filedialog.askopenfilenames(
                initialdir="/", filetypes=[("Gaussian LOG files","*.log"), ("Gaussian OUTPUTS files","*.out")]
            )
            if len(self.filenames_) > 4:
                messagebox.showinfo(
                    "Maximum number of files", "Let's use only the first 4 files of the input."
                )
            for filename in self.filenames_[0:4]:
                self.filenames.append(filename)

            for i in range(1, len(self.filenames), 1):
                self.entry_color_curve_list[i].configure(state="normal", borderwidth=2)
                self.entry_color_drop_list[i].configure(state="normal", borderwidth=2)
                self.entry_color_curve_list[i].delete(0, END)
                self.entry_color_drop_list[i].delete(0, END)
                self.entry_color_curve_list[i].insert(END, '#020041')
                self.entry_color_drop_list[i].insert(END, '#4F4233')
        else:
            self.md = MDfilenames(self)
            self.toplevel.wait_window(self.md.window)
            self.filenames = self.md.returnFileNames()
        for filename in self.filenames:
            fn_div = filename.split('/')
            self.file_name_box.insert(
                    END, ".../"+fn_div[-4]+"/"+fn_div[-3]+"/"+fn_div[-2]+"/"+fn_div[-1]
            )
        self.target_dir = "/".join(self.filenames[-1].split("/")[0:-1])
        self.note.tab(self.note2_struct, state="normal")
        self.note.tab(self.note3_struct, state="normal")
        self.note.tab(self.note4_struct, state="normal")
        self.note.tab(self.note5_struct, state="normal")
        self.note.tab(self.note6_struct, state="normal")
        self.make_spec_bt.configure(state=NORMAL)
        self.output_entry.delete(0, END)
        self.output_entry.insert(0, self.filenames[-1].split("/")[-2].lower())

    def make_spectrum(self):
        if self.choice_file_type.get() == 1:
            self.makeSpectrum()
        else:
            self.makeSpectrumMD()

    def getSimpleValues(self):
        error = 0
        start_a = 1
        end_a = 1
        self.curve_color = [self.entry_color_curve_list[0].get()]
        self.osc_color = [self.entry_color_drop_list[0].get()]
        try:
            start_a = float(self.wl_rang_start_entry.get())
            self.wl_rang_start_entry.configure(fg="#263A90", bg="#FFFFFF")
        except:
            self.wl_rang_start_entry.configure(bg="#DF0027", fg="#FFFFFF")
            messagebox.showinfo(
                "Incoherent input values", "One of the wavelength range values does not make sense."
            )
            error += 1
        try:
            end_a = float(self.wl_rang_end_entry.get())
            self.wl_rang_end_entry.configure(fg="#263A90", bg="#FFFFFF")
        except:
            self.wl_rang_end_entry.configure(bg="#DF0027", fg="#FFFFFF")
            messagebox.showinfo("Incoherent input values",
                                "One of the wavelength range values does not make sense.")
            error +=1
        self.wl_rang = [start_a, end_a]
        try:
            self.wl_n_points = int(self.wl_n_points_entry.get())
            self.wl_n_points_entry.configure(fg="#263A90", bg="#FFFFFF")
            if self.wl_n_points < 500:
                error+=1
                messagebox.showinfo("Incoherent input values",
                                    "The minimum number of points in wavelength range is 500.")
                self.wl_n_points_entry.configure(bg="#DF0027", fg="#FFFFFF")
        except:
            messagebox.showinfo("Incoherent input values",
                                "The number of points of wavelength range does not make sense.")
            self.wl_n_points_entry.configure(bg="#DF0027", fg="#FFFFFF")
            error += 1
        try:
            self.fwhm = float(self.fwhm_entry.get())
            self.fwhm_entry.configure(fg="#263A90", bg="#FFFFFF")
        except:
            messagebox.showinfo("Incoherent input values",
                                "The value of FWHM does not make sense.")
            self.fwhm_entry.configure(bg ="#DF0027", fg="#FFFFFF")
            error += 1
        self.output_file_name = self.output_entry.get()
        if len(self.output_file_name) == 0:
            self.output_file_name = "void_name"
        self.title_chart = self.title_entry.get()
        return error

    def makeSpectrumMD(self):
        self.pyplot_bt.configure(state=NORMAL)
        self.output_file_names=self.output_file_name
        error = self.getSimpleValues()
        if error < 1:
            self.spectrumUnited()
        else:
            messagebox.showinfo("Error in user-fed values",
                                "Please correct the marked values.")

    def makeSpectrum(self):
        self.pyplot_bt.configure(state=NORMAL)
        error = self.getSimpleValues()
        self.total_oscillators = []
        self.output_file_names=[]
        num = 1
        if error < 1:
            for spectrum_divided in self.filenames:
                self.total_oscillators = Get_Osc([spectrum_divided]).take_osc()
                self.spectrum = Gaussian_Convolution(self.total_oscillators, self.fwhm)
                self.plot_limits = self.spectrum.make_spectrum(self.wl_rang[0], self.wl_rang[1], self.wl_n_points)
                self.spectrum.write_spectrum(self.target_dir + "/" + self.output_file_name+"_"+str(num))
                self.output_file_names.append(self.output_file_name+"_"+str(num))
                num+=1
            self.save_adv_bt.configure(state=NORMAL)
            self.save_simp_bt.configure(state=NORMAL)
        else:
            messagebox.showinfo("Error in user-fed values",
                                "Please correct the marked values.")

    def spectrumUnited(self):
        self.total_oscillators = Get_Osc(self.filenames).take_osc()
        self.spectrum = Gaussian_Convolution(self.total_oscillators, self.fwhm)
        self.plot_limits = self.spectrum.make_spectrum(self.wl_rang[0], self.wl_rang[1], self.wl_n_points)
        self.spectrum.write_spectrum(self.target_dir + "/" + self.output_file_name)
        self.save_adv_bt.configure(state=NORMAL)
        self.save_simp_bt.configure(state=NORMAL)


    def adv_file(self):
        pass


    def simple_file(self):
        pass


    def pyplot(self):
        if self.choice_file_type == 2:
            x = Print_Spectrum(
                self.target_dir, [self.output_file_name], self.wl_rang[0],
                self.wl_rang[1], self.title_chart, int(self.entry_res.get()),
                self.osc_color, self.curve_color, "0", self.filenames, self.plottypes.get()
            )
        else:
            self.curve_color = []
            self.osc_color = []
            for i in range(0, len(self.filenames), 1):
                self.curve_color.append(self.entry_color_curve_list[i].get())
                self.osc_color.append(self.entry_color_drop_list[i].get())
            x = Print_Spectrum(
                self.target_dir, self.output_file_names, self.wl_rang[0],
                self.wl_rang[1], self.title_chart, int( self.entry_res.get()),
                self.osc_color, self.curve_color, "0", self.filenames,  self.plottypes.get()
            )

        x.print_matplotlib()

        self.pyplot_bt.configure(state=DISABLED)

    def restart(self):
        self.save_adv_bt.configure(state=DISABLED)
        self.save_simp_bt.configure(state=DISABLED)
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
        self.wl_rang_start_entry.configure(fg="#263A90", bg="#FFFFFF")
        self.wl_rang_end_entry.configure(fg="#263A90", bg="#FFFFFF")
        self.wl_n_points_entry.configure(fg="#263A90", bg="#FFFFFF")
        self.fwhm_entry.configure(fg="#263A90", bg="#FFFFFF")
        self.note.tab(self.note2_struct, state="disabled")
        self.note.tab(self.note3_struct, state="disabled")
        self.note.tab(self.note4_struct, state="disabled")
        self.note.tab(self.note5_struct, state="disabled")
        self.note.tab(self.note6_struct, state="disabled")

    def leave(self):
        self.toplevel.quit()
        self.toplevel.destroy()

    def show_version(self):
        text_to_show = "The UV-VIs Sp3trum P4tronum APP is in version {}, released in {}." .format(
            __version__, __date__
        )
        messagebox.showinfo(
            "UV-Vis Sp3ctrum P4tronum", text_to_show
        )

    def open_manual(self):
        operational_system = sys.platform
        if operational_system == 'win32':
            os.system("start .\manual.pdf")
        if operational_system == "darwin":
            os.system("open manual.pdf")
        if operational_system == "":
            os.system("gnome-open manual.pdf")

    def tutorial(self):
        webbrowser.open(
            "https://askubuntu.com/questions/15354/how-to-open-file-with-default-application-from-command-line"
        )

    def enable_file_bt(self):
        self.run_call_bt.configure(state=NORMAL)

class MDfilenames(Frame):

    def __init__(self, toplevel):
        self.toplevel = toplevel
        self.window = Toplevel(self.toplevel)
        self.continue_loop = True
        self.filenames = []
        self.window.geometry("450x280")
        self.window.configure(background="#FFFFFF")
        self.window.wm_title("Multiple Files from MD")
        self.text_container=Frame(self.window, background="#FFFFFF")
        self.text1= Label(
            self.text_container, text="For MD frame analysis, it is necessary that all files ",
            font="Helvetica 14", fg="#263A90", background="#FFFFFF"
        ).pack(side="top")
        self.text2 = Label(
            self.text_container, text="have names with the following names pattern:", font="Helvetica 14",
            fg="#263A90", background="#FFFFFF"
        ).pack(side="top")
        self.text3 = Label(
            self.text_container, text="initialName_FRAME_finalName.log", font="Helvetica 14 bold",
            fg="#263A90", background="#FFFFFF"
        ).pack(side="top", pady=5)
        self.text_container.pack()
        self.name_pattern_box = Frame(self.window, borderwidth=2, relief=RIDGE, background="#FFFFFF")
        self.name_values = Label(self.name_pattern_box, text="Range of Uncorrelated Frames", font="Helvetica",
                                 fg="#DF0027", bg="#FFFFFF").pack()
        self.name_pattern_box_2 = Frame(self.name_pattern_box, background="#FFFFFF")
        self.name_title2_1 = Label(
            self.name_pattern_box_2, text="Inital:", font="Helvetica", fg="#DF0027", bg="#FFFFFF"
        ).pack(side = "left", fill=BOTH, padx = 5, pady = 5)
        self.step_initial = Entry(
            self.name_pattern_box_2, fg="#263A90", width=7, borderwidth=2, relief=RIDGE, background="#FFFFFF"
        )
        self.step_initial.pack(side="left", anchor=NE, padx=5, pady=5)
        self.name_title2_2 = Label(
            self.name_pattern_box_2, text="Step:", font="Helvetica", fg="#DF0027", bg="#FFFFFF"
        ).pack(side = "left", fill=BOTH, padx = 5, pady = 5)
        self.step_step = Entry(
            self.name_pattern_box_2, fg="#263A90", width=5, borderwidth=2, relief=RIDGE, background="#FFFFFF"
        )
        self.step_step.pack(side="left", anchor=NE, padx=5, pady=5)
        self.name_title2_3 = Label(
            self.name_pattern_box_2, text="Final:", font="Helvetica", fg="#DF0027", bg="#FFFFFF"
        ).pack(side = "left", fill=BOTH, padx = 5, pady = 5)
        self.step_final = Entry(
            self.name_pattern_box_2, fg="#263A90", width=7, borderwidth=2, relief=RIDGE, background="#FFFFFF"
        )
        self.step_final.pack(side="left", anchor=NE, padx=5, pady=5)
        self.name_pattern_box_2.pack()

        self.name_pattern_box_1 = Frame(self.name_pattern_box, background="#FFFFFF")
        self.name_title1 = Label(
            self.name_pattern_box_1, text="Inital Name Pattern:", font="Helvetica", fg="#DF0027", bg="#FFFFFF"
        ).pack(side = "left", fill=BOTH, padx = 5, pady = 5)
        self.name_initial = Entry(
            self.name_pattern_box_1, fg="#263A90", width=24, borderwidth=2, relief=RIDGE, background="#FFFFFF"
        )
        self.name_initial.pack(side = "left", anchor=NE, padx = 5, pady = 5)
        self.name_pattern_box_1.pack()
        self.name_pattern_box_4 = Frame(self.name_pattern_box, background="#FFFFFF")
        self.name_title3 = Label(
            self.name_pattern_box_4, text="Final Name Pattern:", font="Helvetica", fg="#DF0027", bg="#FFFFFF"
        ).pack(side = "left", fill=BOTH, padx = 5, pady = 5)
        self.name_final = Entry(
            self.name_pattern_box_4, fg="#263A90", width=24, borderwidth=2, relief=RIDGE, background="#FFFFFF"
        )
        self.name_final.pack(side="left", anchor=NE, padx=5, pady=5)
        self.name_pattern_box_4.pack()
        self.name_pattern_box.pack()
        self.step_pattern_box = Frame(self.window, background="#FFFFFF")

        self.step_pattern_box.pack(pady=5)

        self.bt_container = Frame(self.window, background="#FFFFFF")

        self.folder_bt = Button(
            self.bt_container, text="Directory files", background="#FFFFFF", font="Helvetica",
            command=self.openDirectory,
            highlightbackground="#FFFFFF", pady=2
        )
        self.folder_bt.grid(row =0, column =0)

        self.submit_bt = Button(
            self.bt_container, text="Submit Files", background="#FFFFFF", font="Helvetica",
            command=self.submit_md,
            highlightbackground="#FFFFFF", pady=2
        )
        self.submit_bt.configure(state=DISABLED)
        self.submit_bt.grid(row =0, column =1)
        self.bt_container.pack()

    def openDirectory(self):
        self.dir = filedialog.askdirectory()
        self.submit_bt.configure(state=NORMAL)

    def submit_md(self):
        error = 0
        try:
            range_init = int(self.step_initial.get())
            self.step_initial.configure(bg="#FFFFFF", fg="#000000")
        except:
            messagebox.showinfo("Incoherent input values",
                                "The starting number of frames range must be integer.")
            self.step_initial.configure(bg="#DF0027", fg="#FFFFFF")
            error += 1
        try:
            range_end =  int(self.step_final.get())
            self.step_final.configure(bg="#FFFFFF", fg="#000000")
        except:
            messagebox.showinfo("Incoherent input values",
                                "The final number of frames range must be integer.")
            self.step_final.configure(bg="#DF0027", fg="#FFFFFF")
            error += 1
        try:
            range_step = int(self.step_step.get())
            self.step_step.configure(bg="#FFFFFF", fg="#000000")
        except:
            messagebox.showinfo("Incoherent input values",
                                "The increment number of the frame range must be integer.")
            self.step_step.configure(bg="#DF0027", fg="#FFFFFF")
            error += 1
        name_init = str(self.name_initial.get()).strip()
        name_end = str(self.name_final.get()).strip()
        not_find = 0
        for step in range(range_init, range_end+1, range_step):
            if len(name_end) > 0:
                filename = name_init+"_"+str(step)+"_"+name_end
                try:
                    test = open(self.dir+"/"+filename+".log")
                    self.filenames.append(self.dir+"/"+filename+".log")
                except:
                    try:
                        test = open(self.dir + "/" + filename + ".out")
                        self.filenames.append(self.dir + "/" + filename + ".out")
                    except:
                        not_find+=1
                        print(self.dir + "/" + filename + ".out")
            else:
                filename = name_init + "_" + str(step)
                try:
                    test = open(self.dir+"/"+filename+".log")
                    self.filenames.append(self.dir + "/" + filename + ".log")
                except:
                    try:
                        test = open(self.dir + "/" + filename + ".out")
                        self.filenames.append(self.dir + "/" + filename + ".out")
                    except:
                        not_find+=1
                        print(self.dir + "/" + filename + ".log")
        if not_find > 0:
            resp = messagebox.askyesno(
                "Incoherent input values", str(not_find)+ " files were not found, do you want to continue? If not, check the file names.")
            if resp == False:
                pass
            else:
                self.window.destroy()
        else:
            self.window.destroy()

    def returnFileNames(self):
        return self.filenames

class Second_Window(Frame):

    def __init__(self, toplevel, dir):
        self.dir = dir
        self.toplevel = toplevel

    def tell_about_us(self):
        t = Toplevel(self.toplevel)
        t.configure(width="600",  background="#FFFFFF")
        t.wm_title("UV-Vis Sp3ctrum P4tronum - About Us")
        logo1 = PhotoImage(file=self.dir+'/icons/sp3ctrum.gif')
        logo2 = PhotoImage(file=self.dir+'/icons/leedmol.gif')
        foto1 = PhotoImage(file=self.dir+"/icons/foto1.gif")
        foto2 = PhotoImage(file=self.dir+"/icons/foto2.gif")
        logo_container = Frame(t)
        lg1 = Label(logo_container, image=logo1, background="#FFFFFF")
        lg1.pack(padx=35, pady=60)
        lg2 = Label(logo_container, image=logo2, background="#FFFFFF")
        lg2.pack(padx=35, pady=40)
        logo_container.pack(side="left")
        text_container = Frame(t)
        l1 = Label(text_container,
                   text="This program was a collaboration of:", background="#FFFFFF", font="Helvetica 20 bold",
                                 fg="#020041")
        l1_1 = Label(
            text_container,
            text="Thiago Oliveira Lopes, \nDaniel Francsico Scalabrini Machado,\nHeibbe C. B. de Oliveira\nand the entire LEEDMOL team.\n\n\n",
            background="#FFFFFF", fg="#DF0027", font="Helvetica 16"
        )
        l1.pack(side="top", padx=40)
        l1_1.pack(side="top", padx=40)
        l3 = Label(text_container, text="Powered by: ", background="#FFFFFF", font="Helvetica 20 bold",
                                 fg="#020041")
        l3_1 = Label(
            text_container,
            text="LEEDMOL Research Group\n(Lab. de Estrutura Eletrônica e Dinâmica Molecular)\nInstitute of Chemistry at Universidade de Brasília.\n\n\n",
            font="Helvetica 16", background="#FFFFFF", fg="#DF0027"
        )
        l3.pack(side="top", padx=40)
        l3_1.pack(side="top", padx=40)
        l4 = Label(
            text_container,text="Adress:", background="#FFFFFF", font="Helvetica 20 bold", fg="#020041"
        )
        l4_1 = Label(
            text_container,
            text="BT-75/3 and BT-79/5\nInstituto de Química\nCampus Universitário Darcy Ribeiro\nUniversidade de Brasília.",
            background="#FFFFFF", font="Helvetica 16", fg="#DF0027"
        )
        l4.pack(side="top", padx=40)
        l4_1.pack(side="top", padx=40)
        text_container.pack(side="left")
        photo_container = Frame(t)
        p1 = Label(photo_container,image=foto1, background="#FFFFFF")
        p1.pack(padx=35, pady=20)
        p2 =Label(photo_container,image=foto2,background="#FFFFFF")
        p2.pack(padx=35, pady=20)
        photo_container.pack(side="left")
        Button(t, text = "LEEDMOL Facebook Page", font = "Helvetica", command = self.facebook_buttom)
