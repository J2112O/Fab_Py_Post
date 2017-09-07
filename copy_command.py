#!/usr/bin/python3.6

import psycopg2 as pg2
import constants as cons # Importing the constants.py file

SQL = "COPY staging_assets FROM STDIN DELIMITER ',' CSV HEADER;"

try:
     # use our connection values to establish a connection
     conn = pg2.connect(cons.connect_str)
     # create a psycopg2 cursor that can execute queries
     cursor = conn.cursor()
     # create a new table with a single column called "name"
except pg2.DatabaseError as e:
     print("Uh oh, can't connect. Invalid dbname, user or password?")
     print(e)


def main():
    # cons.staging_path contains the path to the .csv file
    with open(cons.staging_path) as f:
        cursor.copy_expert(SQL,f)
        conn.commit()
        cursor.close()


if __name__ == "__main__":
    main()

