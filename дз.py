#задание 1
'''number = int(input("Введите число от 1 до 100:"))
if number < 0 or number > 100:
    print("Error")
elif number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 5 == 0:
    print("Buzz")
elif number % 3 == 0:
    print('Fizz')
else:
    print(number)
#задание 2
number1 = int(input("Введите число:"))
number2 = int(input("Выбери степень от 1 до 7:"))
if number2 == 1:
    print(number1 **1)
if number2 == 2:
    print(number1 **2)
if number2 == 3:
    print(number1 **3)
if number2 == 4:
    print(number1 **4)
if number2 == 5:
    print(number1 **5)
if number2 == 6:
    print(number1 **6)
if number2 == 7:
    print(number1 **7)'''
#задание 3
'''
mts = 10
tele2 = 20
megafon = 35
minutes = int(input("Введите количество минут"))
cost = int(input("Введите стоимость разговора за минуту: из предоставленных: "
                 "\n10 \n20 \n35\n:"))
if cost == 10:
    print("цена за минуту у мегафон")
if cost == 20:
    print('цена за минуту у теле2')
if cost == 35:
    print("цена за минуту у мегафон")
else:
    print("Вы ввели неправильную стоимость")
operator = input(str("Введите число оператора из предоставленных:"
                 " \nmts - 1 \ntele2 - 2 \nmegafon - 3 \n"))


if operator == 1:
    print(mts * minutes, "Цена за ", minutes,  "звонок")
elif operator == 2:
    print(tele2 * minutes, "Цена за ", minutes,  "звонок")
elif operator == 3:
    print(megafon * minutes, "Цена за ", minutes,  "звонок")
else:
    print("Вы ввели неправильное число")'''
# Я не смог понять почему пишется "Вы ввели неправильное число"
#задание 4

men_1 = int(input("Введите уровень продаж первого менеджера:"))
men_2 = int(input("Введите уровень продаж второго менеджера:"))
men_3 = int(input("Введите уровень продаж третьего менеджера:"))
sell = 100
sell1 = 100
sell2 = 100
if men_1 >= 500 and men_1 <= 1000:
    sell = 0.03 * men_1 + 200
if men_1 >= 1000 and men_1 <= 2500:
    sell = 0.05 * men_1 + 200
if men_1 >= 2500:
    sell = 0.08 * men_1 +200
if men_2 >= 500 and men_2 <= 1000:
    sell = 0.03 * men_2 + 200
if men_2 >= 1000 and men_2 <= 2500:
    sell = 0.05 * men_2 + 200
if men_2 >= 2500:
    sell = 0.08 * men_2 +200
if men_3 >= 500 and men_3 <= 1000:
    sell = 0.03 * men_3 + 200
if men_3 >= 1000 and men_3 <= 2500:
    sell = 0.05 * men_3 + 200
if men_3 >= 2500:
    sell = 0.08 * men_3 +200

if (men_1>men_2>men_3):
    sell = sell+ 200
if (men_2>men_3>men_1):
    sell1 = sell1 + 200
if (men_3>men_1>men_2):
    sell2 = sell2 + 200
print(sell)
print(sell1)
print(sell2)