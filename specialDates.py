# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:31:17 2020

@author: orkun.yuzbasioglu
"""

#Ozel takvim gunleri

import pandas as pd
import datetime

from workalendar.europe import Turkey
from itertools import chain

#Dataframe icin baslangic ve bitis tarihleri
baslangic = 2015
bitis = 2020

dates = []
events = []

cal = Turkey()

special_dates = [cal.holidays(year) for year in range(baslangic, bitis+1)]

dates = [el[0] for el in list(chain(*special_dates))]
events= [el[1] for el in list(chain(*special_dates))]

special_dates_df = pd.DataFrame({'Date':dates, 'Event':events})
special_dates_df['Date'] =  pd.to_datetime(special_dates_df['Date'])

calender = pd.DataFrame({'Date':pd.date_range(start='1/1/'+str(baslangic), end='3/15/'+str(bitis))})

calender_df = calender.merge(special_dates_df, how='left').fillna('OzelGunDegil')

calender_df.head()
calender_df.tail()
