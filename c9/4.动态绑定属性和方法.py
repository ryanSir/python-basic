class Student:
    # 类属性：定义在类中，方法外的变量
    school = '北京大学'

    # 初始化方法
    def __init__(self, name, age):  # name,age 是局部变量，方法的参数, name，age的作用与是整个__init__方法
        self.name = name  # 左侧是实例属性，name是局部变量，将局部变量的值赋值给实例属性
        self.age = age  # 实例名称和局部变量的名称可以相同

    # 定义在类中的函数，成为方法，自带一个参数self
    def show(self):
        print(f'我叫：{self.name},今年:{self.age}')  # 实例属性可以在整个方法中使用


stu = Student('ryan', 30)
stu2 = Student('陈妹妹', 20)

# 动态绑定实例属性
stu2.gender = '男'
print(stu2.gender)


# 动态绑定方法
def introduce():
    print('我是一个普通的函数,我被动态绑定了stu2对象的方法')

stu2.fun = introduce  # 函数的赋值，不能加小括号
stu2.fun()
