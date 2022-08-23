import csv
from operator import delitem
from sre_constants import CATEGORY
#import gspread

MONTH = 'august'

file = f"sber_{MONTH}.csv"

transaction = []

with open(file, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')
        for row in csv_reader:
            if row:
                DATE = row[1]
                NAME = row[3]
                AMOUNT = row[4]
                CURRENCY = row[5]
                CATEGORY = 'other'
                transaction = ((DATE, NAME, AMOUNT, CURRENCY, CATEGORY ))
                print(transaction)
            

#sa = gspread.service_account()
#sh = sa.open("financeManager")