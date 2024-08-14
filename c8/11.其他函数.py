# format
print(format(3.14, '20'))  # 数值类型默认右对齐
print(format('hello', '20'))  # 字符串默认左对齐
print(format('hello', '*<20'))  # < 左对齐，* 代表填充符
print(format('hello', '*>20'))
print(format('hello', '*^20'))

print(eval('10+20'))  # 去掉左右的符号
