class MyClass:
    class_attribute = 0

    def __init__(self, value):
        self.instance_attribute = value

    @classmethod
    def class_method(cls, value):
        print(f"Accessing class attribute: {cls.class_attribute}")
        return cls(value)


# 使用类方法来创建类的实例
obj = MyClass.class_method(10)
print(obj.instance_attribute)  # 输出: 10

class MyClass:
    @staticmethod
    def static_method(value):
        print(f"Static method called with value: {value}")


# 直接通过类名调用静态方法
MyClass.static_method(10)