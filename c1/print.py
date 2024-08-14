# 普通输出案例
a = 100
b = 50
print(90)
print(a)
print(a * b)
print('北京')
print("北京")
print('''北京''')
print("""北京""")

# 不换行一次输出多个数据,seq:分隔符,end:结尾符号，默认是换行符'\n'
print(a, b, 'hello word!!!', sep='<>')  # def print(self, *args, sep=' ', end='\n', file=None)
print('北京', end='-->')
print('欢迎你')

print('北京' + '欢迎你')

# python 项目默认是用Unicode编码
print(ord('a'))  # 返回该字符在Unicode中的码点（整数表示）
print(chr(97))  # 返回该整数对应的Unicode字符。

print('a', 'b',sep='')
print('a' + 'b')
