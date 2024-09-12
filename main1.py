# from main2 import *


def check_your_age(Age):
    if Age <= 0:
        print("Вы ещё не родились")
    elif Age <= 6:
        print("Ты ещё ребенок")
    elif Age <= 13:
        print("Ты уже подросток")
    elif Age <= 18:
        print("Ты уже взрослый")
    elif Age <= 40:
        print("Ты уже старый")
    else:
        print("Пора на пенсию, старичок")
