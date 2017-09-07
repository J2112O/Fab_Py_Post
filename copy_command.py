#!/usr/bin/python3.6

import psycopg2 as pg2
import constants as cons # Importing the constants.py file
import csv

SQL = "COPY staging_assets(pipe_id, kind, pipe_jt_num, pipe_heat, pipe_length,\
 pipe_wall_thickness, degree) FROM {} DELIMITER ',' CSV HEADER;".format(cons.staging_path)

try:
     # use our connection values to establish a connection
     conn = pg2.connect(cons.connect_str)
     # create a psycopg2 cursor that can execute queries
     cursor = conn.cursor()
     # create a new table with a single column called "name"
except pg2.DatabaseError as e:
     print("Uh oh, can't connect. Invalid dbname, user or password?")
     print(e)

# This variable holds the path that contains the csv file from constants.py
path = cons.staging_path

# Opening and striping any newlines from the csv file to insert
data_file = open(path, newline='')
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


def main():
    data_set = copy_insert()
    #cursor.copy_from(data_set,'staging_assets', sep=',',null='\\N',
    #                 size=8192,columns=cons.staging_tbl_rows)
    with open(cons.staging_path) as f:
        cursor.copy_expert(SQL,f)
        conn.commit()
        cursor.close()


if __name__ == "__main__":
    main()
