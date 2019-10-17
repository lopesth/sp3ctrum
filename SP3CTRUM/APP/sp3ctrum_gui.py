# -*- coding: utf-8 -*-
__author__ = ["Sandro Brito", "Mateus Barbosa", "Daniel Machado", "Thiago Lopes", "Heibbe Oliveira"]
__credits__ = ["LEEDMOL Research group", "Institute of Chemistry at Universidade de Brasilia", "Institute of Chemistry at Universidade Federal de Goiás"]
__date__ = "Oct 16 of 2019"
__version__ = "1.0.1"

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import Button
from PIL import ImageTk, Image
import sys, os, webbrowser
from SP3CTRUM.APP.gaussian_conv import Gaussian_Convolution
from SP3CTRUM.APP.get_osc import Get_Osc
from SP3CTRUM.APP.print_spectrum import Print_Spectrum
from SP3CTRUM.APP.plotTransitions import PlotTransitions
from SP3CTRUM.APP.advancedSave import saveAdvancedSimple

stdColorCurve = ["#E01E23", "#573280", "#945055", "#005CB8", "#29000A"]

class Application(Frame):

    def __init__(self, toplevel):
        Frame.__init__(self, toplevel)

        if sys.platform == "win32":
            self.src = os.path.realpath(__file__).replace("sp3ctrum_gui.py", "")
        else:
            self.src = os.path.realpath(__file__).replace("sp3ctrum_gui.py", "")

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
        self.guiTab6()
        self.guiButtons()
        self.guiLogos()
        self.exp_abs_lines = []
        self.exp_wl_lines = []

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
            },
        })
        self.style.theme_use("leedmol")

    def noteStructures(self):

        ''' Defines all interface structures '''

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

        self.note6_struct = Frame(self.note, background="#FFFFFF")
        self.note6_struct.pack()

        self.note.add(self.note1_struct, text="Files")
        self.note.add(self.note2_struct, text="Spectrum Parameters")
        self.note.add(self.note3_struct, text="Plot Details")
        self.note.add(self.note4_struct, text="Versus Experimental Values")
        self.note.add(self.note6_struct, text="Advanced Options")

        self.note.tab(self.note2_struct, state="disabled")
        self.note.tab(self.note3_struct, state="disabled")
        self.note.tab(self.note4_struct, state="disabled")
        self.note.tab(self.note6_struct, state="disabled")

    def setMenu(self):

        '''
          Method that defines the top bar of the interface.
          The options that are contained in this bar are:
              - File
               --> Open
               --> clear
               --> exit
              - UV-vis Sp3ctrum P4tronum
                --> version
                --> about us
             - Help
                --> manual
                --> tutorial video
        '''

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

    def guiButtons(self):

        '''
           This method defines  *** Files ***
           This method defines the attributes of the Uv-vis home page.
           Allows the user to choose:
               - Calculate Spectrum;
               - Save the Data;
               - Plot Spectrum;
        '''

        self.run_but_container = Frame(self.toplevel, bg="#8EF0F7")

        #choice option Calculate Spectrum
        self.make_spec_bt = Button(
                                   self.run_but_container,
                                   text = "Calculate Spectrum",
                                   font = "Helvetica",
                                   command = self.make_spectrum,
                                   highlightbackground = "#8EF0F7",
                                   pady = 2,
                                   relief = FLAT,
                                   borderwidth = 0
                                  )

        self.make_spec_bt.configure(state=DISABLED)
        self.make_spec_bt.grid(row = 0, column = 0, padx=5)

        # choice option Save the Data
        self.save_adv_bt = Button(
                                  self.run_but_container,
                                  text = "Save the Data",
                                  font = "Helvetica",
                                  command = self.adv_file,
                                  highlightbackground = "#8EF0F7",
                                  pady = 2,
                                  relief = FLAT
                                 )

        self.save_adv_bt.configure(state=DISABLED)
        self.save_adv_bt.grid(row = 0, column = 1, padx=5)

        # choice option Plot Spectrum
        self.pyplot_bt = Button(
                                self.run_but_container,
                                text = "Plot Spectrum",
                                font = "Helvetica",
                                command = self.pyplot,
                                highlightbackground = "#8EF0F7",
                                pady = 2,
                                relief = FLAT
                               )
        self.pyplot_bt.configure(state=DISABLED)
        self.pyplot_bt.grid(row = 0, column = 4, padx=5)

        self.run_but_container.pack()

    def guiTab1(self):

        '''
           This method defines  *** Files ***
           This method defines the attributes of the Uv-vis home page.
           Allows the user to choose:
               - Output Type File;
                  --> Gaussian G09 and G16
               - Type of Anlysis;
                  --> Independent files
                  --> Multiple files
                  --> Multiple files MD
               - Selected Files;
        '''

        self.choice_file_type = IntVar()
        self.choice_log_type = IntVar()
        self.choice_file_type.set(0)
        self.choice_log_type.set(0)

        # structure of the home page.
        self.choice_log_type = Label(
                                     self.note1_struct,
                                     text = "Output Type Files:",
                                     font = "Helvetica 14 bold",
                                     fg = "#263A90",
                                     background = "#FFFFFF"
                                    ).pack(anchor=NW, pady=5, padx=20)

        # chooses the Gaussian(G09 and G16) attribute
        self.rb1_choice_log_type = Radiobutton(
                                               self.note1_struct,
                                               text = "Gaussian (G09 and G16)",
                                               variable = self.choice_log_type,
                                               value = 0,
                                               background = "#FFFFFF"
                                              )
        self.rb1_choice_log_type.pack(anchor=NW, padx=20)
        self.rb1_choice_log_type.select()

        self.choice_files_type = Label(
                                        self.note1_struct,
                                        text = "Choose the type of analysis (with one file or with multiple file overlay):",
                                        font = "Helvetica 14 bold",
                                        fg = "#263A90",
                                        background = "#FFFFFF"
                                      ).pack(anchor = NW, pady = 5, padx = 20)

        self.open_files_BT = Frame(self.note1_struct, background="#FFFFFF")

        # choice option Independent Files
        self.rb1_choice_file_type = Radiobutton(
                                                 self.open_files_BT,
                                                 text = "Independent Files",
                                                 variable = self.choice_file_type,
                                                 value = 0,
                                                 command = self.enable_file_bt,
                                                 background = "#FFFFFF",
                                                 fg = "#000000",
                                               )
        self.rb1_choice_file_type.pack(side="left")

        # choice option multiple Files
        self.rb2_choice_file_type = Radiobutton(
                                                self.open_files_BT,
                                                text = "Multiple Files",
                                                variable = self.choice_file_type,
                                                value = 1,
                                                command = self.enable_file_bt,
                                                background = "#FFFFFF"
                                               )
        self.rb2_choice_file_type.pack(side="left")

        # choice option Multiple files with a logical MD pattern
        self.rb3_choice_file_type = Radiobutton(
                                                 self.open_files_BT,
                                                 text = "Multiple Files with a Logical MD Pattern",
                                                 variable = self.choice_file_type,
                                                 value = 2,
                                                 command = self.enable_file_bt,
                                                 background = "#FFFFFF"
                                               )
        self.rb3_choice_file_type.pack(side="left")

        # choice option Open Files
        self.run_call_bt = Button(
                                   self.open_files_BT,
                                   text = "Open files",
                                   font = "Helvetica",
                                   state = DISABLED,
                                   command = self.select_files,
                                   background = "#FFFFFF",
                                   fg = "#000000",
                                   width = 8
                                 )
        self.run_call_bt.pack(side="left")

        self.open_files_BT.pack(anchor=NW, pady=5, padx=20)

        self.file_container = Frame(self.note1_struct, background="#FFFFFF")

        # choice file with selected file
        self.file_titles = Label(
                                 self.file_container,
                                 text="Selected Files:",
                                 font="Helvetica 25 bold",
                                 fg="#263A90",
                                 background="#FFFFFF"
                                )
        self.file_titles.pack(anchor=NW, pady=5, padx=20)

        self.file_name_box = Listbox(
                                      self.file_container,
                                      relief=RIDGE,
                                      borderwidth=3,
                                      width=82,
                                      height=11,
                                      background="#8EF0F7",
                                      fg="#263A90"
                                    )
        self.file_name_box.pack(anchor=NW, pady=5, padx=20)
        self.file_container.pack()

    def guiTab2(self):

        '''
           This method defines  *** Parameter Spectrum ***
           This is method create box for insert wavelength range in nm and full width at half maximum.
           In this method the user can define:
              - Start wavelength range;
              - End wavelength range;
              - Number of points between the wavelength;
              - Full width at Half Maximum FWHM in (cm-1)
        '''

        self.box_container_interval_2 = Frame(self.note2_struct, background="#FFFFFF")
        self.box_container_interval_2.pack()

        self.box_container_out = Frame(
                                        self.note2_struct,
                                        relief = FLAT,
                                        borderwidth = 1,
                                        background="#FFFFFF"
                                      )

        self.box_container_in1 = Frame(self.box_container_out, background="#FFFFFF")

        self.box_container_line1 = Frame(
                                          self.box_container_in1,
                                          relief = FLAT,
                                          borderwidth = 1,
                                          background = "#FFFFFF"
                                        )
        self.box_container_line1_1 = Frame(self.box_container_line1, background="#FFFFFF")

        self.box_container_wl = Frame(
                                       self.box_container_line1_1,
                                       relief = FLAT,
                                       borderwidth = 1,
                                       background = "#FFFFFF"
                                     )

        # box that contains input information about wavelength and Number of points
        self.wl_rang_name = Label(
                                   self.box_container_line1_1,
                                   text="Wavelength Range (nm):",
                                   font="Helvetica 16 bold",
                                   fg="#DF0027",
                                   bg="#FFFFFF"
                                 ).pack(fill=X)
        self.box_container_line1_1.pack()
        self.box_container_line1_2 = Frame(self.box_container_line1, background="#FFFFFF")

        # box start
        self.wl_rang_name_s = Label(
                                     self.box_container_line1_2,
                                     text = "Start",
                                     font = "Helvetica 14",
                                     fg = "#DF0027",
                                     background = "#FFFFFF"
                                   ).pack(side="left")

        # box that receives the initial input value
        self.wl_rang_start_entry = Entry(
                                          self.box_container_line1_2,
                                          width = 4,
                                          fg = "#263A90",
                                          borderwidth = 2,
                                          relief =
                                          RIDGE, background="#FFFFFF"
                                        )
        self.wl_rang_start_entry.insert(END, '150')
        self.wl_rang_start_entry.pack(side="left")

        # box end
        self.wl_rang_name_e = Label(
                                     self.box_container_line1_2,
                                     text = "End",
                                     font = "Helvetica 14",
                                     fg = "#DF0027",
                                     background = "#FFFFFF"
                                   ).pack(side="left")

        # box that receives final input value
        self.wl_rang_end_entry = Entry(
                                        self.box_container_line1_2,
                                        width = 4,
                                        fg = "#263A90",
                                        borderwidth = 2,
                                        relief = RIDGE,
                                        background = "#FFFFFF"
                                      )
        self.wl_rang_end_entry.insert(END, '350')
        self.wl_rang_end_entry.pack(side="left")

        self.box_container_line1_2.pack()
        self.box_container_line1_2 = Frame(self.box_container_line1, background="#FFFFFF")

        # box that receives total number of points.
        self.wl_n_points_name = Label(
                                       self.box_container_line1_2,
                                       text = "Number of points",
                                       fg = "#DF0027",
                                       font = "Helvetica 14",
                                       background = "#FFFFFF"
                                     ).pack()

        self.wl_n_points_entry = Entry(
                                        self.box_container_line1_2,
                                        width = 5,
                                        fg = "#263A90",
                                        borderwidth = 2,
                                        relief = RIDGE,
                                        background = "#FFFFFF"
                                      )
        self.wl_n_points_entry.insert(END, '10000')
        self.wl_n_points_entry.pack()

        self.box_container_line1_2.pack()
        self.box_container_line1.pack(side="left")
        self.box_container_line2 = Frame(self.box_container_in1, relief=FLAT, borderwidth=1, background="#FFFFFF")
        self.box_container_div = Frame(self.box_container_in1, relief=FLAT, borderwidth=1, background="#FFFFFF")

        # empty box
        self.wl_n_points_name = Label(
                                       self.box_container_div,
                                       text = "                                ",
                                       font = "Helvetica 14",
                                       background = "#FFFFFF"
                                     ).pack()
        self.box_container_div.pack(side="left")

        self.box_container_fwhm = Frame(
                                         self.box_container_line2,
                                         relief = FLAT,
                                         borderwidth = 1,
                                         background = "#FFFFFF"
                                       )
        # information for box Full width at Half Maximum FWHM (cm-1)
        self.fwhm_name = Label(
                                self.box_container_fwhm,
                                text = 'Full Width at Half Maximum',
                                font = "Helvetica 16 bold",
                                fg = "#DF0027",
                                background = "#FFFFFF"
                              ).pack(fill=X)

        self.fwhm_name2 = Label(
                                 self.box_container_fwhm,
                                 text = u'FWHM (cm\u207B\u00B9):',
                                 font = "Helvetica 16 bold",
                                 fg = "#DF0027",
                                 background = "#FFFFFF"
                               ).pack(fill=X)

        # enter the width value with half height.
        self.fwhm_entry = Entry(
                                 self.box_container_fwhm,
                                 width = 7,
                                 fg = "#263A90",
                                 borderwidth = 2,
                                 relief = RIDGE,
                                 background = "#FFFFFF"
                               )
        self.fwhm_entry.insert(END, '3226.22')
        self.fwhm_entry.pack()

        self.box_container_fwhm.pack(side="left")
        self.box_container_line2.pack(side="left")
        self.box_container_in1.grid(row=0)
        self.box_container_out.pack()

    def guiTab3(self):

        '''
           This method defines  *** Plot Details ***
           This is method create box for insert:
               - Title of the plots;
               - Colors of Curve;
               - Color of Oscillators;
               - Resolution of Plot (dpi);
               - Plot Types
                  --> Independent plots
                  --> Overlay Plots
        '''


        self.box_container_plot = Frame(
                                         self.note3_struct,
                                         relief = FLAT,
                                         borderwidth = 0,
                                         background = "#FFFFFF"
                                       )
        # choice of graph title
        self.name_title = Label(
                                 self.box_container_plot,
                                 text = "Title of the Plots (Optional):",
                                 font = "Helvetica 14 bold",
                                 fg = "#DF0027",
                                 background = "#FFFFFF"
                               ).pack(side="left")

        self.title_entry = Entry(
                                  self.box_container_plot,
                                  width = 60,
                                  fg = "#263A90",
                                  borderwidth = 2,
                                  relief = RIDGE,
                                  background = "#FFFFFF"
                                )
        self.title_entry.pack(side="left")
        self.box_container_plot.pack(pady=5)

        # colors of each curves
        self.box_container_curve_colors = Frame(
                                                 self.note3_struct,
                                                 relief = FLAT,
                                                 borderwidth = 0,
                                                 background = "#FFFFFF"
                                               )

        self.title_color_curve = Label(
                                        self.box_container_curve_colors,
                                        text = "Color of Curve\n(CSS Hex Style, for each .log file):",
                                        font = "Helvetica",
                                        fg = "#DF0027",
                                        background = "#FFFFFF"
                                      ).pack(side="left")

        self.entry_color_curve_list = []  # list of collors curves
        for i in range(0, 5):
            entry_color_curve1 = Entry(
                                        self.box_container_curve_colors,
                                        width=8,
                                        fg="#263A90",
                                        borderwidth=2,
                                        relief=RIDGE,
                                        background="#FFFFFF"
                                     )
            entry_color_curve1.insert(END, stdColorCurve[i])
            entry_color_curve1.pack(side="left", padx=5)
            self.entry_color_curve_list.append(entry_color_curve1)

        self.box_container_curve_colors.pack(side="top", pady=5, anchor=W, padx=10)

        self.checkbutton_hide_osc_box = Frame(
                                         self.note3_struct,
                                         relief = FLAT,
                                         borderwidth = 0,
                                         background = "#FFFFFF"
                                        )
        self.hideOscValue = IntVar(0)

        self.checkbuttonHideOsc = Label(
                                           self.checkbutton_hide_osc_box,
                                           text = "Hide the Theoretical Oscillators?",
                                           fg = "#DF0027",
                                           background = "#FFFFFF"
                                          ).pack(side="left")

        self.checkbutton_hide_osc2 = Radiobutton(
                                             self.checkbutton_hide_osc_box,
                                             text = "Yes",
                                             variable = self.hideOscValue,
                                             value = 1,
                                             background = "#FFFFFF",
                                             command = self.hideOsc
                                            )
        self.checkbutton_hide_osc1 = Radiobutton(
                                             self.checkbutton_hide_osc_box,
                                             text = "No",
                                             variable = self.hideOscValue,
                                             value = 0,
                                             background = "#FFFFFF",
                                             command = self.notHideOsc
                                            )

        self.checkbutton_hide_osc1.pack(side="left")
        self.checkbutton_hide_osc2.pack(side="left")
        self.checkbutton_hide_osc_box.pack(side="top", pady=5, anchor=W, padx=10)

        # colors of each Oscillators
        self.box_container_drop_colors = Frame(
                                                self.note3_struct,
                                                relief = FLAT,
                                                borderwidth = 0,
                                                background = "#FFFFFF"
                                              )
        self.title_color_drop = Label(
                                       self.box_container_drop_colors,
                                       text = "Color of Oscillators\n(CSS Hex Style, for each .log file):",
                                       font = "Helvetica",
                                       fg = "#DF0027",
                                       background = "#FFFFFF"
                                     ).pack(side="left")

        self.entry_color_drop_list = []  # List of colors Oscillators
        for i in range(0, 5):
            entry_color_drop = Entry(
                                      self.box_container_drop_colors,
                                      width = 8,
                                      fg = "#263A90",
                                      borderwidth = 2,
                                      relief = RIDGE,
                                      background = "#FFFFFF"
                                    )
            entry_color_drop.insert(END, stdColorCurve[i])
            entry_color_drop.pack(side="left", padx=5)
            self.entry_color_drop_list.append(entry_color_drop)

        self.box_container_drop_colors.pack(side="top", pady=10, anchor=W, padx=10)

        self.clean_color_box(1) # clear box

        self.box_container_res = Frame(self.note3_struct, relief=FLAT, borderwidth=0, background="#FFFFFF")

        self.title_res = Label(
                                 self.box_container_res,
                                 text = "Resolution of Plot (dpi):",
                                 font = "Helvetica",
                                 fg = "#DF0027",
                                 background = "#FFFFFF"
                              ).pack(side="left")

        self.entry_res = Entry(
                                 self.box_container_res,
                                 width = 4,
                                 fg = "#263A90",
                                 borderwidth = 2,
                                 relief = RIDGE,
                                 background = "#FFFFFF"
                              )
        self.entry_res.insert(END, '300')
        self.entry_res.pack()
        self.box_container_res.pack(side="top", pady=5, anchor=W, padx=10)

        self.checkbuttonplot_box = Frame(
                                         self.note3_struct,
                                         relief = FLAT,
                                         borderwidth = 0,
                                         background = "#FFFFFF"
                                        )
        self.plottypes = IntVar(0)

        self.checkbuttonplot_name = Label(
                                           self.checkbuttonplot_box,
                                           text = "Plot Types:",
                                           fg = "#DF0027",
                                           background = "#FFFFFF"
                                          ).pack(side="left")

        self.checkbuttonplot1 = Radiobutton(
                                             self.checkbuttonplot_box,
                                             text = "Independent Plots",
                                             variable = self.plottypes,
                                             value = 0,
                                             background = "#FFFFFF"
                                            )

        self.checkbuttonplot2 = Radiobutton(
                                             self.checkbuttonplot_box,
                                             text = "Overlay Plots",
                                             variable = self.plottypes,
                                             value = 1,
                                             background = "#FFFFFF"
                                            )
        self.checkbuttonplot1.pack(side="left")
        self.checkbuttonplot2.pack(side="left")
        self.checkbuttonplot_box.pack(side="top", pady=5, anchor=W, padx=10)

    def hideOsc(self):
        print(self.hideOscValue.get(), "hide")
        for i in range(0, 5):
            self.entry_color_drop_list[i].delete(0, END)
            self.entry_color_drop_list[i].configure(state="disabled", borderwidth=2)
 
    def notHideOsc(self):
        print(self.hideOscValue.get(), "not hide")
        for i in range(0, 5):
            self.entry_color_drop_list[i].delete(0, END)
        for i in range(0, len(self.filenames)):
            self.entry_color_drop_list[i].configure(state="normal", borderwidth=2)
            self.entry_color_drop_list[i].insert(END, stdColorCurve[i])

    def clean_color_box(self, firstItem):
        
        '''
           This method removes the information that was entered by the user in relation to the colors of the curves,
           as well as the colors of the oscillators.
           The default color is that of the first box.
        '''

        for i in range(firstItem, 5):
            self.entry_color_drop_list[i].delete(0, END)
            self.entry_color_curve_list[i].delete(0, END)
            self.entry_color_curve_list[i].configure(state="disabled", borderwidth=2)
            self.entry_color_drop_list[i].configure(state="disabled", borderwidth=2)

    def guiTab4(self):

        '''
           This method describes the values of experimental plots.
        '''

        self.option_experimental = IntVar(0)
        self.experimental_type = IntVar(0)
        self.experimental_points_wl = []
        self.experimental_points_abs = []

        self.box_option_experimental = Frame(
                                              self.note4_struct,
                                              relief = FLAT,
                                              borderwidth = 0,
                                              bg = "#FFFFFF"
                                            )

        self.text_option_experimental = Label(
                                               self.box_option_experimental,
                                               text = "Plot with experimental data?",
                                               bg = "#FFFFFF"
                                             ).pack(side = "left", padx = 10)

        self.option_experimental_NObt = Radiobutton(
                                                     self.box_option_experimental,
                                                     text = "No",
                                                     variable = self.option_experimental,
                                                     value = 0,
                                                     background = "#FFFFFF",
                                                     command = self.no_experimental_data
                                                   )
        self.option_experimental_NObt.pack(side="left", padx=10)

        self.option_experimental_Ybt = Radiobutton(
                                                    self.box_option_experimental,
                                                    text = "Yes",
                                                    variable = self.option_experimental,
                                                    value = 1,
                                                    background = "#FFFFFF",
                                                    command = self.experimental_data_type
                                                  )
        self.option_experimental_Ybt.pack(side="left", padx=10)
        self.box_option_experimental.pack(side="top", pady=5, anchor=W)

        self.box_experimental_color = Frame(
                                             self.note4_struct,
                                             relief = FLAT,
                                             borderwidth = 0,
                                             bg = "#FFFFFF"
                                           )

        self.text_experimental_color = Label(
                                              self.box_experimental_color,
                                              text = "Color of Plot of Experimental:",
                                              bg = "#FFFFFF"
                                            )
        self.text_experimental_color.pack(side="left", padx=10)

        self.entry_color_exp = Entry(
                                      self.box_experimental_color,
                                      width = 8,
                                      fg = "#263A90",
                                      borderwidth = 2,
                                      relief = RIDGE,
                                      background = "#FFFFFF"
                                    )
        self.entry_color_exp.pack(side="left", padx=5)
        self.box_experimental_color.pack(side="top", pady=5, anchor=W)

        self.box_experimental_types = Frame(
                                             self.note4_struct,
                                             relief = FLAT,
                                             borderwidth = 0,
                                             bg = "#FFFFFF"
                                           )

        self.text_experimental_types = Label(
                                              self.box_experimental_types,
                                              text = "Plot of Experimental Values:",
                                              bg = "#FFFFFF"
                                            )
        self.text_experimental_types.pack(side="left", padx=10)

        self.experimental_type_curve_bt = Radiobutton(
                                                       self.box_experimental_types,
                                                       text = "Curve",
                                                       variable = self.experimental_type,
                                                       value = 0,
                                                       background = "#FFFFFF",
                                                       command = self.experimental_data_curve
                                                     )
        self.experimental_type_curve_bt.pack(side="left", padx=10)

        self.experimental_type_ref_bt = Radiobutton(
                                                     self.box_experimental_types,
                                                     text = "Reference",
                                                     variable = self.experimental_type,
                                                     value = 1,
                                                     background = "#FFFFFF",
                                                     command = self.experimental_data_ref
                                                   )
        self.experimental_type_ref_bt.pack(side="left", padx=10)
        self.box_experimental_types.pack(side="top", pady=10,  anchor=W)

        self.box_experimental_plot = Frame(
                                            self.note4_struct,
                                            relief = FLAT,
                                            borderwidth = 0,
                                            bg = "#FFFFFF"
                                          )

        self.text_experimental_plot = Label(
                                             self.box_experimental_plot,
                                             text = "File with experimental data:",
                                             bg = "#FFFFFF"
                                            )
        self.text_experimental_plot.pack(side="left", padx=10)

        self.buttom_experimental_plot = Button(
                                                self.box_experimental_plot,
                                                text = "Open Files",
                                                command = self.open_experimental_data_file
                                              )
        self.buttom_experimental_plot.pack(side="left", padx=10)

        self.boxList_experimental_plot = Listbox(
                                                  self.box_experimental_plot,
                                                  relief = RIDGE,
                                                  borderwidth = 3,
                                                  width = 45,
                                                  height = 1,
                                                  background = "#FFFFFF",
                                                  fg = "#263A90"
                                                )
        self.boxList_experimental_plot.pack(side="left", padx=10)
        self.box_experimental_plot.pack(side="top", pady=10,  anchor=W)

        self.box_experimental_ref = Frame(
                                           self.note4_struct,
                                           relief = FLAT,
                                           borderwidth = 0,
                                           bg = "#FFFFFF"
                                         )

        self.experimental_ref_text = Label(
                                            self.box_experimental_ref,
                                            text = "Points of the\nexperimental values:",
                                            bg = "#FFFFFF"
                                          )
        self.experimental_ref_text.pack(side="left", padx=10)

        self.box_experimental_ref_wl = Frame(
                                              self.box_experimental_ref,
                                              relief = FLAT,
                                              borderwidth = 0,
                                              bg = "#FFFFFF")

        self.experimental_ref_wl_name = Label(
                                               self.box_experimental_ref_wl,
                                               text = "Wavelength\n(nm):",
                                               bg = "#FFFFFF"
                                             )
        self.experimental_ref_wl_name.pack(side="top", padx=10)
        for i in range(0, 4):
            entry_wl_exp = Entry(
                                  self.box_experimental_ref_wl,
                                  width = 8,
                                  fg = "#263A90",
                                  borderwidth = 2,
                                  relief = RIDGE,
                                  background = "#FFFFFF"
                                )
            entry_wl_exp.pack(side="top", padx=10)
            self.experimental_points_wl.append(entry_wl_exp)

        self.box_experimental_ref_wl.pack(side="left", padx=10)
        self.box_experimental_ref_abs = Frame(self.box_experimental_ref,relief=FLAT, borderwidth=0, bg = "#FFFFFF")
        self.experimental_ref_abs_name = Label(
                                                self.box_experimental_ref_abs,
                                                text = "Molar Absortivity\n(L/mol.cm):",
                                                bg = "#FFFFFF"
                                              )
        self.experimental_ref_abs_name.pack(side="top", padx=10)
        for i in range(0, 4):
            entry_abs_exp = Entry(
                                   self.box_experimental_ref_abs,
                                   width = 8,
                                   fg = "#263A90",
                                   borderwidth = 2,
                                   relief = RIDGE,
                                   background = "#FFFFFF"
                                 )
            entry_abs_exp.pack(side="top", padx=10)
            self.experimental_points_abs.append(entry_abs_exp)

        self.box_experimental_ref_abs.pack(side="left", padx=10)
        self.box_experimental_ref.pack(side="top", pady=10,  anchor=W)
        self.no_experimental_data()

    def no_experimental_data(self):
        self.experimental_type_curve_bt.config(state=DISABLED)
        self.experimental_type_ref_bt.config(state=DISABLED)
        self.text_experimental_color.config(fg="#BFBFBF")
        self.text_experimental_types.config(fg="#BFBFBF")
        self.entry_color_exp.config(state="disable")
        self.no_experimental_data_curve()
        self.no_experimental_data_ref()

    def experimental_data_type(self):

        '''
           configures box information in relation to the experimental data.
        '''

        self.experimental_type_curve_bt.config(state=NORMAL)
        self.experimental_type_ref_bt.config(state=NORMAL)
        self.entry_color_exp.config(state=NORMAL)
        self.entry_color_exp.delete(0, 'end')
        self.entry_color_exp.insert(END, '#957532')
        self.text_experimental_types.config(fg="#000000")
        self.text_experimental_color.config(fg="#000000")

    def experimental_data_curve(self):
        self.no_experimental_data_ref()
        self.text_experimental_plot.config(fg="#000000")
        self.buttom_experimental_plot.config(state=NORMAL)
        self.boxList_experimental_plot.config(state=NORMAL)

    def no_experimental_data_curve(self):
        self.text_experimental_plot.config(fg="#BFBFBF")
        self.buttom_experimental_plot.config(state=DISABLED)
        self.boxList_experimental_plot.delete(0, END)
        self.boxList_experimental_plot.config(state=DISABLED)

    def experimental_data_ref(self):
        self.no_experimental_data_curve()
        self.experimental_ref_text.config(fg="#000000")
        self.experimental_ref_wl_name.config(fg="#000000")
        self.experimental_ref_abs_name.config(fg="#000000")
        for i in range(0, 4, 1):
            self.experimental_points_wl[i].config(state=NORMAL)
            self.experimental_points_abs[i].config(state=NORMAL)

    def no_experimental_data_ref(self):
        self.experimental_ref_text.config(fg="#BFBFBF")
        self.experimental_ref_wl_name.config(fg="#BFBFBF")
        self.experimental_ref_abs_name.config(fg="#BFBFBF")
        for i in range(0, 4, 1):
            self.experimental_points_wl[i].delete(0, 'end')
            self.experimental_points_abs[i].delete(0, 'end')
            self.experimental_points_wl[i].config(state=DISABLED)
            self.experimental_points_abs[i].config(state=DISABLED)

    #############################################
    #                                           #
    #     There is no structure 5.              #
    #                                           #
    #     There is no guiTab5.                  #
    #                                           #
    #############################################

    def guiTab6(self):

        '''
           This method describes the possible output names of the files and intensity methods.
           This method describes the possible output names of the files and intensity methods.
           In this option the user can can choose:
              - Names of the output data.
              - Methods of spectrum intensity.
        '''

        self.choice_intensity = IntVar()
        self.choice_intensity.set(1)

        self.box_container_adv = Frame(
                                        self.note6_struct,
                                        relief = FLAT,
                                        borderwidth = 0,
                                        background = "#FFFFFF"
                                      )

        self.name_output = Label(
                                  self.box_container_adv,
                                  text = "Base of Output Names:",
                                  font = "Helvetica 14 bold",
                                  fg = "#DF0027",
                                  background = "#FFFFFF"
                                ).pack(side="left")

        self.output_entry = Entry(
                                   self.box_container_adv,
                                   width = 60,
                                   borderwidth = 2,
                                   relief = RIDGE,
                                   background = "#FFFFFF"
                                 )
        self.output_entry.pack(side="left")
        self.box_container_adv.pack(side="top", pady=5, anchor=W)

        self.box_intensity_Choice = Frame(
                                           self.note6_struct,
                                           relief = FLAT,
                                           borderwidth = 0,
                                           background = "#FFFFFF"
                                         )
        self.intensity_Choice = Label(
                                       self.box_intensity_Choice,
                                       text = "Spectrum intensity method:",
                                       font = "Helvetica 14 bold",
                                       fg = "#DF0027",
                                       background = "#FFFFFF"
                                     ).pack(side="left")

        self.rb1_choice_intensity = Radiobutton(
                                                 self.box_intensity_Choice,
                                                 text = "Relative Intensity",
                                                 variable = self.choice_intensity,
                                                 value = 0,
                                                 background = "#FFFFFF",
                                                 command = self.expButt
                                               )
        self.rb1_choice_intensity.pack(side="left")

        self.rb2_choice_intensity = Radiobutton(
                                                 self.box_intensity_Choice,
                                                 text = "Estimated Absorbance",
                                                 variable = self.choice_intensity,
                                                 value = 1,
                                                 background = "#FFFFFF",
                                                 command = self.expButt
                                               )
        self.rb2_choice_intensity.pack(side="left")
        self.box_intensity_Choice.pack(side="top", pady=5, anchor=W)

    def guiLogos(self):
        self.all_logos_container = Frame(self.toplevel, background="#8EF0F7", borderwidth=0)
        self.logo1 = PhotoImage(file=self.src + "icons/sp3ctrum_b.gif")
        self.logo2 = PhotoImage(file=self.src + "icons/leedmol_b.gif")
        self.logos_title_container = Frame(
                                            self.all_logos_container,
                                            background = "#8EF0F7",
                                            borderwidth = 5,
                                            width = 300
                                          )
        self.lg1_title = Label(
                                self.logos_title_container,
                                text = "UV-Vis",
                                background = "#8EF0F7",
                                font="Helvetica 23 bold italic",
                                fg = "#62338C"
                              ).grid(row=0, column=0)

        self.lg1_title = Label(
                                self.logos_title_container,
                                text = "Sp3ctrum P4tronus",
                                background = "#8EF0F7",
                                font = "Helvetica 23 bold italic",
                                fg="#62338C"
                              ).grid(row=1, column=0)

        self.lg2_title = Label(
                                 self.logos_title_container,
                                 text = "Powered by:",
                                 background = "#8EF0F7",
                                 font = "Helvetica 16 italic",
                                 fg = "#62338C"
                              ).grid(row=2, column=0)

        self.lg2_title = Label(
                                self.logos_title_container,
                                text = "LEEDMOL",
                                background = "#8EF0F7",
                                font = "Helvetica 20 bold italic",
                                fg = "#62338C"
                              ).grid(row=3, column=0)

        self.logos_title_container.grid(row=0, column=0)

        self.lg1 = Label(
                          self.all_logos_container,
                          image = self.logo1,
                          background = "#8EF0F7",
                          height = 150,
                          width = 250
                        ).grid(row=0, column=1)

        self.lg2 = Label(
                          self.all_logos_container,
                          image = self.logo2,
                          background = "#8EF0F7",
                          height = 150,
                          width = 250
                        ).grid(row=0, column=2)
        self.all_logos_container.pack()

    def expButt(self):

        if self.choice_intensity.get() == 1:
            self.note.tab(self.note4_struct, state="normal")
        else:
            self.note.tab(self.note4_struct, state="disable")

    def select_files(self):

        self.save_adv_bt.configure(state="disable")
        self.pyplot_bt.configure(state="disable")
        self.file_name_box.delete(0, END)
        self.operationMode = self.choice_file_type.get()

        # mode Independent files
        if self.choice_file_type.get() == 0:
            self.filenames = []
            self.filenames_ = filedialog.askopenfilenames(
                                                          initialdir="/",
                                                          filetypes=[("Gaussian LOG files","*.log"), ("Gaussian OUTPUTS files","*.out")]
                                                         )
            if len(self.filenames_) > 4:
                messagebox.showinfo(
                                    "Maximum number of files", "Let's use only the first 5 files of the input."
                                   )

            for filename in self.filenames_[0:5]:
                self.filenames.append(filename)

            self.clean_color_box(len(self.filenames))

            # define cor do plots
            for i in range(0, len(self.filenames)):
                self.entry_color_curve_list[i].configure(state="normal", borderwidth=2)
                self.entry_color_drop_list[i].configure(state="normal", borderwidth=2)
                self.entry_color_curve_list[i].delete(0, END)
                self.entry_color_drop_list[i].delete(0, END)
                self.entry_color_curve_list[i].insert(END, stdColorCurve[i])
                self.entry_color_drop_list[i].insert(END, stdColorCurve[i]) # define a cor do oscilador

        # mode multiple files
        elif self.choice_file_type.get() == 1:
            self.filenames = []

            self.filenames_m = filedialog.askopenfilenames(
                                                           initialdir="/",
                                                           filetypes=[("Gaussian LOG files","*.log"), ("Gaussian OUTPUTS files","*.out")]
                                                          )

            for filename in self.filenames_m:
                self.filenames.append(filename)

            self.clean_color_box(1)
            self.entry_color_curve_list[1].insert(END, stdColorCurve[0])
            self.entry_color_drop_list[1].insert(END, stdColorCurve[0])


        elif self.choice_file_type.get() == 2:
            self.md = MDfilenames(self)
            self.toplevel.wait_window(self.md.window)
            self.filenames = self.md.returnFileNames()
            self.clean_color_box(1)

            self.entry_color_curve_list[1].insert(END, stdColorCurve[0])
            self.entry_color_drop_list[1].insert(END, stdColorCurve[0])

        for filename in self.filenames:
            fn_div = filename.split('/')
            if len(fn_div) > 3:
                self.file_name_box.insert(
                                      END, ".../"+fn_div[-3]+"/"+fn_div[-2]+"/"+fn_div[-1]
                                     )
            else:
                if len(fn_div) > 2:
                    self.file_name_box.insert(
                                      END, ".../"+fn_div[-2]+"/"+fn_div[-1]
                                     )
                else:
                    operational_system = sys.platform
                    if operational_system == 'win32':
                        self.file_name_box.insert(
                                      END, fn_div[-2]+"/"+fn_div[-1]
                                     )
                    else:
                        self.file_name_box.insert(
                                      END, "/"+fn_div[-2]+"/"+fn_div[-1]
                                     )
        self.target_dir = "/".join(self.filenames[-1].split("/")[0:-1])
        self.note.tab(self.note2_struct, state="normal")
        self.note.tab(self.note3_struct, state="normal")

        # representa diferenças entre Independent files e multiple files
        if self.choice_file_type.get() == 0:
            self.note.tab(self.note4_struct, state="normal")

        else:
            if self.choice_file_type.get() == 1:
                self.note.tab(self.note4_struct, state="disable")
            if self.choice_file_type.get() == 2:
                self.note.tab(self.note4_struct, state="disable")
            self.checkbuttonplot1.configure(state = DISABLED)
            self.checkbuttonplot2.configure(state = DISABLED)

        self.note.tab(self.note6_struct, state="normal")
        self.make_spec_bt.configure(state=NORMAL)
        self.output_entry.delete(0, END)
        operational_system = sys.platform
        filenameTemp = self.filenames[-1].split("/")[-2].lower()
        if operational_system == 'win32':
            filenameTemp = filenameTemp.split(":")[0]
        self.output_entry.insert(0, filenameTemp)

    def make_spectrum(self):

        if self.choice_file_type.get() == 0:
            # It is the method for Calculate Gaussian convolution with
            # Independent Files.
            self.makeSpectrum()
        else:
            # It is the method for Calculate Gaussian convolution with
            # Multiple Files and Multiple files with a logical MD pattern.
            self.makeSpectrumMD()

    def getSimpleValues(self):

        '''
           This method handles the possible errors entered by users within the
           Spectrum Parameters and returns a Boolean variable..
        '''

        error = False
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
                                 "Incoherent input values",
                                 "One of the wavelength range values does not make sense."
                               )
            error = True

        try:
            end_a = float(self.wl_rang_end_entry.get())
            self.wl_rang_end_entry.configure(fg="#263A90", bg="#FFFFFF")
        except:
            self.wl_rang_end_entry.configure(bg="#DF0027", fg="#FFFFFF")
            messagebox.showinfo("Incoherent input values",
                                "One of the wavelength range values does not make sense.")
            error = True

        self.wl_rang = [start_a, end_a]

        try:
            self.wl_n_points = int(self.wl_n_points_entry.get())
            self.wl_n_points_entry.configure(fg="#263A90", bg="#FFFFFF")

            if self.wl_n_points < 500:

                error = True
                messagebox.showinfo("Incoherent input values",
                                    "The minimum number of points in wavelength range is 500.")
                self.wl_n_points_entry.configure(bg="#DF0027", fg="#FFFFFF")
        except:
            messagebox.showinfo("Incoherent input values",
                                "The number of points of wavelength range does not make sense.")
            self.wl_n_points_entry.configure(bg="#DF0027", fg="#FFFFFF")
            error = True

        try:
            self.fwhm = float(self.fwhm_entry.get())
            self.fwhm_entry.configure(fg="#263A90", bg="#FFFFFF")
        except:
            messagebox.showinfo("Incoherent input values",
                                "The value of FWHM does not make sense.")
            self.fwhm_entry.configure(bg ="#DF0027", fg="#FFFFFF")
            error = True

        self.output_file_name = self.output_entry.get()
        if len(self.output_file_name) == 0:
            self.output_file_name = "void_name"
        self.title_chart = self.title_entry.get()

        return error

    def makeSpectrumMD(self):

        ''' Compute the convolution considering multiple files. '''

        self.pyplot_bt.configure(state=NORMAL)
        self.output_file_names = [self.output_entry.get()]
        error = self.getSimpleValues()          # self.getSimpleValues() retorna valores de erros

        if error == False:
            self.spectrumUnited()
        else:
            messagebox.showinfo("Error in user-fed values",
                                "Please correct the marked values.")

    def makeSpectrum(self):

        ''' Compute the convolution considering Independent files. '''

        self.pyplot_bt.configure(state=NORMAL)
        error = self.getSimpleValues()         # self.getSimpleValues() retorna valores de erros
        self.total_oscillators = []
        self.output_file_names = []

        num = 1
        if error == False:
            for spectrum_divided in self.filenames:
                self.total_oscillators = Get_Osc([spectrum_divided]).take_osc(float(self.wl_rang[0]), self.wl_rang[1])
                self.spectrum = Gaussian_Convolution(self.total_oscillators, self.fwhm)
                self.plot_limits = self.spectrum.make_spectrum(self.wl_rang[0], self.wl_rang[1], self.wl_n_points)
                self.spectrum.write_spectrum(self.target_dir + "/" + self.output_file_name + "_" + str(num))
                self.output_file_names.append(self.output_file_name + "_" + str(num))
                num += 1
            self.save_adv_bt.configure(state=NORMAL)
        else:
            messagebox.showinfo("Error in user-fed values",
                                "Please correct the marked values.")

    def spectrumUnited(self):

        ''' This method is called for from the spectrum Make method. '''

        self.total_oscillators = Get_Osc(self.filenames).take_osc(float(self.wl_rang[0]), self.wl_rang[1])
        self.spectrum = Gaussian_Convolution(self.total_oscillators, self.fwhm)
        self.plot_limits = self.spectrum.make_spectrum(self.wl_rang[0], self.wl_rang[1], self.wl_n_points)
        self.spectrum.write_spectrum(self.target_dir + "/" + self.output_file_name)
        self.save_adv_bt.configure(state=DISABLEs)

    def adv_file(self):
        print(self.target_dir)

        try:
            os.remove(self.target_dir + "/" + self.output_file_name + "_advancedData.dat")
        except:
            pass

        if self.choice_file_type.get() == 0:
            for i in range(0, len(self.filenames)):
                print(self.target_dir + "/" + self.output_file_names[i] + "_spectrum.dat")
                toSave = saveAdvancedSimple(self.filenames[i], self.target_dir + "/" + self.output_file_names[i] + "_spectrum.dat")
        else:
            for i in range(0, len(self.filenames)):
                if i == len(self.filenames) - 1:
                    toSave = saveAdvancedSimple(self.filenames[i], self.target_dir + "/" + self.output_file_name + "_spectrum.dat", False)
                else:
                    toSave = saveAdvancedSimple(self.filenames[i], self.target_dir + "/" + self.output_file_name + "_spectrum.dat", False, False)

        concordPlural = (False if len(self.filenames) == 1 or self.choice_file_type.get() != 0 else True)
        titSave = ("Files Saved" if concordPlural else "File Saved")
        messagSave = ("All files have" if concordPlural else "The file has")
        messagebox.showinfo(titSave, messagSave + " already been saved in the working directory")

    def get_exp_data(self):

        if self.option_experimental.get() == 0:
            self.exp_abs_lines = []
            self.exp_wl_lines = []
        else:
            if self.experimental_type.get() == 0:
                try:
                    with open(self.experimental_data_file, encoding="utf8", errors='ignore') as myFile:
                        for line in myFile:
                            if len(line.split()) > 0:
                                wlString, absorbanceString = line.split()
                                wl = float(wlString)
                                absorbance = float(absorbanceString)
                                if wl >= float(self.wl_rang_start_entry.get()):
                                    if wl <= float(self.wl_rang_end_entry.get()):
                                        self.exp_wl_lines.append(wl)
                                        self.exp_abs_lines.append(absorbance)
                except:
                    pass
            else:
                self.exp_wl_lines = []
                self.exp_abs_lines = []
                for i in range(0, 4):
                    x = self.experimental_points_wl[i].get()
                    if len(x) > 0:
                        self.exp_wl_lines.append(float(x))
                    y = self.experimental_points_abs[i].get()
                    if len(y) > 0:
                        self.exp_abs_lines.append(float(y))

    def open_experimental_data_file(self):

        ''' A method that extracts experimental data values. '''

        messagebox.showinfo(
                              "Experimental curve file",
                              "The File that contains the experimental spectrum must be a two-column .dat text file.\n"
                              "The first column should be the wavelength (nm), while the second should be the Molar Absorptivity (L/mol.cm)."
                           )
        self.experimental_data_file = filedialog.askopenfilename(
                                                                  initialdir = "/",
                                                                  filetypes = [("File Data","*.dat")]
                                                                )
        self.boxList_experimental_plot.insert(0, self.experimental_data_file)

    def pyplot(self):

        ''' This method plots the oscillators and the spectrum. '''

        self.get_exp_data()
        self.curve_color = []
        self.osc_color = []

        if self.choice_file_type.get() == 0:
            for i in range(0, len(self.filenames)):
                self.curve_color.append(self.entry_color_curve_list[i].get())
                self.osc_color.append(self.entry_color_drop_list[i].get())
        else:
            self.curve_color.append(self.entry_color_curve_list[0].get())
            self.osc_color.append(self.entry_color_drop_list[0].get())
        plot = Print_Spectrum(
                              self.target_dir,              # directory path which will be added to the curve.
                              self.output_file_names,       # list with names of output files.
                              self.wl_rang[0],              # Initial wavelength.
                              self.wl_rang[1],              # end wavelength.
                              self.title_chart,             # if you want to enter a name for the curve.
                              int(self.entry_res.get()),    # if you want to enter a new resolution for the curve.
                              self.osc_color,               # Oscillator Colors.
                              self.curve_color,             # Curve colors.
                              self.filenames,               # List with INPUT files
                              self.plottypes.get(),         # Values 0 - Independent Plots or 1 - Overlay Plots
                              self.exp_abs_lines,           # List with absolute experimental data values.
                              self.exp_wl_lines,            # List with experimental data values of wavelength.
                              self.entry_color_exp.get(),   # Color of experimental input values.
                              self.choice_intensity.get()   # Sets the type of intensity method. 0 - Relative Intensity and 1 - Estimated Absorbance
                            )
        plot.print_matplotlib()
        self.pyplot_bt.configure(state=DISABLED)

    def restart(self):

        ''' Method that restarts the initial conditions '''

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
        self.note.tab(self.note6_struct, state="disabled")

    def leave(self):
        self.toplevel.quit()
        self.toplevel.destroy()

    def show_version(self):
        text_to_show = "The UV-VIs Sp3trum P4tronum APP is in version {}, released in {}.".format(
            __version__, __date__
        )

        messagebox.showinfo(
                            "UV-Vis Sp3ctrum P4tronum",
                            text_to_show
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

        '''
           This method is called inside the  *** Help *** tab.
          Passing information about using the software in Tutorial Video .
        '''

        webbrowser.open(
                        "https://askubuntu.com/questions/15354/how-to-open-file-with-default-application-from-command-line"
                       )

    def enable_file_bt(self):

        '''
           Method that calls and rum the user-defined options. These options can be:
           - Independent files
           - Multiple Files
           - Multiple Files with a logical MD Pattern
        '''

        self.run_call_bt.configure(state=NORMAL)

class MDfilenames(Frame):

    '''
       This class defines a new dialog box that will be used if
       MD Multiple files mode is selected.
    '''

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
                           self.text_container,
                           text = "For MD frame analysis, it is necessary that all files ",
                           font = "Helvetica 14",
                           fg = "#263A90",
                           background = "#FFFFFF"
                         ).pack(side="top")

        self.text2 = Label(
                             self.text_container,
                             text = "have names with the following names pattern:",
                             font = "Helvetica 14",
                             fg = "#263A90",
                             background = "#FFFFFF"
                          ).pack(side="top")

        self.text3 = Label(
                            self.text_container,
                            text = "initialName_FRAME_finalName.log",
                            font = "Helvetica 14 bold",
                            fg = "#263A90",
                            background = "#FFFFFF"
                          ).pack(side="top", pady=5)
        self.text_container.pack()

        self.name_pattern_box = Frame(
                                       self.window,
                                       borderwidth = 2,
                                       relief = RIDGE,
                                       background = "#FFFFFF"
                                     )
        self.name_values = Label(
                                  self.name_pattern_box,
                                  text = "Range of Uncorrelated Frames",
                                  font = "Helvetica",
                                  fg = "#DF0027",
                                  bg = "#FFFFFF"
                                ).pack()

        self.name_pattern_box_2 = Frame(self.name_pattern_box, background="#FFFFFF")

        self.name_title2_1 = Label(
                                    self.name_pattern_box_2,
                                    text = "Inital:",
                                    font = "Helvetica",
                                    fg = "#DF0027",
                                    bg = "#FFFFFF"
                                  ).pack(side = "left", fill=BOTH, padx = 5, pady = 5)

        self.step_initial = Entry(
                                   self.name_pattern_box_2,
                                   fg = "#263A90",
                                   width = 7,
                                   borderwidth = 2,
                                   relief = RIDGE,
                                   background = "#FFFFFF"
                                 )
        self.step_initial.pack(side="left", anchor=NE, padx=5, pady=5)

        self.name_title2_2 = Label(
                                    self.name_pattern_box_2,
                                    text = "Step:",
                                    font = "Helvetica",
                                    fg = "#DF0027",
                                    bg = "#FFFFFF"
                                  ).pack(side = "left", fill=BOTH, padx = 5, pady = 5)

        self.step_step = Entry(
                                self.name_pattern_box_2,
                                fg = "#263A90",
                                width = 5,
                                borderwidth = 2,
                                relief = RIDGE,
                                background = "#FFFFFF"
                              )
        self.step_step.pack(side="left", anchor=NE, padx=5, pady=5)

        self.name_title2_3 = Label(
                                   self.name_pattern_box_2,
                                   text = "Final:",
                                   font = "Helvetica",
                                   fg = "#DF0027",
                                   bg = "#FFFFFF"
                                  ).pack(side = "left", fill=BOTH, padx = 5, pady = 5)

        self.step_final = Entry(
                                 self.name_pattern_box_2,
                                 fg = "#263A90",
                                 width = 7,
                                 borderwidth = 2,
                                 relief = RIDGE,
                                 background = "#FFFFFF"
                                )
        self.step_final.pack(side="left", anchor=NE, padx=5, pady=5)
        self.name_pattern_box_2.pack()

        self.name_pattern_box_1 = Frame(self.name_pattern_box, background="#FFFFFF")
        self.name_title1 = Label(
                                  self.name_pattern_box_1,
                                  text = "Inital Name Pattern:",
                                  font = "Helvetica",
                                  fg = "#DF0027",
                                  bg = "#FFFFFF"
                                ).pack(side = "left", fill=BOTH, padx = 5, pady = 5)

        self.name_initial = Entry(
                                   self.name_pattern_box_1,
                                   fg = "#263A90",
                                   width = 24,
                                   borderwidth = 2,
                                   relief = RIDGE,
                                   background = "#FFFFFF"
                                  )
        self.name_initial.pack(side = "left", anchor=NE, padx = 5, pady = 5)

        self.name_pattern_box_1.pack()
        self.name_pattern_box_4 = Frame(self.name_pattern_box, background="#FFFFFF")
        self.name_title3 = Label(
                                  self.name_pattern_box_4,
                                  text = "Final Name Pattern:",
                                  font = "Helvetica",
                                  fg = "#DF0027",
                                  bg = "#FFFFFF"
                                ).pack(side = "left", fill=BOTH, padx = 5, pady = 5)

        self.name_final = Entry(
                                 self.name_pattern_box_4,
                                 fg = "#263A90",
                                 width = 24,
                                 borderwidth = 2,
                                 relief = RIDGE,
                                 background = "#FFFFFF"
                               )
        self.name_final.pack(side="left", anchor=NE, padx=5, pady=5)
        self.name_pattern_box_4.pack()
        self.name_pattern_box.pack()

        self.step_pattern_box = Frame(self.window, background="#FFFFFF")
        self.step_pattern_box.pack(pady=5)

        self.bt_container = Frame(self.window, background="#FFFFFF")

        self.folder_bt = Button(
                                 self.bt_container,
                                 text = "Directory files",
                                 background = "#FFFFFF",
                                 font = "Helvetica",
                                 command = self.openDirectory,
                                 highlightbackground = "#FFFFFF",
                                 pady = 2
                               )
        self.folder_bt.grid(row =0, column =0)

        self.submit_bt = Button(
                                 self.bt_container,
                                 text = "Submit Files",
                                 background = "#FFFFFF",
                                 font = "Helvetica",
                                 command = self.submit_md,
                                 highlightbackground = "#FFFFFF",
                                 pady = 2
                               )
        self.submit_bt.configure(state = DISABLED)
        self.submit_bt.grid(row = 0, column = 1)
        self.bt_container.pack()

    def openDirectory(self):
        self.dir = filedialog.askdirectory()
        self.submit_bt.configure(state=NORMAL)

    def submit_md(self):

        ''' This method treats the possible errors in the module Multiple Files MD '''

        try:
            range_init = int(self.step_initial.get())
            self.step_initial.configure(bg="#FFFFFF", fg="#000000")
        except:
            messagebox.showinfo(
                                "Incoherent input values",
                                "The starting number of frames range must be integer."
                               )
            self.step_initial.configure(bg="#DF0027", fg="#FFFFFF")

        try:
            range_step = int(self.step_step.get())
            self.step_step.configure(bg="#FFFFFF", fg="#000000")
        except:
            messagebox.showinfo(
                                "Incoherent input values",
                                "The increment number of the frame range must be integer."
                               )
            self.step_step.configure(bg="#DF0027", fg="#FFFFFF")

        try:
            range_end =  int(self.step_final.get())
            self.step_final.configure(bg="#FFFFFF", fg="#000000")
        except:
            messagebox.showinfo(
                                "Incoherent input values",
                                "The final number of frames range must be integer."
                               )
            self.step_final.configure(bg="#DF0027", fg="#FFFFFF")

        name_init = str(self.name_initial.get()).strip()
        name_end = str(self.name_final.get()).strip()
        not_find = False

        for step in range(range_init, range_end+1, range_step):
            if len(name_end) > 0:
                filename = name_init + "_" + str(step) + "_" + name_end

                try:
                    test = open(self.dir + "/" + filename + ".log", encoding="utf8", errors='ignore')
                    self.filenames.append(self.dir + "/" + filename + ".log")
                except:
                    try:
                        test = open(self.dir + "/" + filename + ".out", encoding="utf8", errors='ignore')
                        self.filenames.append(self.dir + "/" + filename + ".out")
                    except:
                        not_find = True
                        print(self.dir + "/" + filename + ".out")
            else:
                filename = name_init + "_" + str(step)
                try:
                    test = open(self.dir + "/" + filename + ".log", encoding="utf8", errors='ignore')
                    self.filenames.append(self.dir + "/" + filename + ".log")
                except:
                    try:
                        test = open(self.dir + "/" + filename + ".out", encoding="utf8", errors='ignore')
                        self.filenames.append(self.dir + "/" + filename + ".out")
                    except:
                        not_find = True
                        print(self.dir + "/" + filename + ".log")

        if not_find == True:
            resp = messagebox.askyesno(
                                       "Incoherent input values", str(not_find) +
                                       " files were not found, do you want to continue? If not, check the file names."
                                      )
            if resp == False:
                pass
            else:
                self.window.destroy()
        else:
            self.window.destroy()

    def returnFileNames(self):
        return self.filenames

class Second_Window(Frame):

    '''
          This class defines the characteristics of the authors and collaborators
        of the software.
          Since the window is called on the top flap of the program in
        UV-vis Sp3ctrum P4tronum.
    '''

    def __init__(self, toplevel, dir):
        self.dir = dir
        self.toplevel = toplevel

    def tell_about_us(self):
        top = Toplevel(self.toplevel)
        top.configure(width="600",  background="#FFFFFF")
        top.wm_title("UV-Vis Sp3ctrum P4tronum - About Us")

        logo1 = ImageTk.PhotoImage(Image.open(self.dir + '/icons/sp3ctrum.gif'))
        logo2 = ImageTk.PhotoImage(Image.open(self.dir + '/icons/leedmol.gif'))

        logo_container = Frame(top)
        logo_container.configure(background="#FFFFFF")
        lg1 = Label(logo_container, image=logo1, background="#FFFFFF")
        lg1.image = logo1
        lg1.configure(image = logo1)
        lg1.pack(padx=35, pady=60)

        lg2 = Label(logo_container, image=logo2, background="#FFFFFF")
        lg2.image = logo2
        lg2.configure(image = logo2)
        lg2.pack(padx=35, pady=40)
        logo_container.pack(side="left")

        text_container = Frame(top)
        text_container.configure( background="#FFFFFF")
        l1 = Label(
                    text_container,
                    text = "This program was a collaboration of:",
                    background = "#FFFFFF",
                    font = "Helvetica 20 bold",
                    fg = "#020041"
                  )

        author_text = ", \n".join(__author__[0:-1]) + "\n and " + __author__[-1] + "."
        credits_text = "\n".join(__credits__)

        l1_1 = Label(
                      text_container,
                      text = author_text + "\n",
                      background = "#FFFFFF",
                      fg = "#DF0027",
                      font = "Helvetica 16"
                    )
        l1.pack(side="top", padx=40)
        l1_1.pack(side="top", padx=40)

        l3 = Label(
                    text_container,
                    text = "LEEDMOL - Research Group",
                    background = "#FFFFFF",
                    font = "Helvetica 20 bold",
                    fg = "#020041"
                  )

        l3_1 = Label(
                      text_container,
                      text = "Laboratório de Estrutura Eletrônica e Dinâmica Molecular\nInstituto de Química\nCampus Universitário Samabaia\nUniversidade Federal de Goiás.\n\n",
                      font = "Helvetica 16",
                      background = "#FFFFFF",
                      fg = "#DF0027"
                    )
        l3.pack(side="top", padx=40)
        l3_1.pack(side="top", padx=40)

        l4 = Label(
                    text_container,
                    text = "LMSC - Research Group",
                    background = "#FFFFFF",
                    font = "Helvetica 20 bold",
                    fg = "#020041"
                  )

        l4_1 = Label(
                      text_container,
                      text = "Laboratório de Modelagem de Sistemas Complexos\nInstituto de Química\nCampus Universitário Darcy Ribeiro\nUniversidade de Brasília.",
                      background = "#FFFFFF",
                      font = "Helvetica 16",
                      fg = "#DF0027"
                    )
        l4.pack(side="top", padx=40)
        l4_1.pack(side="top", padx=40)
        text_container.pack(side="left")

