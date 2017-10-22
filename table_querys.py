#!/usr/bin/python3.6

pipe_select = """SELECT * FROM pipe_assets WHERE  kind = 'PIPE_JOINT';"""
bend_select = """SELECT pa.custom_name, pa.joint_number, pa.heat, pa.pipe_length, pa.wall_thickness, pa.kind, b.degree
                FROM pipe_assets AS pa
                LEFT JOIN bend AS b
                ON pa.custom_name = b.bend_id
                WHERE pa.kind = 'BEND'
                ORDER BY pa.custom_name ASC;"""

unknown_select = """SELECT pa.custom_name, pa.joint_number, pa.heat, pa.pipe_length, pa.wall_thickness, unk.kind
                FROM pipe_assets AS pa
                LEFT JOIN unknown_assets AS unk
                ON pa.custom_name = unk.unknown_id
                WHERE pa.kind NOT IN ('BEND', 'PIPE_JOINT')
                ORDER BY pa.custom_name ASC;"""


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
def get_pipe_assets(pipe_cursor):
    try:
        pipe_cursor.execute(pipe_select)
        pipe_rows = pipe_cursor.fetchall()
        for row in pipe_rows:
            print(row)
            return pipe_rows
    except Exception as e:
        print("No records")
        print(e)


# This function retrieves all the records from the bend_assets table.
def get_bend_assets(bend_cursor):
    try:
        bend_cursor.execute(bend_select)
        bend_rows = bend_cursor.fetchall()
        for row in bend_rows:
            print(row)
            return bend_rows
    except Exception as e:
        print("No records")
        print(e)


def get_unknown_assets(unk_cursor):
    try:
        unk_cursor.execute(unknown_select)
        unk_rows = unk_cursor.fetchall()
        for row in unk_rows:
            print(row)
            return unk_rows
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
