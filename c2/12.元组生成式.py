t = (i for i in range(1, 4))
print(t)
# t = tuple(t)  # 需要把对象转换一下
# print(t)

# for i in range(len(t)):
#     print(t[i])

print(t.__next__())
print(t.__next__())
print(t.__next__())
