class Person:
    def eat(self):
        print('人吃五谷杂粮')


class Cat:
    def eat(self):
        print('猫喜欢吃鱼')


class Dog:
    def eat(self):
        print('狗喜欢吃骨头')


# 这三个类中都有一个同名的方法，eat

# 编写函数
def fun(obj):  # obj 是函数的形式参数，在定义出并不知道这个形参的数据类型
    obj.eat()  # 通过变量obj调用eat方法


# 创建三个类的对象
per = Person()
cat = Cat()
dog = Dog()

# 调用fun函数
fun(per)
fun(cat)
fun(dog)
