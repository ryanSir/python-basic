lst = [20, 3, 45]

# 排序
asc_lst = sorted(lst)  # 升序
desc_lst = sorted(sorted(lst), reverse=True)  # 降序

print(asc_lst)
print(desc_lst)

# reversed 反向
new_list = reversed(lst)
print(type(new_list))
print(list(new_list))

# zip
x = ['a', 'b', 'c']
y = [10, 20, 30]
zipopj = zip(x, y)

print(type(zipopj))
print(zipopj)
print(list(zipopj))

# enum
enum = enumerate(y, start=1)
print(type(enum))
print(tuple(enum))

# all
lst2 = [10, 20, '', 30]
print(all(lst2))

# any
print(any(lst2))

# next
s = ['a', 'b', 'c']
q = [10, 20, 30]
zipopj2 = zip(s, q)
print(next(zipopj2))
print(next(zipopj2))
print(next(zipopj2))


def fun(num):
    return num % 2 == 1


obj = filter(fun, range(1, 10))
print(list(obj))  # [1, 3, 5, 7, 9]


def upper(x):
    return x.upper()

new_list2 = ['hello']
obj2 = map(upper, new_list2)
print(list(obj2))
