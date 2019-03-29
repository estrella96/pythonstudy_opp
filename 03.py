# 继承
# 任何一个类都有一个共同的父类 object
class Person():
    name = "Noname"
    age = 0
    __score = 0  # private
    _petname = "sec"  # protected

    def sleep(self):
        print("Sleeping...")


# 父类写在括号里
class Teacher(Person):
    teacher_id = "001"
    name = "jane"  # 优先使用子类

    def make_test(self):
        print("stttef")

    def sleep(self):
        # super().sleep()
        Person.sleep(self)
        self.make_test()


#
# t=Teacher()
# print(t.name)
# print(t._petname)
# # print(t.__score)
# t.sleep()
# print(Teacher.name)


# 构造函数

class Animal():
    pass


class PaxingAni(Animal):
    def __init__(self, name):
        print("Paxing Dongwu {0}".format(name))


class Dog(PaxingAni):
    # 构造函数 实例化时第一个被调用
    def __init__(self):
        print("I am init in dog")


class Cat(PaxingAni):
    # 没有构造函数找父类的
    pass


kaka = Dog()
c = Cat("cat")

print(type(super))
