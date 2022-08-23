import csv
#import gspread

MONTH = 'august'

file = f"sber_{MONTH}.csv"

transactions = []

with open(file, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')
    for row in csv_reader:
        if row:
            DATE = row[1]
            NAME = row[3]
            AMOUNT = row[4]
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
            

#sa = gspread.service_account()
#sh = sa.open("financeManager")