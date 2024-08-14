# 个数可变的位置参数
def fun(*para):
    print(type(para))
    for item in para:
        print(item)


# 调用
fun(10, 20, 30, 40)
fun(10)
fun([10, 20, 30])  # 实际传递的是一个元素
fun(*[10, 20, 30])  # 加一颗星，会将列表进行解包


# 个数可变的关键字参数
def fun2(**kwpara):
    print(type(kwpara))
    for key, value in kwpara.items():
        print(key, '--->', value)


# 调用
fun2(name='kiven', age=18, height=170)

d = {'name': 'kiven', 'age': 18}
fun2(**d)
