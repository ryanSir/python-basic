import re

pattern = r'\d\.\d+'
s = 'I study Python3.11 every day Python3.8 I love you'
match = re.search(pattern, s)
print(match)

print(match.group())


lst = re.findall(pattern,s)
print(lst)


