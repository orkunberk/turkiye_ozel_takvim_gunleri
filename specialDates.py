# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:18:09 2020

@author: orkun.yuzbasioglu
"""

#Special Dates
import pandas as pd
import datetime

from workalendar.europe import Turkey
from itertools import chain

cal = Turkey()

#special_dates = list((chain([cal.holidays(year) for year in range(2018, 2021)])))
special_dates = [cal.holidays(year) for year in range(2016, 2021)]

dates = []
events = []

dates = list(chain(*[[day[0] for day in year] for year in special_dates]))
events = list(chain(*[[day[1] for day in year] for year in special_dates]))
special_dates_df = pd.DataFrame({'Date':dates, 'event':events})
special_dates_df['Date'] =  pd.to_datetime(special_dates_df['Date'])

''' 20.03
special_dates_final = special_dates_df.copy()
special_dates_final['event'] = 1
special_dates_final['event']  = pd.to_numeric(special_dates_final['event'])
'''

#Dates processing
calender = pd.DataFrame({'Date':pd.date_range(start='1/1/2016', end='3/15/2020')})
#calender_df = calender.merge(special_dates_final, how='left').fillna(0)
calender_df = calender.merge(special_dates_df, how='left').fillna('NotASpecialDate')
calender_df.set_index('Date', inplace=True)
calenderHourly = calender_df.resample('60min').ffill()

#calenderHourly.drop(calenderHourly.tail(1).index, inplace=True)