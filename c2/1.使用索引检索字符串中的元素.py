# 正向递增索引
s = 'helloworld'
for i in range(0, len(s), 2):  # range(start, stop, step)
    if i == 9:
        print(i, s[i], sep=':', end='')
    else:
        print(i, s[i], sep=':', end=' --> ')

print("\n""------------")

# 反向递减
for i in range(-10, 0):
    print(i, s[i], end='\t\t')

for i in range(3):
    print(i)  # 0 1 2
