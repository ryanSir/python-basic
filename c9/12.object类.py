class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好：我叫${self.name},今年${self.age}')

    # 重写object __str__方法
    def __str__(self):
        return '这是一个人类，具有name和age两个属性'


per = Person('Ryan', 20)

print(dir(per))
print(per)
