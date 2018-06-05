import datetime
from datetime import date, time


def collect_daily_stats():
    """Collects user input


    Raises:
        e -- [description]
        e -- [description]
        e -- [description]
    """
    while True:
        try:
            day_walked = str(input("Date Hiked (Format: DD-Mon-YYYY) - Note for the current date, enter 'Today' ")).upper()
            if day_walked == 'TODAY':
                v_date_obj = date.today()
            else:
                format_string = '%d-%b-%Y'
                date_entry = datetime.datetime.strptime(day_walked, format_string).date()
                v_date_obj = datetime.date(date_entry.year, date_entry.month, date_entry.day)
        except Exception as e:
            raise e
        else:
            break

    while True:
        try:
            v_cal_burned = float(input("Calories burned: "))
        except ValueError:
            print("Decimal numbers only.")
        else:
            break

    while True:
        try:
            v_miles_walked = float(input("Miles Walked: "))
        except ValueError:
            print("Decimal numbers only.")
        else:
            break

    while True:
        try:
            v_mph = float(input("Pace (in mph): "))
        except ValueError:
            print("Decimal numbers only.")
        else:
            break

    while True:
        try:
            duration = str(input("Duration in hours, minutes, and seconds (Format hh:mm:ss): "))
            d_split = [int(item) for item in duration.split(':')]
            # Creating the time object to be stored by passing in the appropriate casted list elements ie(index[0] is hour, etc...)
            v_dur_obj = datetime.time(d_split[0], d_split[1], d_split[2])
        except Exception as e:
            raise e
        else:
            break

    while True:
        try:
            v_additional_weight = str(input("Additional weight (True or False): ")).title()
            if v_additional_weight == "True":
                v_weight_amount = float(input("Added weight: "))
                v_additional_weight = True
            else:
                v_additional_weight = False
                v_weight_amount = 0.0
        except ValueError:
            print("Decimal numbers only.")
        else:
            break

    while True:
        try:
            v_trekking_poles = str(input("Trekking Poles Used? (True or False): ")).title()
            if v_trekking_poles == "True":
                v_trekking_poles = True
            else:
                v_trekking_poles = False
        except Exception as e:
            raise e
            print("True or False input only. ")
        else:
            break

    while True:
        try:
            v_shoe_id = int(input("Shoe id of shoes worn: "))
        except ValueError:
            print("Whole numbers only.")
        else:
            break

    while True:
        try:
            v_trail_id = int(input("Trail id of trail hiked: "))
        except ValueError:
            print("Whole numbers only.")
        else:
            break

    return (v_date_obj, v_cal_burned, v_miles_walked, v_mph, v_dur_obj, v_additional_weight, v_weight_amount, v_trekking_poles, v_shoe_id, v_trail_id,)
