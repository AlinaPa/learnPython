from datetime import datetime, timedelta

# Вчера
today = datetime.today()
dt_yesterday = today - timedelta(days=1)
print(dt_yesterday)

# Сегодня
dt_today = datetime.today()
print(dt_today)

# Завтра
today = datetime.today()
dt_tomorrow = today + timedelta(days=1)
print(dt_tomorrow)

# Превратите строку в объект datetime
date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S:%f')
print(date_dt)
