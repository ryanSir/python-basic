def happy_birthday(name='k', age=16):
    print('祝' + name + '生日快乐')
    print(str(age) + '生日快乐')


happy_birthday()  # 不用传参 ，使用默认值

happy_birthday('s')  # 位置传参

happy_birthday(age=19)  # 关键字传参


def fun(a, b=20):   # 当位置参数和关键字参数同时存在的时候，要遵循位置参数再签，关键字参数在后
    pass


# def fun2(a=20, b):  # 报错了，语法错误，当位置参数和关键字参数同时存在的时候，位置参数在后会被报错
#     pass
