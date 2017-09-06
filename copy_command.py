#!/usr/bin/python3.6

import constants as cons # Importing the constants.py file
import csv

# This variable holds the path that contains the csv file from constants.py
path = cons.staging_path

data_file = open(path, newline='') # Opening and striping any newlines
reader = csv.reader(data_file) # Creating a reader obj

header = next(reader) # Skipping the header

def copy_insert():
    data = []
    for row in reader:
        # row = [pipe_id, kind, jt_num, heat, pipe_length, wall_thick, deg]
        custom_pipe_id = str(row[0]) # Casting to string
        pipe_kind = str(row[1])# Casting to string
        pipe_jt_num = str(row[2])# Casting to string
        pipe_ht = str(row[3])# Casting to string
        pipe_lt = float(row[4])# Casting to float
        pipe_wt = float(row[5])# Casting to float
        pipe_deg = float(row[6])# Casting to float

        # Appending the correct data types for the columns to the 'data' list
        data.append([custom_pipe_id,pipe_kind,pipe_jt_num,pipe_ht,pipe_lt,
                    pipe_wt,pipe_deg])
    return data
