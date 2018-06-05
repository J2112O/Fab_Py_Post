#!/usr/bin/python3.6

from db_helper import insert_hiking_stats
from daily_stats import collect_daily_stats
from Hiking_Stats import HikingStats


def main():
    stats = collect_daily_stats()
    h_stats = HikingStats(*stats)
    insert_vals = tuple(h_stats)
    insert_hiking_stats(*insert_vals)


if __name__ == '__main__':
    main()
