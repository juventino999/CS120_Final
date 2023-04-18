"""
Created on Fri Apr 14 10:33:28 2023

@author: juventino1112
"""
#import numpy as np
import pandas as pd
import numpy as np
""" Open CSV file and save contents to a list of lists. First row must be variables. """
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

"""take a dictionary {variable name:variable value} and delete observations that match given values"""
def delete_obs_by_var_multi(file, var_obs):
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
    test = open_csv("test.csv")
    print(test)
    print()
    print(delete_obs_by_var(test, 'alpha', 'name'))
    print()
    print(delete_obs_by_var_multi(test, {'id':1, 'name':'alpha', 'location':'worc'}))
