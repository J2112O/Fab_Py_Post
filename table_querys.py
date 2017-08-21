#!/usr/bin/python3.6

# This function retrieves all records from the weld_log table.
def get_weld_log(weld_cursor):
    try:
        weld_cursor.execute("""SELECT * FROM weld_log;""")
        weld_rows = weld_cursor.fetchall() 
        for row in weld_rows:
            print(row)
            return weld_rows
    except Exception as e:
        print("No records")
        print(e)

# This function retrieves all records from the pup_assets table.
def get_pup_assets(pup_cursor):
    try:
        pup_cursor.execute("""SELECT * FROM pup_assets;""")
        pup_rows = pup_cursor.fetchall()
        for row in pup_rows:
            print(row)
            return pup_rows
    except Exception as e:
        print("No records")
        print(e)

# This function retrieves all the records from the bend_assets table.
def get_bnd_assets(bnd_cursor):
    try:
        bnd_cursor.execute("""SELECT * FROM bend_assets;""")
        bnd_rows = bnd_cursor.fetchall()
        for row in bnd_rows:
            print(row)
            return bnd_rows
    except Exception as e:
        print("No records")
        print(e)

# This function retrieves all the records from the all_attributes view.
def get_aa_view(aa_view_cursor):
    try:
        aa_view_cursor.execute("""SELECT * FROM all_attributes;""")
        aa_view_rows = aa_view_cursor.fetchall()
        for row in aa_view_rows:
            print(row)
            return aa_view_rows
    except Exception as e:
        print("No records")
        print(e)
