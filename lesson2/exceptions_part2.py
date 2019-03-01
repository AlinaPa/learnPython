def get_sum(num_one, num_two):
    try:
        les = int(num_one + num_two)
        print(les)
    except ValueError:
        print("Неверный тип даннных")


get_sum("a", "b")
