lst = ['hello', 'world', 'python']

print('原列表：', lst, id(lst))

# 增加元素的操作 , 增加元素之后内存地址并没有改变
lst.append('sql')
print('增加元素之后：', lst, id(lst))

# 使用insert(index,x)在指定的index位置上插入元素x
lst.insert(1, 100)
print(lst)

# 列表元素的删除操作
lst.remove('world')
print(lst, id(lst))

# 使用pop(index)根据索引将元素取出，然后再删除
print(lst.pop(1))
print(lst)

# 清除列表中的所有元素
# lst.clear()
# print(lst, id(lst))

# 列表的反向
lst.reverse()
print(lst)

# 列表的拷贝，将产生一个新的列表对象
new_lst = lst.copy()
print(lst, id(lst))
print(new_lst, id(new_lst))

# 列表元素的修改
lst[1] = 'mysql'
print(lst)
