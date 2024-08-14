class Student:
    # 首尾双下划线
    def __init__(self, name, age, gender):
        self._name = name  # self._name 受保护的，只能本类或子类访问
        self.__age = age  # self.__age 表示私有的，只能类本身访问
        self.gender = gender  # 普通的实例属性,类的内部，外部，及子类都可以访问

    def _fun(self):  # 受保护的方法
        print('子类及本身可以访问')

    def __fun2(self):  # 私有方法
        print('只有定义的类可以访问')

    def show(self):
        self._fun()  # 类本身访问受保护的方法
        self.__fun2()
        self._name
        self.__age


stu = Student('陈妹妹', 20, '女')
print(stu._name)
# print(stu.__age)  # 报错，私有属性

stu._fun()
# stu.__fun()

print(stu._Student__age)
stu._Student__fun2()

print(dir(stu))
