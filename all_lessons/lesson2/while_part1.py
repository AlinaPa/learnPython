# coding=utf-8
# Первая часть задания


def ask_user():
    question = str(input('Как дела?: '))
    while question:
        if question == str('Хорошо'):
            break
        else:
            question = str(input('Как дела?: '))


ask_user()


