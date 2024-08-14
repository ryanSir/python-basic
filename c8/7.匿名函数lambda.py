# 匿名函数
s = lambda a, b: a + b

print(s(1, 2))

print('*' * 30)

list = [10, 20, 30]
for i in range(len(list)):
    print(list[i])

for i in range(len(list)):
    result = lambda x: x[i]
    print(result(list))

studen_scores = [
    {'name': 'kiven', 'score': 90},
    {'name': 'ryan', 'score': 99},
    {'name': 'sk', 'score': 98}
]

studen_scores.sort(key=lambda x: x.get('score'), reverse=True)
print(studen_scores)
