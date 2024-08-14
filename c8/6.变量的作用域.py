def cal(a, b):
    s = a + b
    return s

    # print(a, b, s)  # a,b 函数的参数，参数是局部变量，s是函数中定义的变量，也是局部变量


result = cal(10, 20)
print(result)

a = 100  # 全局变量


def cal2(a, b):
    global s  # global声明的变量是全局变量
    s = 300  # 声明和复制必须分开执行
    return a + b + s


print(cal2(10, 20))
print(s)   # 运行不会报错
