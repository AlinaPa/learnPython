# coding=utf-8
age = int(input('Введите Ваш возраст: '))


def work_by_age():
    if age <= 6:
        print('Вы должны учиться в детском саду')
    elif 7 <= age <= 15:
        print('Вы должны учиться в школе')
    elif 16 <= age <= 23:
        print('Вы должны учиться в Вузе')
    elif 16 <= age <= 65:
        print('Вы должны работать')
    else:
        print('Можно отдохнуть на пенсии')


work_by_age()
