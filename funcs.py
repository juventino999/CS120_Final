"""
Created on Fri Apr 14 10:33:28 2023

@author: juventino1112
"""
#import numpy as np
import pandas as pd
import csv
""" Open CSV file and save contents to a list of lists. First row must be variables. """
def open_csv(filename):
#    with open(filename, mode='r') as file:
    return(pd.read_csv(filename))

""" Delete a list of specific variables (columns) """
def delete_var(file, varlist): # Nick
    try: 
        file = file.drop(varlist, axis = 1)
        return(file)
    except: 
        raise_gui_error("Variables not found")

""" Delete observation (row) by index number list. """
def delete_obs(file, obslist): # Nick
    try: 
        file = file.drop(obslist, axis = 0)
        return(file)
    except: 
        raise_gui_error("Observation not found")    

""" Delete observation (row). Search all obs within given var and drop if they match.
If multi = 0, search thru one variable and delete all instances. If multi = 1, search list
of variables and argument list of obs must match (match by index) """
def delete_obs_by_var(file, obs, var, multi=0): # Nick. Multi needs to be looked over and probably fixed, untested
    if multi == 0:
        obslist = []
        for index, contents in file.iterrows():
            if obs in contents[var]:
                obslist.append(index)
        file = delete_obs(file, obslist)
        return(file)
    if multi == 1: # use re to make set of obs that contain obs in each var. Compare all sets and pass overlap to delete_obs as list
        obslist = {}
        for i in range(len(var)): # for each variable in varlist, as index
            obslist[i] = set() # create set that is {index}obslist
            for index, contents in file.iterrows(): # basically run multi == 0, add each obs to set from above
                if obs in contents[var[i]]:
                    obslist[i] += index
        # find the overlap of all sets, pass that as list to delete_obs()
        

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
    print('error')
    
def save_df_to_csv(df, target_filename):
    pass

if __name__ == '__main__': # does not execute this part if importing from another file
    test = open_csv("gradebook.csv")
    print(test)
    print()
    test = delete_obs_by_var(test, 'nick')
    print(test)
