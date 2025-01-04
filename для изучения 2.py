#1 задание

Students = [("Student1", 90), ("Student2", 92),("Student3", 85), ("Student4", 99)]
print(sorted(Students, key= lambda x: x[1], reverse=True))
# 2 задание
tuple1 = (5,10,2,3,4)
tuple2 = (2,5,2,8,9,)
tuple3 = min(tuple1, tuple2)
print(tuple3)
from collections import Counter
# 3 задание
numbers1 = (1,2,4,3,2,3,5,6,7,8)
print(Counter(set(numbers1)))
# 4 задание
# 5 задание
tuple_num = (1,2,4,5,6)
square_numbers = [x * x for x in tuple_num]
print(square_numbers)
print(sum(square_numbers))

