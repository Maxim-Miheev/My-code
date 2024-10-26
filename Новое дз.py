# 1.  задание вывести x в степени y
x= int(input("Введите первое целое число:"))
y = int(input("Введите второе целое число:"))
print(x ** y)
# 2.
count = 0
for i in range(100, 1000):
    num = str(i)
    if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]:
        count += 1
print(count)
# 3
count1=0
count2=0
for a in range(100,9999):
    n1=(a//1000)
    n2=(a//100)%10
    n3=(a%10)//10
    n4=a%10
    if a <=1000:
        (n2!=n3 or n2!=n4 or n3!=n4)
        count1 += 1
    if a >=1000:
        (n1!=n2 or n1!=n3 or n1!=n4 or n2!=n3 or n2!=n4 or n3!=n4)
        count2 += 1
print("Количество разных целых чисел в диапазоне от 100 до 9999:",count1+count2 )
# задание 4
n = int(input('n = '))
arr = []
while n > 0:
    n, k = divmod(n, 10)
    if k not in (3, 6):
        arr.append(k)
x = 0
for i, v in enumerate(arr):
    x += v * 10 ** i
print(x)

