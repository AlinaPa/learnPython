# Вывести последнюю букву в слове
word = 'Архангельск'
print(f"Последняя буква: {word[-1]}")


# Вывести количество букв в слове
word = 'Архангельск'
print(f"Количество букв: {len(word)}")


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = set("ёуеыаоэяиюЁУЕЫАОЭЯИЮ")
print(f"Количество гласных букв: {sum(letter in vowels for letter in word)}")


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f"Количество слов в предложении: {len(sentence.split())}")


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence2 = sentence.split()
for letters in sentence2:
    print(letters[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
length = sentence.split()
average_length = int((len(length[0])/2) + (len(length[1])/8) + (len(length[2])/1) + (len(length[3])/5) / 4)
print(f"Средняя длина каждого слова из предложения: {average_length}")
