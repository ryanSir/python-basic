d = {1001: '李梅', 1002: '王华', 1003: '张峰'}
print(d)

# 添加元素
d[1004] = '丽丽'
print(d)

# 获取字典中所有的key
keys = d.keys()
print(keys)
print(list(keys))
print(tuple(keys))

# 获取字典中所有的值
values = d.values();

# 将字典中的数据转换成key-value的形式，以元组的方式进行展现
lst = list(d.items())
print(lst)

d = dict(lst)
print(d)  # 又变成了字典类型

# 使用pop函数
print(d.pop(1001))
print(d)

# 删除一个不存在的值
print(d.pop(1008, '不存在'))

# 随机删除
print(d.popitem())
print(d)

# 清空所有元素
d.clear()
print(d)

# 空字典的布尔值为false
print(bool(d))
