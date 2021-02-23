#!/usr/bin/env python
# coding: utf-8

# ### Türkiye Özel Takvim Günleri
# 
# Belirtilen tarih aralığında, Türkiye'deki özel takvim günlerini pandas dataframe oluşturma kodu.

import pandas as pd
import datetime
import warnings

from workalendar.europe import Turkey
from itertools import chain

cal = Turkey()

baslangic_yili = 2015
bitis_yili = 2020

dates = []
events = []

special_dates = [cal.holidays(year) for year in range(baslangic_yili, bitis_yili+1)]

dates = [el[0] for el in list(chain(*special_dates))]
events= [el[1] for el in list(chain(*special_dates))]


# #### Özel Günler Dataframe'i<br>
# `special_dates_df` özel takvim günlerini içeren bir `pandas` dataframe.


special_dates_df = pd.DataFrame({'Date':dates, 'Event':events})
special_dates_df['Date'] =  pd.to_datetime(special_dates_df['Date'])

# #### Tüm Günler Dataframe'i<br>
# `calender` özel takvim günlerini içeren bir `pandas` dataframe.

calender = pd.DataFrame({'Date':pd.date_range(start='1/1/'+str(baslangic_yili), end='31/12/'+str(bitis_yili))})

calender_df = calender.merge(special_dates_df, how='left').fillna('NotASpecialDate')