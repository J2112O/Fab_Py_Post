#!/usr/bin/python3.6

import psycopg2 as pg2
from creds import connect_str

SQL = "SELECT * FROM shoe_brand;"

with pg2.connect(connect_str) as conn:
    with conn.cursor() as curs:
        curs.execute(SQL)
        shoe_rows = curs.fetchall()
        for row in shoe_rows:
            print(row)
