with open('referat.txt', 'r', encoding='utf-8') as myfile:
    content = myfile.read()
words = content.split()
print(f"Длина всей строки: {len(content)}")
print(f"Количество слов: {len(words)}")
replacement = content.replace('.', '!')
with open('referat2.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(replacement)
