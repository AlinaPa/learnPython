list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in list:
    print(number+1)

print("____________________________________________")

''' Второе задание (цикл) '''
string = 'weather'

for letters in string:
    print(letters)

print("____________________________________________")

''' Третье задание (оценки) '''
one = [{'school_class': '4a', 'scores': [4, 5, 4, 5, 4]},
       {'school_class': '7б', 'scores': [2, 5, 5, 4, 3]},
       {'school_class': '9в', 'scores': [5, 5, 5, 5, 5]}]

a_scores = int(sum(one[0]['scores'])/5)
b_scores = int(sum(one[1]['scores'])/5)
c_scores = int(sum(one[2]['scores'])/5)

full_scores = int(((sum(one[0]['scores'])/5) + (sum(one[1]['scores'])/5) + (sum(one[2]['scores'])/5)) / 3)

print(f"Средний балл по школе: {full_scores}")
print(f"Средний балл по 4а классу: {a_scores}")
print(f"Средний балл по 7б классу: {b_scores}")
print(f"Средний балл по 9в классу: {c_scores}")
