with open('referat.txt', 'r', encoding='utf-8') as myfile:
    content = myfile.read()
    words = content.split()
    print(f"Длина всей строки: {len(content)}")
    print(f"Количество слов: {len(words)}")
    replacement = content.replace('.', '!')
    new_file = open('referat2.txt', 'w', encoding='utf-8')
    new_file.write(replacement)


