list = [4, 56, 3, 78, 40, 56, 89]
print('原列表：', list)

# 排序，默认是升序,排序是在原列表上完成的，不会产生新的列表对象
list.sort()
print('升序：', list)

# 降序
list.sort(reverse=True)
print('降序', list)

list2 = sorted(list, reverse=True)
print("原列表：", list, id(list))
print("新列表", list2, id(list2))
