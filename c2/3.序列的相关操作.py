s = 'helloworld'
print('是否存在', 'e' in s)

print("不存在", 'v' in s)

# 内置函数的使用
print('len()', len(s))
print('max():', max(s))
print('min():', min(s))

# 序列对象的方法，使用序列的名称，打点调用
print('s.index():', s.index('o'))  # o 第一次出现位置

print('s.count():', s.count('o'))  # 统计个数
