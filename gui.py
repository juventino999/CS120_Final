#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:29:30 2023

@author: juventino1112

TO-DO:
    - Configure buttons and add backend commands to them
    - Get scroll to work
    - add horizontal scroll bar
    - Decide what to do with the bottom row
"""
import csv
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from funcs import Sheet
import tkinter.scrolledtext as st

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

        btn_open = Button(frame_menu, text="Import CSV")
        btn_open.grid(row=0, column=0, sticky="WE", padx=5, pady=5)

        btn_save = Button(frame_menu, text="Save as CSV")
        btn_save.grid(row=1, column=0, sticky="WE", padx=5, pady=5)

        btn_quit = Button(frame_menu, text="Save CSV")
        btn_quit.grid(row=2, column=0, sticky="WE", padx=5, pady=5)
        
        #btn_quit = Button(frame_menu, text="Delete ID", command=lambda: funcs.delete_var("saved_test_long.csv", "id"))
        btn_quit.grid(row=3, column=0, sticky="WE", padx=5, pady=5)
        
        btn_quit = Button(frame_menu, text="save CSV")
        btn_quit.grid(row=4, column=0, sticky="WE", padx=5, pady=5)
        
    ###
        # Define what to show on the right (the game - top)
        frame_csv = Frame(self.window, bg="SILVER")
        frame_csv.grid(row=0, column=1, rowspan=3, sticky='WENS')

# =============================================================================
#         scroll = Scrollbar(frame_csv)
#         scroll.pack(side = RIGHT, fill = Y)
# =============================================================================

# =============================================================================
#         self.output_txt = Label(frame_csv, bg="SILVER")
#         self.output_txt.place(relx=.5, rely=1, anchor='center')
#         self.refresh(funcs.open_csv("saved_test_long.csv"))
# =============================================================================
        
        self.text_area = st.ScrolledText(frame_csv,
                     width = 30, 
                     height = 8, 
                     font = ("Times New Roman",
                             15))
        self.text_area.grid(row=0, column = 0, pady = 10, padx = 10)

        self.update_display()


        # Define what to show on the right (the input - bottom)
        frame_input = Frame(self.window)
        frame_input.grid(row=1,column=1, sticky='WENS')
        frame_input.columnconfigure(0, weight=1)

        left_boxes = Frame(frame_input)
        left_boxes.grid(row=0, column=0, sticky='NW')

        right_boxes = Frame(frame_input)
        right_boxes.grid(row=0, column=1, sticky='NE', padx=5)

        row_txt = Label(left_boxes, text = "Row").grid(row = 0,column = 0, sticky='W')
        col_txt = Label(left_boxes, text = "Col").grid(row = 1,column = 0, sticky='W')
        val_txt = Label(left_boxes, text = "Value").grid(row = 2,column = 0, sticky='W')
        
        # Submit button
        #btn_submit = Button(left_boxes, text="Submit", command=self.add_value).grid(row=4, column=0, sticky='W')

        # Get user input for row, col and value
        self.row_input = Entry(left_boxes)
        self.row_input.grid(row=0, column=1, sticky='W')

        self.col_input = Entry(left_boxes)
        self.col_input.grid(row=1, column=1, sticky='W')

        self.val_input = Entry(left_boxes)
        self.val_input.grid(row=2, column = 1, sticky='W')
          
        # Display error/success messages
        self.inputtxt = Label(right_boxes, height=5, width=30, bg="WHITE")
        self.inputtxt.grid(row=0, column=0, pady=5, sticky='E')
        
        # Run the app
        self.window.mainloop()
    def refresh(self, df):
        self.output_txt.config(text=print(activeSheet))
    def update_display(self):
        self.text_area.insert(INSERT, str("1") * 100)
win = Window()