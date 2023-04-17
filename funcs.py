"""
Created on Fri Apr 14 10:33:28 2023

@author: juventino1112
"""
#import numpy as np
import pandas as pd
import csv
""" Open CSV file and save contents to a list of lists """
def open_csv(filename):
#    with open(filename, mode='r') as file:
    return(pd.read_csv(filename))

""" Delete a list of specific variables (columns) """
def delete_var(file, varlist): # Nick
    try: 
        file.drop(varlist, axis = 1)
    except: 
        raise_gui_error("Variables not found")

""" Delete observation (row) by index number list. """
def delete_obs(file, obslist): # Nick
    try: 
        file.drop(obslist, axis = 0)
    except: 
        raise_gui_error("Observation not found")    

""" Delete observation (row). Search all obs within given var and drop if they match """
def delete_obs_by_var(file, obs, var):
    obslist = []
    for 
    delete_obs(file, obslist)
    pass

""" Split file by observation. Take a variable to look under and a list of 
observations, and move all rows containing the observations in the list to a new file. 
Make sure to avoid crashing the whole program if the obs in list aren't found. """
def split_obs(file, target_filename, target_var, obs): # Nick
    pass

""" Split file by variable. Take a list of variables and move those variables 
into a separate CSV file, along with optional other variables  to copy (not move) too.  """
def split_var(file, target_filename, varlist, copylist=[]): # Nick
    pass

""" Append a list of observations from csv to an existing file, target_filename"""
def append(file, target_filename, obs): #Zhangir

    pass

""" Delete duplicate observations. Select whether complete duplicates should be
removed, or if observations with duplicated list of var values should be removed. 
Make sure to keep the original. """
def delete_duplicates(file, perfect_duplicates, var=[], obs=[]): #Zhangir
    pass

def sort(file, sortby): #Zhangir
    pass

def raise_gui_error():
    pass

if __name__ == '__main__': # does not execute this part if importing from another file
    test = open_csv("gradebook.csv")