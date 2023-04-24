"""
Created on Fri Apr 14 10:33:28 2023

@author: juventino1112
TO-DO:
    - Finish missing functions
    - Change CSV-based to df-based
"""
#import numpy as np
import pandas as pd
import numpy as np
import csv

""" Change to class structure instead? Would probably be easier, can update with methods instead of having to call functions
#class Sheet(): # change out filename for self and make them all methods"""

class Sheet:
    def __init__(self, filename):
        self.df = pd.read_csv(filename)
    def __repr__(self):
        return(self.to_string())
    def delete_var(self, varlist):
        self.df = self.df.drop(varlist, axis = 1)
    def delete_obs(self, obslist): # Nick
        self.df = self.df.drop(obslist, axis = 0)
    def delete_obs_by_var(self, obs, var): # Nick. 
        obslist = []
        for index, contents in self.df.iterrows():
            if obs in contents[var]:
                obslist.append(index)
        self.df = delete_obs(obslist)
    def delete_obs_by_var_multi(self, var_obs): # Nick
        indices = {}
        for variable, value in var_obs.items(): 
            index = list(np.where(self.df[variable] == value))
            indices[variable] = (set(index[0]))
        # for loop thru dictionary, find intersect of each value set
        inter = list(indices.values())[0]
        for value in indices.values():
            inter = inter.intersection(value)
        self.df.delete_obs(inter)
    
""" Open CSV file and save contents to a dataframe. First row must be variables. """
def open_csv(filename): # Nick
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

""" Delete observation (row). Search all obs within given var and drop if they match. search thru one variable and delete all instances """
def delete_obs_by_var(file, obs, var): # Nick. 
    obslist = []
    for index, contents in file.iterrows():
        if obs in contents[var]:
            obslist.append(index)
    file = delete_obs(file, obslist)
    return(file)

"""take a dictionary {variable name:variable value} and delete observations that match given values. No limit to dictionary argument length."""
"""Can probably use this as a base for keep by multi var """
def delete_obs_by_var_multi(file, var_obs): # Nick
    indices = {}
    for variable, value in var_obs.items(): 
        index = list(np.where(file[variable] == value))
        indices[variable] = (set(index[0]))
    # for loop thru dictionary, find intersect of each value set
    inter = list(indices.values())[0]
    for value in indices.values():
        inter = inter.intersection(value)
    file = delete_obs(file, inter)
    return(file)

        
""" Split file by observation. Take a variable to look under and a list of 
observations, and move all rows containing the observations in the list to a new file. 
Make sure to avoid crashing the whole program if the obs in list aren't found. """
def split_obs(file, target_filename, target_var, obs): # Zhangir
    pass

""" Split file by variable. Take a list of variables and move those variables 
into a separate CSV file, along with optional other variables  to copy (not move) too.  """
def split_var(file, target_filename, varlist, copylist=[]): # Zhangir
    pass

""" Append a list of observations from csv to an existing file, target_filename"""
def append(file, target_filename, obs): #Zhangir

    with open(target_filename, 'a', newline='') as f:
     writer = csv.writer(f)
     for row in obs:
        writer.writerow(row)

    pass

""" Delete duplicate observations. Select whether complete duplicates should be
removed, or if observations with duplicated list of var values should be removed. 
Make sure to keep the original. """

def delete_duplicates(file):
    unique_rows = []
    with open(file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        unique_rows.append(header)
        for row in reader:
            is_duplicate = False
            for prev_row in unique_rows:
                if row == prev_row:
                    is_duplicate = True
                    break
                elif row[0] == prev_row[0]:
                    is_duplicate = True
                    unique_rows.remove(prev_row)
                    break
            if not is_duplicate:
                unique_rows.append(row)

    with open('{}_unique.csv'.format(file.split('.csv')[0]), 'w', newline='') as f:
        writer = csv.writer(f)
        for row in unique_rows:
            writer.writerow(row)
    pass

def sort_csv(file, sort_column):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    sorted_rows = sorted(rows, key=lambda x: x[sort_column])
    sorted_rows.insert(0, header)
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sorted_rows)

def raise_gui_error():
    print('error')
    
def save_df_to_csv(df, target_filename):
    return(df.to_csv(target_filename, index = False))

def rename_var(file):
    pass

if __name__ == '__main__': # does not execute this part if importing from another file
    test = open_csv("test.csv")
    print(test)
    print()
    print(delete_obs_by_var(test, 'alpha', 'name'))
    print()
    test = (delete_obs_by_var_multi(test, {'id':1, 'name':'alpha', 'location':'worc'}))
    save_df_to_csv(test, "saved_test1.csv")
