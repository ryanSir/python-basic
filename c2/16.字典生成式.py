import random

d = {item: random.randint(1, 10) for item in range(4)}
print(d)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
d = {key: value for key, value in zip(list1, list2)}
print(d)
