class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    # 使用@property修改方法，将方法转成属性使用
    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value != '男' and value != '女':
            print('性别有误')
            self.__gender = '男'
        else:
            self.__gender = value


stu = Student('ryan', '男')
print(stu.gender)

# 尝试修改属性值
stu.gender = '其他'
print(stu.gender)
stu.gender = '女'
print(stu.gender)
