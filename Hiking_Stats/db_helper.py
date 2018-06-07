import psycopg2 as pg2
import creds as cr


def insert_hiking_stats(some_date_obj, some_cal_burned, some_miles_walked, some_mph, some_dur_obj, some_additional_weight, some_weight_amount, some_trekking_poles, some_shoe_id, some_trail_id):
    """
    Function for inserting values.

    Function calls the fit_hiking_ins() database funtions and inserts values

    Arguments:
    """
    with pg2.connect(cr.connect_creds) as conn:
        with conn.cursor() as curs:
            curs.execute("""SELECT fit_hiking_ins(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (some_date_obj, some_cal_burned, some_miles_walked, some_mph, some_dur_obj, some_additional_weight, some_weight_amount, some_trekking_poles, some_shoe_id, some_trail_id))
            print("Inserts sucessful.")
