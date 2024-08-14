s = 'helloworld'

# 切片操作 序列[start:end:step]
s1 = s[0:5:2]
print('\n' + s1)

# 省略开始位置,默认为0
s2 = s[:5:2]
print('\n' + s2)

# 省略步长 ,默认为1
s3 = s[:5:]
print('\n' + s3)

# 省略结束为止，默认到序列最后一个
s4 = s[::]
print('\n' + s4)

s5 = s[5:]  # 结尾默认，步长默认
print('\n' + s5)

s6 = s[::-1]  # 逆序输出
print('\n' + s6)

s7 = s[-1:-11:-1]
print('\n' + s7)
