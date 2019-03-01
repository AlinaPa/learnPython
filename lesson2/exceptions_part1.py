# coding=utf-8


def ask_user():
    try:
        question = str(input('Как дела?: '))
        while question:
            if question == str('Хорошо'):
                break
            else:
                question = str(input('Как дела?: '))
    except KeyboardInterrupt:
        print("Пока!")


ask_user()
