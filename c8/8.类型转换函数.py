print('非空字符串的布尔值：', bool('hello'))
print('空字符串的布尔值：', bool(''))
print('空列表的布尔值：', bool([]))
print('空列表的布尔值：', bool(list()))
print('空元组的布尔值：', bool(()))
print('空元组的布尔值：', bool(tuple()))
print('空集合的布尔值：', bool(set()))
print('空字典的布尔值：', bool({}))
print('空字段的布尔值：', bool(dict()))

print('-' * 30)
print('非0整数的布尔值', bool(1223))
print('整数0的布尔值', bool(0))
print('浮点数0的布尔值', bool(0.0))

# 将其它类型转换成字符串类型
lst = [10, 20, 30]
print(type(lst), lst)

s = str(lst)
print(type(s), s)

# float 类型和 str 类型转成int类型
print('-' * 30, 'float类型和str类型转成int类型', '-' * 30)
print(int(98.7) + int('90'))

s = 'hello'
print(list(s))

seq = range(1, 10)
print(type(seq))
print(tuple(seq))
print(set(seq))
print(type(list(seq)), list(seq))
