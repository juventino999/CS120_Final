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

TO-DO:
    - Configure buttons and add backend commands to them
    - on click button, change bottom part to text boxes for that specific function
"""
# can use askstring for var/obs inputs or can make text boxes below
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from funcs import Sheet
import funcs
import tkinter.scrolledtext as st
import pandas as pd
from tkinter import ttk

activeSheet = pd.read_csv("saved_test_long.csv")
class Window():

    def __init__(self):

        # Set up tkinter
        self.window = Tk()
        self.window.title("CSV Editor")
        self.window.geometry('800x800')
        
        # Set up window grid
        self.window.rowconfigure(0, weight=5)
        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(0, weight=1) 
        self.window.columnconfigure(1, weight=20)

        # Define what to show on the left (menu)
        frame_menu = Frame(self.window, relief=RAISED, bd=2)
        frame_menu.grid(row=0, column=0, rowspan=1, sticky='WENS')

        btn_open = ttk.Button(frame_menu, text="Import CSV", command=self.openfile) # use lambda if wanting to pass args
        btn_open.grid(row=0, column=0, sticky="WE", padx=5, pady=5)

        btn_save = Button(frame_menu, text="Save as CSV", command=self.saveasfile)
        btn_save.grid(row=1, column=0, sticky="WE", padx=5, pady=5)

        
        btn_delete_var = Button(frame_menu, text="Delete variable", command=self.delete_var_button)
        btn_delete_var.grid(row=3, column=0, sticky="WE", padx=5, pady=5)
        
        btn_quit = Button(frame_menu, text="Exit", command=self.program_exit)
        btn_quit.grid(row=4, column=0, sticky="WE", padx=5, pady=5)
        
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

        row_txt = Label(left_boxes, text = "Observations").grid(row = 0,column = 0, sticky='W')
        col_txt = Label(left_boxes, text = "Variables").grid(row = 1,column = 0, sticky='W')
        
        # Submit button
        btn_submit = Button(left_boxes, text="Gather arguments", command=self.gather_args).grid(row=4, column=0, sticky='W')

        # Get user input for row, col and value
        self.obs_input = Entry(left_boxes)
        self.obs_input.grid(row=0, column=1, sticky='W')

        self.var_input = Entry(left_boxes)
        self.var_input.grid(row=1, column=1, sticky='W')

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
    def delete_var_button(self):
        self.activeSheet.delete_var(self.var_args)
        self.refresh(self.activeSheet)
        
    # take obs and vars as lists. comma with no space as separator
    #to-do: add error processing, spit out an error on inputtxt if the input isnt a var/obs, print "success" if successful
    def gather_args(self):
        # Valid input
        try:
            self.obs_args = self.obs_input.get().split(sep=",")
            self.var_args = self.var_input.get().split(sep=",")
# =============================================================================
#             if:
#                  self.inputtxt.config(text="Value added successfully.")
#             else:
#                 self.inputtxt.config(text="Data violates the rules of sudoku.")
# =============================================================================
        # Invalid input
        except:
            message = "Invalid input\n"
            self.inputtxt.config(text=message)

        


win = Window()