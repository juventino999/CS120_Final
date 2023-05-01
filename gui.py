#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:29:30 2023

@author: juventino1112

Instructions:
    - import CSV file using the button
    - Type desired observations/variables to manipulate in text box on button of GUI and press "Gather arguments"
    - Click a button to execute a function from funcs.py using the arguments gathered
    - Save the CSV file using the button

"""
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from funcs import Sheet
import funcs
import tkinter.scrolledtext as st
from tkinter import ttk
import pandas as pd


class Window():

    def __init__(self):

        # Set up tkinter
        self.window = Tk()
        self.window.title("CSV Editor")
        self.window.geometry('1000x800')
        
        # Set up window grid
        self.window.rowconfigure(0, weight=5)
        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(0, weight=1) 
        self.window.columnconfigure(1, weight=20)

        # Define what to show on the left (menu)
        frame_menu = Frame(self.window, relief=RAISED, bd=2)
        frame_menu.grid(row=0, column=0, rowspan=1, sticky='WENS')
# buttons
        btn_open = ttk.Button(frame_menu, text="Import CSV", command=self.openfile)
        btn_open.grid(row=0, column=0, sticky="WE", padx=5, pady=5)

        btn_save = Button(frame_menu, text="Save as CSV", command=self.saveasfile)
        btn_save.grid(row=1, column=0, sticky="WE", padx=5, pady=5)

        btn_delete_var = Button(frame_menu, text="Delete variable", command=lambda: self.func_button(self.activeSheet.delete_var))
        btn_delete_var.grid(row=2, column=0, sticky="WE", padx=5, pady=5)

        #btn_delete_obs = Button(frame_menu, text="Delete observation", command=lambda: self.df = self.df.drop(obslist, axis = 0)
        btn_delete_obs = Button(frame_menu, text="Delete observation", command=self.func_obs)
        btn_delete_obs.grid(row=3, column=0, sticky="WE", padx=5, pady=5)
      
        btn_delete_obs_var = Button(frame_menu, text="Del obs matching var", command=lambda: self.func_button(self.activeSheet.delete_obs_by_var))
        btn_delete_obs_var.grid(row=4, column=0, sticky="WE", padx=5, pady=5)
        
        btn_delete_obs_multi = Button(frame_menu, text="Del obs matching multiple vars", command=lambda: self.func_button(self.activeSheet.delete_obs_by_var_multi))
        btn_delete_obs_multi.grid(row=5, column=0, sticky="WE", padx=5, pady=5)
        
        btn_quit = Button(frame_menu, text="Exit", command=self.program_exit)
        btn_quit.grid(row=6, column=0, sticky="WE", padx=5, pady=5)
        
        # Define what to show on the right (the dataframe - top)
        frame_csv = Frame(self.window, bg="SILVER")
        frame_csv.grid(row=0, column=1, rowspan=1, sticky='WENS')

        xscrollbar = ttk.Scrollbar(frame_csv, orient='horizontal')
        xscrollbar.pack(side='bottom', fill='x')

        # Create a vertical scrollbar and attach it to the frame
        yscrollbar = ttk.Scrollbar(frame_csv, orient='vertical')
        yscrollbar.pack(side='right', fill='y')
        # table
        self.table = st.ScrolledText(frame_csv, wrap=NONE, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
        self.table.pack(side='left', fill='both', expand=True)
        
        xscrollbar.configure(command=self.table.xview)

        # Configure the vertical scrollbar to work with the table
        yscrollbar.configure(command=self.table.yview)

        # Define what to show on the right (the input - bottom)
        frame_input = Frame(self.window)
        frame_input.grid(row=1,column=1, sticky='WENS')
        frame_input.columnconfigure(0, weight=1)

        left_boxes = Frame(frame_input)
        left_boxes.grid(row=0, column=0, sticky='NW')

        right_boxes = Frame(frame_input)
        right_boxes.grid(row=0, column=1, sticky='NE', padx=5)

        row_txt = Label(left_boxes, text = "Variables").grid(row = 0,column = 0, sticky='W')
        col_txt = Label(left_boxes, text = "Observations").grid(row = 1,column = 0, sticky='W')
        
        # Submit button
        btn_submit = Button(left_boxes, text="Gather arguments", command=self.gather_args).grid(row=4, column=0, sticky='W')

        # Get user input for row, col and value
        self.var_input = Entry(left_boxes)
        self.var_input.grid(row=0, column=1, sticky='W')

        self.obs_input = Entry(left_boxes)
        self.obs_input.grid(row=1, column=1, sticky='W')

        # Display error/success messages
        self.inputtxt = Label(right_boxes, height=5, width=30, bg="WHITE")
        self.inputtxt.grid(row=0, column=0, pady=5, sticky='E')
        
        # Run the app
        self.window.mainloop()
#clear table, then add dataframe to it
    def refresh(self, Sheet):
        self.table.config(state=NORMAL)
        self.table.delete(1.0, END)
        self.table.insert(END, Sheet)
        self.table.config(state=DISABLED)
#set open a file to self.activeSheet, then run refresh()
    def openfile(self):
        self.activeSheet = Sheet(askopenfilename(filetypes=[("CSV", "*.csv")]))
        self.refresh(self.activeSheet)
#make a new window that asks if the user really wants to quit
    def program_exit(self):
        self.quitWindow = Toplevel(self.window)
        self.quitWindow.geometry("300x100")
        quitLabel = Label(self.quitWindow, text="Are you sure you want to exit?")
        quitLabel.pack()
        btn_exit = Button(self.quitWindow, text="Yes", command=self.window.destroy)
        btn_exit.pack(padx=5, pady=5)
        btn_dont_exit = Button(self.quitWindow, text="No", command=self.quitWindow.destroy)
        btn_dont_exit.pack(padx=5, pady=5)
    def saveasfile(self):
        target_filename = asksaveasfilename(filetypes=[("CSV", "*.csv")])
        Sheet.save_df_to_csv(self.activeSheet, target_filename)
# =============================================================================
# no longer used, using self.func_button() instead
#     def delete_var_button(self):
#         self.activeSheet.delete_var(self.var_args)
#         self.refresh(self.activeSheet)
# =============================================================================
#generic button function: takes a function from Sheet class, runs it with var_args and obs_args, and then refreshes
    def func_button(self, function):
        function(self.var_args, self.obs_args)
        self.refresh(self.activeSheet)
    # take obs and vars as lists. comma with no space as separator
    #to-do: add error processing, spit out an error on inputtxt if the input isnt a var/obs, print "success" if successful
    def gather_args(self): # delete obs by var not working for integer obs
        # Valid input
        self.obs_args = []
        self.var_args = []
        try:
            
            self.var_args = self.var_input.get().split(sep=",")
            self.obs_args = self.obs_input.get().split(sep=",")

        # Invalid input
        except:
            message = "Invalid input\n"
            self.inputtxt.config(text=message)
        print(self.obs_args)
        print(self.var_args)

    def func_obs(self):
        self.activeSheet.delete_obs([], self.obs_args)
        self.refresh(self.activeSheet)        


win = Window()