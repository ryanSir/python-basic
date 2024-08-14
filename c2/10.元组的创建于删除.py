# 使用小括号创建元组
t = ('hello', [10, 20, 30], 'pyton3')
print(t)

# 使用内置函数tuple()创建元组
t = tuple('helloworld')
print(t)

t = tuple([10, 20, 30])
print(t)

print("存在：", 10 in t)
print("不存在", 9 in t)
print(max(t))
print(min(t))
print(len(t))
print(t.count(10))
print(t.index(10))

print(type(t))

# 如果只有一个元素,逗号不能省略
t = (10)
print(t, type(t))

t = (10,)
print(t, type(t))

# 元组的删除
del t
