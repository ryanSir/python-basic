import re

pattern = r'\d\.\d+'  # + 限定符  \d 0-9 数字出现1次或者多次
s = 'I study Python 3.11 every day'
match = re.match(pattern, s, re.I)
print(match)
s2 = '3.11Python I study every day'
match = re.match(pattern, s2, re.I)
print(match)

print('匹配值的起始位置:', match.start())  # 匹配值的起始位置: 0
print('匹配值的结束位置:', match.end())  # 匹配值的结束位置: 4
print('匹配区间的位置元素:', match.span())  # 匹配区间的位置元素: (0, 4)
print('待匹配的字符串:', match.string)  # 待匹配的字符串: 3.11Python I study every day
print('匹配的数据:', match.group())  # 匹配的数据: 3.11


