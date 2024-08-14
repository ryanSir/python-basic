# {} 直接创建集合
s = {10, 20, 30}
print(s, type(s))

# 集合只能存储不可变数据类型
# s = {[10, 20], [30, 50]} # TypeError: unhashable type: 'list'

# 使用set()创建集合
s = set()  # 创建一个空集合，如果用s={},创建的是空字典

s = {}
print(s, type(s))  # dict

s = set("hello")
print(s)

s = set([10, 20, 30])
print(s, type(s))

s = set(range(1, 10))
print(s)

# 集合属序列的一种
print(max(s))
print(min(s))
print(len(s))

print(9 in s)
print(9 not in s)

# 集合的删除
del s
