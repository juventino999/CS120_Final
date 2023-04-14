#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 10:33:28 2023

@author: juventino1112
"""
import numpy as np
import pandas as pd
import csv
""" Open CSV file and save contents to a list of lists """
def open_csv(filename):
    with open(filename, mode='r') as file:
        return(pd.read_csv(file))
""" Delete a specific variable (column) """
def delete_var(file, var):
    pass

""" Delete observation (row) """
def delete_obs(file, obs):
    pass

""" Split file by observation. Take a variable to look under and a list of 
observations, and move all rows containing the observations in the list to a new file. 
Make sure to avoid crashing the whole program if the obs in list aren't found. """
def split_obs(file, target_filename, target_var, obs):
    pass

""" Split file by variable. Take a list of variables and move those variables 
into a separate CSV file, along with optional other variables  to copy (not move) too.  """
def split_var(file, target_filename, varlist, copylist=[]):
    pass

""" Append a list of observations from csv to an existing file, target_filename"""
def append(file, target_filename, obs):
    pass

""" Delete duplicate observations. Select whether complete duplicates should be
removed, or if observations with duplicated list of var values should be removed. 
Make sure to keep the original. """
def delete_duplicates(file, perfect_duplicates, var=[], obs=[]):
    pass

file = open_csv("1.csv")
file['']

