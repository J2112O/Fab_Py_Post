#!/usr/bin/python3.6

import psycopg2 as pg2
import constants as cons # from the constants.py file
import csv

path = "/home/bigdaddy/Practice_Data/Daily_Pipe_Tally_python_staging.csv"

data_file = open(path, newline='')
reader = csv.reader(data_file)

header = next(reader)

data = []
for row in reader:
    #row = [pipe_id, kind, jt_num, heat, pipe_length, wall_thick, deg]
    custom_pipe_id = str(row[0])
    pipe_kind = str(row[1])
    pipe_jt_num = str(row[2])
    pipe_ht = str(row[3])
    pipe_lt = float(row[4])
    pipe_wt = float(row[5])
    pipe_deg = float(row[6])

    data.append([custom_pipe_id,pipe_kind,pipe_jt_num,pipe_ht,pipe_lt,
                 pipe_wt,pipe_deg])

for row in data:
    print(row)
