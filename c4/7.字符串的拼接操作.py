s1 = 'hello'
s2 = 'world'

# 使用+号进行拼接
print(s1 + s2)

# 使用字符串的join
print(''.join([s1, s2]))
print('*'.join([s1, s2]))

# 直接拼接
print('hello''world')

# 使用格式化字符串进行拼接
print('%s%s' % (s1, s2))
print(f'{s1}{s2}')
print('{0}{1}'.format(s1, s2))
