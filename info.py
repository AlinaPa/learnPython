first_name = 'Алина'
second_name = 'Пахомова'
print(first_name, second_name)

list = [3, 5, 7, 9, 10.5]
print(list)
list.append('Python')
print(len(list))

print(list[0])
print(list[-1])
print(list[2:4])
list.remove('Python')
print(list)


dict = {"city": "Москва", "temperature": "20"}
print(dict.get("city"))
dict["temperature"] = int(dict["temperature"]) - 5
print(dict)

print(dict.get("country"))
print(dict.get("country", "Россия"))
dict["date"] = "27.05.2019"
print(len(dict))












