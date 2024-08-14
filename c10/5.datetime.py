from datetime import datetime  # 从datatime 模块中导入datetime类

dt = datetime.now()
print('当前系统时间：', dt)

# datatime 是一个类，手动创建
dt2 = datetime(2028, 8, 8, 20, 7)
print('dt2的数据类型：', type(dt2), '所表示的时间日期：', dt2)
print('年:', dt2.year, '月:', dt2.month, '日:', dt2.day)
print('时:', dt2.hour, '分:', dt2.minute, '秒:', dt2.second)

# 比较两个datatime 类型对象的大小
labor_day = datetime(2028, 5, 1, 0, 0, 0)
national_day = datetime(2028, 10, 1, 0, 0, 0)
print(labor_day < national_day)

# datatime 类型与字符串进行转换
nowdt = datetime.now()
nowdt_str = nowdt.strftime('%Y-%m-%d %H:%M:%S')
print(nowdt_str)

# 字符串类型转成datetime 类型
str_datetime = '2024年8月2日 10点8分20秒'
dt3 = datetime.strptime(str_datetime,'%Y年%m月%d日 %H点%M分%S秒')
print(dt3)
