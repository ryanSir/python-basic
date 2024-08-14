# 大小写转换
s1 = "hello World"
new_s2 = s1.lower()
print(s1, new_s2)
new_s3 = s1.upper()
print(new_s3)

# 字符串的分割
email = 'ryan@163.com'
lst = email.split('@')
print('邮箱名：', lst[0], '邮件服务名：', lst[1])

# 统计次数
print(s1.count('o'))  # 统计o在字符串出现的次数
print(s1.count('z'))  # -1 没有找到

print(s1.index('o'))

# 判断前缀和后缀
print('demo.py'.endswith('py'))

print(s1.startswith('hello'))
