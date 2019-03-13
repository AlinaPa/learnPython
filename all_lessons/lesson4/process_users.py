import csv

fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
money_total = 0

with open('users.csv', 'r', encoding='utf-8') as users:
    reader = csv.DictReader(users, fields, delimiter=';')
    for row in reader:
        money_total += float(row['balance'])
print(money_total)
