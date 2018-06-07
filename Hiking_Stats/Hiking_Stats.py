#!/usr/bin/python3.6


class HikingStats:
    """Class for HikingStats

    Class of all values for the hiking stats to insert
    """

    def __init__(self, date_obj, cal_burned, miles_walked, mph, dur_obj, additional_weight, weight_amount, trekking_poles, shoe_id, trail_id):
        self.date_obj = date_obj
        self.cal_burned = cal_burned
        self.miles_walked = miles_walked
        self.mph = mph
        self.dur_obj = dur_obj
        self.additional_weight = additional_weight
        self.weight_amount = weight_amount
        self.trekking_poles = trekking_poles
        self.shoe_id = shoe_id
        self.trail_id = trail_id
