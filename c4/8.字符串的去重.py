s = 'helloworldhelloworld'

# 字符串拼接及not in
new_s = ''
for item in s:
    if item not in new_s:
        new_s += item
print(new_s)

# 使用索引 + not in
new_s2 = ''
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2 += s[i]
print(new_s2)

# 通过集合去重 + 列表的排序操作
new_s3 = set(s)
lst = list(new_s3)
lst.sort(key=s.index)
print(''.join(lst))
