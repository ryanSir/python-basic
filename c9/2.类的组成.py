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

    # 静态方法
    @staticmethod
    def sm():
        print('这是一个静态方法，不能调用实例属性和实例方法')

    # 类方法
    @classmethod
    def cm(cls):  # cls 是class的简写
        print('这是一个类方法，不能调用实例属性和实例方法')


# 创建类的对象
stu = Student('ysj', 18)  # 为什么传了两个参数，因为__init__方法中，有两个形参，self，是自带的参数，无需手动传入

# 1.实例属性，使用对象名进行打点调用的
print(stu.name, stu.age)

# 2.类属性，直接使用类名，调用
print(Student.school)

# 3.实例方法，使用对象名进行调用
stu.show()

# 4.类方法，@classmethod进行修饰的方法，直接使用类名调用
Student.cm()

# 5.静态方法，@staticmethod进行修饰的方法，直接使用类名调用
Student.sm()
