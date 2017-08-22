#!/usr/bin/python3.6
import psycopg2 as pg2
import constants as cons # from the constants.py file
import table_querys as tq # from the table_querys.py file
# both of the below imports are for the google aa_sheets API
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Fab Tracking')
ba_sheet = sheet.worksheet('bend_assets') # Assigning the bend_assets sheet here.

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
    # Creating a list through list comprehensions based on the list returned from the get_bnd_assets() function.
    an_insert = [row for row in tq.get_bnd_assets(cursor)]
    for x in an_insert:
        ba_sheet.insert_row(x, 2) # beginning the insert of each row at the 2nd
    if cursor:                    # row since the first row is in 'freeze' mode for column headers
        cursor.close()            # Need to look at adding in always subtracting one from how many
                                  # rows are present in the sheet to.

if __name__=="__main__":
    main()
