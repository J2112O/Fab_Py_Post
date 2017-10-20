#!/usr/bin/python3.6

import psycopg2 as pg2
import constants as cons # from the constants.py file
import table_querys as tq # from the table_querys.py file
# both of the below imports are for the google aa_sheets API
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',
                                                         scope)
client = gspread.authorize(creds)
sheet = client.open('Fab Tracking')
aa_sheet = sheet.worksheet('all_attributes')
ba_sheet = sheet.worksheet('bend_assets')
pa_sheet = sheet.worksheet('pup_assets')

try:
    # use our connection values to establish a connection
    conn = pg2.connect(cons.connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # create a new table with a single column called "name"
except pg2.DatabaseError as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)

def sht_aa():
    an_insert = [row for row in tq.get_all_attributes(cursor)]
    for x in an_insert:
        aa_sheet.insert_row(x, row_count + 1)

def sht_ba():
    an_insert = [row for row in tq.get_bnd_assets(cursor)]
    for x in an_insert:
        ba_sheet.insert_row(x, row_count + 1)

def sht_pa():
    an_insert = [row for row in tq.get_pup_assets(cursor)]
    for x in an_insert:
        pa_sheet.insert_row(x, row_count + 1)


def main():
    print("Hello World. Just a text")
    #choice = str(input("Which Google Sheet do you wish to upload data to? " \
                #"All (ALL), pup_assets (PUP) or bend_assets (BEND). ")).upper()
    #an_insert = [row for row in tq.get_pup_assets(cursor)]
    #for x in an_insert:
        #pa_sheet.insert_row(x, 2)
    if cursor:
        cursor.close()

if __name__=="__main__":
    main()
