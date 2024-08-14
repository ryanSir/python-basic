# 直接使用[]创建列表
lst = ['hello', 'world', 98, 100.5]
print(lst)

# 可以使用内置函数创建列表
list2 = list('helloworld')
print(list2)

list3 = list(range(1, 10, 2))  # 从1开始，到10结束，步长为2，不包含10
print(list3)

print(lst + list2 + list3)  # 序列的相加操作

print(lst * 3)
print(len(lst))
print(max(list2))
print(min(list2))
print(list2.count('o'))  # 查看o出现的次数
print(list2.index('o'))  # 查看o第一次出现的次数

# 列表的删除操作
list4 = [10, 20, 30]
del list4
print(list4)  # 此时会报错，list4已经不存在
