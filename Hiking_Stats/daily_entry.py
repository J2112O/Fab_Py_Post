#!/usr/bin/python3.6
import datetime
from datetime import date, time


def collect_daily_stats():
    """This function collects all daily hiking stats for insert into the database.
    """
    while True:
        try:
            day_walked = str(input("Date Hiked (Format: DD-Mon-YYYY) - Note for the current date, enter 'Today' ")).upper()
            if day_walked == 'TODAY':
                date_obj = date.today()
            else:
                format_string = '%d-%b-%Y'
                date_entry = datetime.datetime.strptime(day_walked, format_string).date()
                date_obj = datetime.date(date_entry.year, date_entry.month, date_entry.day)
        except Exception as e:
            raise e
        else:
            break

    while True:
        try:
            cal_burned = float(input("Calories burned: "))
        except ValueError:
            print("Decimal numbers only.")
        else:
            break

    while True:
        try:
            miles_walked = float(input("Miles Walked: "))
        except ValueError:
            print("Decimal numbers only.")
        else:
            break

    while True:
        try:
            mph = float(input("Pace (in mph): "))
        except ValueError:
            print("Decimal numbers only.")
        else:
            break

    while True:
        try:
            duration = str(input("Duration in hours, minutes, and seconds (Format hh:mm:ss): "))
            d_split = [int(item) for item in duration.split(':')]
            # Creating the time object to be stored by passing in the appropriate casted list elements ie(index[0] is hour, etc...)
            dur_obj = datetime.time(d_split[0], d_split[1], d_split[2])
        except Exception as e:
            raise e
        else:
            break

    while True:
        try:
            additional_weight = str(input("Additional weight (True or False): ")).title()
            if additional_weight == "True":
                weight_amount = float(input("Added weight: "))
                additional_weight = True
            else:
                additional_weight = False
                weight_amount = 0.0
        except ValueError:
            print("Decimal numbers only.")
        else:
            break

    while True:
        try:
            trekking_poles = str(input("Trekking Poles Used? (True or False): ")).title()
            if trekking_poles == "True":
                trekking_poles = True
            else:
                trekking_poles = False
        except Exception as e:
            raise e
            print("True or False input only. ")
        else:
            break

    while True:
        try:
            shoe_id = int(input("Shoe id of shoes worn: "))
        except ValueError:
            print("Whole numbers only.")
        else:
            break

    while True:
        try:
            trail_id = int(input("Trail id of trail hiked: "))
        except ValueError:
            print("Whole numbers only.")
        else:
            break

    return date_obj, cal_burned, miles_walked, mph, dur_obj, additional_weight, weight_amount, trekking_poles, shoe_id, trail_id


if __name__ == '__main__':
    collect_daily_stats()
