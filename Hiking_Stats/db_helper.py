import psycopg2 as pg2
import creds as cr

conn = pg2.connect(cr.connect_creds)
curs = conn.cursor()


def insert_hiking_stats(tup_of_values):
    """Function for inserting values.

    Function calls the fit_hiking_ins() database funtions and inserts values

    Arguments:
            tup_of_values {[tuple]} -- [a tuple containing values for insert]
    """
    with curs as c:
        HIKING_STATS_SQL = """SELECT fit_hiking_ins(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    c.execute(HIKING_STATS_SQL, *tup_of_values)
    c.commit()
    c.close()
    conn.close()


curs.close()
conn.close()
