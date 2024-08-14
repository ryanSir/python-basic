s = 'helloworld'
print('{0:*<20}'.format(s))  # 字符串的显示宽度为20，左对齐，空白部分使用*号填充
print('{0:*>20}'.format(s))

print('{0:*^20}'.format(s))
print(s.center(20, '*'))

# 千位分隔符(只适用于整数和浮点数)
print('{0:,}'.format(987654321))
print('{0:,}'.format(987654321.7865))

# 浮点数小数部分的精度
print('{0:.2f}'.format(3.132432342))

# 字符串类型，表示最大的显示长度
print('{0:.5}'.format('helloworld'))

