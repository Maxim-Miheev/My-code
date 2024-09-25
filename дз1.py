#задание 1
num1 = str(input("Введите первое число:"))
num2 = str(input("Введите второе число:"))
num3 = str(input("Введите третье число:"))
summa = str((num1+num2+num3))
print(summa)
# задание 2
number = input('Введите число: ')
count = 1
for i in number:
    count *= int(i)
print(count)
#задание 3
meters = int(input("Введите количество метров"))
santimetrs = meters * 100
dechimetrs = meters * 10
millimetrs = meters * 1000
mili = meters * 0.62
print("равно -",
      santimetrs,"сантиметров",'\n',
      dechimetrs, "дециметров", "\n",
      millimetrs, "миллиметров", "\n",
      mili, "милей")
#задание 4
razmer = int(input("Введите размер основания в виде целого числа"))
dlina_visoty = int(input("Введите высоту в виде числа"))
plochad_treygolnika = (0.5 * razmer * dlina_visoty)
print(plochad_treygolnika)
# задание 5
number = int(input("Введите четырехзначное число"))
number_as_str = str(number)
reversed_number = number_as_str[::-1] # с помощью среза меняем порядок чисел на зеркально противоположный
new_number = int(reversed_number)
print(new_number)