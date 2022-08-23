import csv
#import gspread
import time

MONTH = 'august'

file = f"sber_{MONTH}.csv"

transactions = []

sum = 0

def sberFin(file):

    with open(file, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')
        next(csv_reader)
        for row in csv_reader:
            if row:
                DATE = row[1]
                NAME = row[3]
                AMOUNT = int(row[4])
                sum += AMOUNT
                CURRENCY = row[5]
                CATEGORY = 'other'
                if NAME == "Супермаркеты":
                    CATEGORY = 'Eat'
                if NAME == "Другим людям":
                    CATEGORY = 'Money transfer'
                if NAME == 'ЖКХ, связь, интернет':
                    CATEGORY = 'Internet'
                if NAME == 'Образование':
                    CATEGORY = 'Book or Education'
                transaction = ((DATE, NAME, AMOUNT, CURRENCY, CATEGORY))
                print(transaction)
                transactions.append(transaction)
            return transactions

# sa = gspread.service_account()
# sh = sa.open("Personal Finances")

# wks = sh.worksheet(f"{MONTH}")

# for row in rows:
#     wks.insert_row([row[1], row[3], row[4], row[5]], 8)
#     time.sleep(2)

# rows = sberFin(file)

# wks.insert_row([1,2,3], 10)