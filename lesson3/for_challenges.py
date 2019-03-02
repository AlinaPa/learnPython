# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(''.join(list(map(str, name))))

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(''.join(list(map(str, name))), len(name))


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика
is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}

for name, gender in is_male.items():
    if gender is True:
        print(''.join(list(map(str, name))), "Мужской")
    else:
        print(''.join(list(map(str, name))), "Женский")


# Задание 4
# Даны группы учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
print(f"Всего {len(groups)} группы.")
print(f"В первой группе {len(groups[0])} ученика.")
print(f"Во второй группе {len(groups[1])} ученика.")


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
print(f"Группа 1: {groups[0]}")
print(f"Группа 2: {groups[1]} ")
