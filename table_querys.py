#!/usr/bin/python3.6

# This function retrieves all records from the weld_log table.
def get_weld_log(weld_cursor):
    # selection string for weld_log table.
    weld_select = "SELECT * FROM weld_log;"
    try:
        weld_cursor.execute(weld_select)
        weld_rows = weld_cursor.fetchall()
        for row in weld_rows:
            print(row)
            return weld_rows
    except Exception as e:
        print("No records")
        print(e)

# This function retrieves all records from the pup_assets table.
def get_pup_assets(pup_cursor):
    #selection string for pup_assets table.
    pup_select = "SELECT * FROM pup_assets;"
    try:
        pup_cursor.execute(pup_select)
        pup_rows = pup_cursor.fetchall()
        for row in pup_rows:
            print(row)
            return pup_rows
    except Exception as e:
        print("No records")
        print(e)

# This function retrieves all the records from the bend_assets table.
def get_bnd_assets(bnd_cursor):
    # selection string for the bnd_assets table;
    bend_select = "SELECT * FROM bend_assets;"
    try:
        bnd_cursor.execute(bend_select)
        bnd_rows = bnd_cursor.fetchall()
        for row in bnd_rows:
            print(row)
            return bnd_rows
    except Exception as e:
        print("No records")
        print(e)

# This function retrieves all the records from the all_attributes view.
def get_aa_view(aa_view_cursor):
    # selection string for the all_attributes view.
    aa_select = "SELECT * FROM all_attributes;"
    try:
        aa_view_cursor.execute(aa_select)
        aa_view_rows = aa_view_cursor.fetchall()
        for row in aa_view_rows:
            print(row)
            return aa_view_rows
    except Exception as e:
        print("No records")
        print(e)
