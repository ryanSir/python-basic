import random

list = [item for item in range(1, 11)]
print(list)

list2 = [item * item for item in range(1, 11)]
print(list2)

list3 = [random.randint(1, 100) for _ in range(1, 11)]
print(list3)

# 从列表中选择符合条件的元素
list4 = [i for i in range(1, 11) if i % 2 == 0]
print(list4)
