#!/usr/bin/python3.6

from db_helper import insert_hiking_stats
from daily_stats import collect_daily_stats
from Hiking_Stats import HikingStats


def main():
    # Assigning the tuple of values from collect_daily_stats() function to variable.
    stats = collect_daily_stats()
    # Creating a HikingStats obj and unpacking the tuple into it.
    h_stats = HikingStats(*stats)
    # Calling the insert_hiking_stats database function passing in all the instance variables.
    insert_hiking_stats(h_stats.date_obj, h_stats.cal_burned, h_stats.miles_walked, h_stats.mph, h_stats.dur_obj, h_stats.additional_weight, h_stats.weight_amount, h_stats.trekking_poles, h_stats.shoe_id, h_stats.trail_id)


if __name__ == '__main__':
    main()
