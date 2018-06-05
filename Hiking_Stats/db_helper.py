import psycopg2 as pg2
import creds as cr

conn = pg2.connect(cr.connect_creds)
curs = conn.cursor()


def insert_hiking_stats(p_date, p_cal_burned, p_miles_walked, p_mph, p_duration, p_additonal_weight, p_weight_amt, p_trekking_poles, p_shoe_id, p_trail_id):
    with curs as c:
        HIKING_STATS_SQL = """SELECT fit_hiking_ins();"""
        c.execute(HIKING_STATS_SQL)
        c.commit()
        c.close()
        conn.close()


curs.close()
conn.close()
