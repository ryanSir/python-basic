def happy_birthday(name, age):
    print('祝' + name + '生日快乐')
    print(str(age) + '生日快乐')


# 调用
happy_birthday('kiven', 18)  # 按照顺序传参

happy_birthday(age=18, name='kiven')  # 关键字传参

