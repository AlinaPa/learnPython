def get_sum(num_one, num_two):
    try:
        les = int(num_one + num_two)
        print(les)
    except (ValueError, TypeError):
        print("Неверный тип даннных")


get_sum("a", "b")
get_sum("a", None)