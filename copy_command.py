#!/usr/bin/python3.6

import psycopg2 as pg2
import constants as cons # Importing the constants.py file

# This variable holds the path to the staging.csv 
staging_path = r"/home/bigdaddy/Practice_Data/Daily_Pipe_Tally_python_staging.csv"

SQL = "COPY staging_assets FROM STDIN DELIMITER ',' CSV HEADER;"

try:
     # use our connection values to establish a connection
     conn = pg2.connect(cons.connect_str)
     # create a psycopg2 cursor that can execute queries
     cursor = conn.cursor()
     # catch the connection errors here with warning and the error by printing e
except pg2.DatabaseError as e:
     print("Uh oh, can't connect. Invalid dbname, user or password?")
     print(e)


def main():
    try:
        # staging path contains the path to Daily_Pipe_Tally_python.csv file
        with open(staging_path) as f:
            cursor.copy_expert(SQL,f)
            conn.commit()
            cursor.close()
    except pg2.DatabaseError as e:
        print("Uh-oh. Insert issues. Please see error message.")
        print(e)


if __name__ == "__main__":
    main()
