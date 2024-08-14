list = [
    ['城市', '环比', '同比'],
    ['北京', 102, 103],
    ['上海', 104, 504],
    ['深圳', 100, 39]
]

print(list)

for row in list:  # 行
    for item in row:  # 列
        print(item, end="\t")
    print()

# 生成一个四行五列的二维列表
list2 = [[j for j in range(5)] for i in range(4)]
print(list2)
