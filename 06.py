# 抽象类
class Animal():
    # 抽象方法
    def sayHello(self):
        pass


class Dog(Animal):
    def sayHello(self):
        print("闻一下")


class Person(Animal):
    def sayHello(self):
        print("kiss me")


# d=Dog()
# d.sayHello()
# p=Person()
# p.sayHello()

# 抽象类
import abc


# 抽象类声明
class Human(metaclass=abc.ABCMeta):
    # 抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 类抽象方法
    @abc.abstractclassmethod
    def drink(self):
        pass

    # 静态抽象方法
    @abc.abstractstaticmethod
    def play(self):
        pass


# 自定义类 函数名可以当做变量使用
from types import MethodType


class A():
    pass


def say(self):
    print("saying")


def talk(self):
    print("talking")


say(9)
# A.say=say
a = A()
a.say = MethodType(say, A)
a.say()
# 用type创建类
B = type("Aname", (object,), {"class_say": say, "class_talk": talk})
b = B()
b.class_say()


# 元类
# 写法固定 继承自type
class TulingMetaClass(type):
    # 注意以下写法
    def __new__(cls, *args, **kwargs):
        # 自己的业务处理
        print("hhhhhh")
        return type.__new__(cls, *args, **kwargs)


class Teacher(object, metaclass=TulingMetaClass):
    pass


t = Teacher()
t.__dict__
