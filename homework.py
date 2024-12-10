# 1 задание
film = {
    "название":"Одержимость",
    "год":"2014",
    "жанр":"триллер"
}
print(film["жанр"])
# задание 2

people = {}


for _ in range(3):
    name = (input("Введите имя:"))
    age = int(input("Введите возраст:"))
    people[name] = age


print(people)

# 3 задание
dict1 = {"информатика":5,
         "География":4,
         "Английский":4,
         "Математика":3


         }
print(len(dict1.values()))


# 4 задание
string1 = input("Введите текст:")
dict_str = string1.split()
print(len(dict_str))


