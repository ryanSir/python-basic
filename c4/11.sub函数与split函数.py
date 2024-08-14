import re

pattern = '黑客|破解|反爬'
s = '我想学习Python，想破解一些VIP视频，Python可以实现无底线反爬吗?'
new_str = re.sub(pattern, 'xxx', s)
print(new_str)

s2 = 'https://www.baidu.com?wd=yyy'
pattern2 = '[.|?]'
lst = re.split(pattern2, s2)
print(lst)
