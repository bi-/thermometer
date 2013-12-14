# -*- coding: utf-8 -*-
import gspread
import datetime
import time
from temp import read_temp

while True:
        gc = gspread.login('...','...')
        values = [datetime.datetime.now(), read_temp()]
        wks = gc.open("...").sheet1
        wks.append_row(values)
        time.sleep(600)
