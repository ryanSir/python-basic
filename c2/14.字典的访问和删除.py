d = {'hello': 10, 'world': 20, 'python': 30}

# 访问字典中的元素
# 1. 使用d[key]
print(d['hello'])

# 2. d.get(key)
print(d.get('hello'))

# 二者之间是有区别的，如果键不存在，d[key]会报错，d.get(key)可以指定默认值
print(d.get('hel', '不存在'))

# 字典的遍历
for item in d.items():
    print(item)  # 得到的是元组

# 在使用for循环，分别获取key和value
for key, value in d.items():
    print(key, value)
