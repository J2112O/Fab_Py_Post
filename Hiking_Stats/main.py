#!/usr/bin/python3.6

import psycopg2 as pg2
import creds as cr

shoe_labels = ("shoe_id", "name_brand",)
trial_labels = ("trail_id", "name", "surface_material",)
SHOE_SQL = "SELECT * FROM shoe_brand;"
TRAIL_SQL = "SELECT * FROM trail_route"

with pg2.connect(cr.connect_creds) as conn:
    with conn.cursor() as curs:
        curs.execute(SHOE_SQL)
        shoe_rows = curs.fetchall()
        print(shoe_labels)
        for row in shoe_rows:
            print(row)
        print(trial_labels)
        curs.execute(TRAIL_SQL)
        trail_rows = curs.fetchall()
        for row in trail_rows:
            print(row)
