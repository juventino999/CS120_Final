"""
Created on Fri Apr 14 10:33:28 2023

@author: juventino1112
TO-DO:
    - Finish missing functions
    - Change CSV-based to df-based
"""
#import numpy as np
import pandas as pd
import csv

""" Change to class structure instead? Would probably be easier, can update with methods instead of having to call functions
#class Sheet(): # change out filename for self and make them all methods"""

class Sheet:
    def __init__(self, filename):
        self.df = pd.read_csv(filename)
        #self.df.applymap(str) #think this part is unnecessary, have to test further
        
    def __repr__(self):
        return(self.df.to_string())
    
    def delete_var(self, varlist, obslist=[]): #unused obslist so can use generic button function in GUI. could make it optional here but can't in following func
        self.df = self.df.drop(varlist, axis = 1)
        
    def delete_obs(self, varlist, obslist): #varlist is unused here, just pass an empty list. necessary for button function in GUI
        #gui program wasn't working w GUI because it was feeding the function strings instead of ints, now convert obslist to ints then run 
        for i in range(len(obslist)):
            obslist[i] = int(obslist[i])
        self.df = self.df.drop(obslist, axis = 0)
        
    def delete_obs_by_var(self, var, obs): # inputs in lists must be str
        obs = obs[0] # because obs and var are given as a list, take obs to be first element in the list
        var = var[0]
        obslist = []
        for index, contents in self.df.iterrows(): # was previously getting error when contents were int
            contents = contents[var] # so make contents just the target variable part
            contents = str(contents) # and make it to a string
            if obs in contents:
                obslist.append(index)
        self.delete_obs([], obslist)
        
    def delete_obs_by_var_multi(self, varlist, obslist): # this must use an integer as argument if the df has an integer in it
        # create var_obs dictionary from varlist and obslist 
        # current issue: if trying to use this after using delete obs or delete_obs_by_var, won't work. delete obs looks at pandas df index, this just looks at which column it is in existing columns. need to find pandas df index.
        var_obs = {}
        for i in range(len(varlist)):
            var_obs[varlist[i]] = obslist[i] 
        indices = {}
        for variable, value in var_obs.items(): # iteratr thru target variables and variable values
            try:
                value = int(value)
            except:
                pass
            variable = str(variable)
            # old implementation in comment below, new implementation should take care of current issue
            index = []
            for ind, row in self.df.iterrows():
                if row[variable] == value:
                    index.append(ind)
            #index = list(np.where(self.df[variable] == value)) # index = a list of where the variable == string version of value. below, set(index) was set(index[0])
            indices[variable] = (set(index)) # construct a dictionary with the key being the variable and the value being a set containing the list above
        # for loop thru dictionary, find intersect of each value set
        inter = list(indices.values())[0]
        for value in indices.values():
            inter = inter.intersection(value)
        inter= list(inter) # turn the set into a list so it can be converted to int in delete_obs()
        self.delete_obs([], inter)
        
    def save_df_to_csv(self, target_filename):
        return(self.df.to_csv(target_filename, index = False))
        
""" Split file by variable. Take a list of variables and copy those variables 
into a separate CSV file"""
"""to-do: delete unused variable names, remove row[0] from line 115"""
def split_var(file, target_filename, varlist): #Zhangir
    # Open the input file for reading
    with open(file, 'r') as infile:
        reader = csv.reader(infile)
        header = next(reader) # Get the header row

        # Get the indices of the variables to move
        move_indices = [header.index(var) for var in varlist]

        # Open the output file for writing
        with open(target_filename, 'w', newline='') as outfile:
            writer = csv.writer(outfile)

            # Write the header of ID and the chosen variable to the output file
            writer.writerow(['ID'] + varlist)

            # Loop through the input file
            for row in reader:
                # Split the row into the variables to move and the variables to keep
                move_vars = [row[i] for i in move_indices]

                # Write the ID and variables to move and copy to the output file
                writer.writerow([row[0]] + move_vars)

""" Split file by observation. Take a variable to look under and a list of 
observations, and copy all rows containing the observations in the list to a new file. 
Make sure to avoid crashing the whole program if the obs in list aren't found.  """

def split_obs(file, target_filename, target_var, obs): # Zhangir
    # Open input file and output file
    with open(file, 'r') as f_in, open(target_filename, 'w', newline='') as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)
        header = next(reader)  # read header
        target_col = header.index(target_var)  # get index of target variable column
        writer.writerow([header[0:])  # write header row

        # Loop through rows and write to output file
        for row in reader:
            if row[target_col] in obs:
                writer.writerow([row[0:])

""" Append a list of observations from csv to an existing file, target_filename"""
def append(file, target_filename, obs): #Zhangir
    # Open the main file and read the data
    with open(file, 'r') as main_file:
        main_reader = csv.reader(main_file)
        main_data = list(main_reader)
    
    # Open the second file and read the data
    with open(obs, 'r') as obs_file:
        obs_reader = csv.reader(obs_file)
        # Skip the header row
        next(obs_reader)
        obs_data = list(obs_reader)
    
    # Create the new file and write the combined data
    with open(target_filename, 'w', newline='') as target_file:
        target_writer = csv.writer(target_file)
        # Write the data from the main file
        target_writer.writerows(main_data)
        # Write the data from the second file
        target_writer.writerows(obs_data)



""" Delete duplicate observations """

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

def sort_csv(file, sort_column):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    # Find the index of the sort column by searching for its name in the header row
    sort_index = header.index(sort_column)
    sorted_rows = sorted(rows, key=lambda x: x[sort_index])
    sorted_rows.insert(0, header)
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sorted_rows)
                                 
def rename_var(file):
    pass

if __name__ == '__main__': # does not execute this part if importing from another file
    pass
    
