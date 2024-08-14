class Person:  # 默认继承了Object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好，我叫:{self.name},{self.age}岁')


class Student(Person):
    def __init__(self, name, age, stuno):
        super().__init__(name, age)
        self.stuno = stuno

    def show(self):
        # 调用父类中的方法
        super().show()
        print(f'学号：{self.stuno}')


class Doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department


stu = Student('Ryan', 30, '1001')
stu.show()

doctor = Doctor('Kiven', 29, '外科')
doctor.show()
