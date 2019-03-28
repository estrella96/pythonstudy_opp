class A():
    name = "jane"
    age = 18

    def say(self):
        self.name = "bbbb"
        self.age = 30
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))

    def sayAgain(s):
        print("My name is {0}".format(s.name))
        print("My age is {0}".format(s.age))


lisa = A()
lisa.say()
lisa.sayAgain()


# #类实例的属性和对象的实例属性在不具体赋值的情况下指向同一个变量
#
# #A 类实例
# print(A.name)
# print(A.age)
# print("*"*20)
# print(id(A.name))
# print(id(A.age))
# print("*"*20)
# #a 对象
# a=A()
# print(a.name)
# print(a.age)
# print(id(a.name))
# print(id(a.age))

class Teacher():
    name = "ada"
    age = 34

    def say(self):
        self.name = "bbbb"
        self.age = 30
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))

    def sayAgain():  # 绑定类函数，使用类名调用
        # 调用类的成员变量
        print(__class__.name)
        print(__class__.age)
        print("Nice to see you")


t = Teacher()
t.say()
Teacher.sayAgain()


# 关于self的案例
class B():
    name = "qwer"
    age = 18

    def __init__(self):
        self.name = "aaaa"
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)


class C():
    name = "cccc"
    age = 90


a = B()
# 系统默认a是第一个参数
a.say()
# 此时self被a替换
B.say(a)
# B代表self
B.say(B)
# C代表self
B.say(C)
# 以上代表鸭子模型 不严格区分数据类型
