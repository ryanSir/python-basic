s = 'helloworld'

s1 = s[0:5:2]  # 字符串切片[start:end:step] 起始索引为0，end不包含
print(s1)

s2 = '\n' + s1
print(s2)
s3 = r"'\n' + s1"  # 都不转义
print(s3)
