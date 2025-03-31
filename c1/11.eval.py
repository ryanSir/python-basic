s = '3.14+3'
print('s的数据类型', type(s))

x = eval(s)  # eval 函数去掉左右两侧的引号
print('x的数据类型', type(x))

# 经常和input函数使用
age = eval(input('请输入你的年龄：'))  # 将字符串类型转换成int类型 ，相当于 int(age)

print('我的年龄是:', age, '数据类型是:', type(age))

hello = '北京'
print(hello)
print(eval('hello'))  # 输出了北京，去掉了引号，相当于获取了hello变量的值