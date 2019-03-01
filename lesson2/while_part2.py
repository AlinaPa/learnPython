options = {
    "Как дела?": "Хорошо!",
    "Что делаешь?": "Программирую",
    "Мы можем прервать разговор?": "Да, до связи!"
}


def get_options(user_question, options):
    return options.get(user_question)


def ask_user(optional):
    while True:
        user_question = input("Задайте вопрос:  ")
        option = get_options(user_question, optional)
        print(option)

        if user_question == "Мы можем прервать разговор?":
            break

if __name__ == "__main__":
    ask_user(options)

