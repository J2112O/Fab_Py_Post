#!/usr/bin/python3.6

import psycopg2 as pg2
import creds as cr
from daily_entry import collect_daily_stats as cds

shoe_labels = ("shoe_id", "name_brand",)
trial_labels = ("trail_id", "name", "surface_material",)
SHOE_SQL = "SELECT * FROM shoe_brand;"
TRAIL_SQL = "SELECT * FROM trail_route"

HIKING_STATS_SQL = "SELECT fit_hiking_ins(date_obj, cal_burned, miles_walked, mph, dur_obj, additional_weight, weight_amount, trekking_poles, shoe_id, trail_id);"

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
