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
        return(self.df.to_string())
    def delete_var(self, varlist):
        self.df = self.df.drop(varlist, axis = 1)
    def delete_obs(self, obslist):
        self.df = self.df.drop(obslist, axis = 0)
    def delete_obs_by_var(self, obs, var): 
        obs = obs[0] # because obs and var are given as a list, take obs to be first element in the list
        var = var[0]
        obslist = []
        for index, contents in self.df.iterrows():
            if obs in contents[var]:
                obslist.append(index)
        self.delete_obs(obslist) #this need to be fixed?
    def delete_obs_by_var_multi(self, varlist, obslist):
        # create var_obs dictionary from varlist and obslist 
        var_obs = {}
        for i in range(len(varlist)):
            var_obs[varlist[i]] = obslist[i] 
        indices = {}
        for variable, value in var_obs.items(): 
            index = list(np.where(self.df[variable] == value))
            indices[variable] = (set(index[0]))
        # for loop thru dictionary, find intersect of each value set
        inter = list(indices.values())[0]
        for value in indices.values():
            inter = inter.intersection(value)
        self.delete_obs(inter)
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

            # Write the header row to the output file
            writer.writerow(header)

            # Loop through the input file
            for row in reader:
                # Split the row into the variables to move and the variables to keep
                move_vars = [row[i] for i in move_indices]

                # Write the ID and variables to move and copy to the output file
                writer.writerow([row[0]] + move_vars)

""" Split file by observation. Take a variable to look under and a list of 
observations, and copy all rows containing the observations in the list to a new file. 
Make sure to avoid crashing the whole program if the obs in list aren't found.  """
"""to-do: delete duplicate column"""
def split_obs(file, target_filename, target_var, obs): # Zhangir
    # Open input file and output file
    with open(file, 'r') as f_in, open(target_filename, 'w', newline='') as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)
        header = next(reader)  # read header
        target_col = header.index(target_var)  # get index of target variable column
        writer.writerow([header[0], target_var] + header[1:])  # write header row

        # Loop through rows and write to output file
        for row in reader:
            if row[target_col] in obs:
                writer.writerow([row[0], row[target_col]] + row[1:])

""" Append a list of observations from csv to an existing file, target_filename"""
def append(file, target_filename, obs): #Zhangir

    with open(target_filename, 'a', newline='') as f:
     writer = csv.writer(f)
     for row in obs:
        writer.writerow(row)



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
""" to-do: fix TypeError"""
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

def rename_var(file):
    pass

if __name__ == '__main__': # does not execute this part if importing from another file
    s = Sheet("saved_test.csv")
    print(s)
    s.delete_obs_by_var_multi(['name', 'location'], ['alpha', 'worc'])
    print()
    print(s)
    