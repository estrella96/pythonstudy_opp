# 属性案例
# Student 类
# name属性格式不统一

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.setName(name)

    def intro(self):
        print("hi,my name is {0}".format(self.name))

    def setName(self, name):
        self.name = name.upper()


s1 = Student("LIU YING", 19)
s2 = Student("jack jobs", 24)


# s1.intro()
# s2.intro()

# property 函数
# Person类 具有name age属性
# 输入的姓名大写保存
# 年龄 整数
# x=property(fget,fset,fdel,doc)
class Person():
    # 函数名称可以任意
    def fget(self):
        return self._name * 2

    def fset(self, name):
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget, fset, fdel, "对name的操作")

    def __call__(self, *args, **kwargs):
        print("我被调用了")

    def __str__(self):
        return "asdsff"


p1 = Person()
p1.name = "TuLing"
print(p1.name)

# __call__
t = Person()
t()
print(t)


# __getattr__
class A():
    name = "noname"
    age = 18

    def __getattr__(self, item):
        print("no found")
        print(item)


a = A()
print(a.name)
print(a.addr)


# __setattr__
class B():
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        print("设置属性：{0}".format(name))
        # 死循环 以下设置key的过程会自动调用__setattr__
        # self.key=value
        # 避免死循环 统一调用父类魔法函数
        super().__setattr__(name, value)


b = B()
b.age = 18


# 类和对象的三种方法
class Per():
    # 实例方法
    def eat(self):
        print(self)
        print("Eating")

    # 类方法
    @classmethod
    def play(cls):
        print(cls)
        print("Playing")

    # 静态方法
    @staticmethod
    def say():
        print("Saying")


yueyue = Per()
yueyue.eat()
Per.play()
yueyue.play()
Per.say()
yueyue.say()
