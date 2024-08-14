from datetime import datetime
from datetime import timedelta

# 创建两个datatime 类型的对象
delta1 = datetime(2028, 10, 1) - datetime(2028, 5, 1)
print('数据类型', type(delta1))
print(delta1)

print(datetime(2028, 5, 1) + delta1)

# 通过传入参数的方式创建一个timedelta对象
td1 = timedelta(10)
print('创建一个10天的timedelta对象', td1)
td2 = timedelta(10, 29)
print('创建一个10天29秒的timedelta对象', td2)
