s = 'Hello World'
# 字符串的替换
new_s = s.replace('o', '你好', 1)
print(new_s)

# 字符串在指定的宽度范围内居中
print(s.center(20))
print(s.center(20, '*'))

# 去掉字符串左右的空格
s2 = '    Hello   World    '
print(s2.strip())
print(s2.lstrip())  # 去掉字符串左侧的空格
print(s2.rstrip())  # 去掉字符串右侧的空格

# 去掉指定的字符
s3 = 'dl-Helloworld'
print(s3.strip('ld'))  # 与顺序无关
print(s3.lstrip('ld'))
print(s3.rstrip('ld'))
