'''
定义一个学生类
'''


# 定义一个空类
class Student():
    pass


# 定义一个对象
jane = Student()


class PythonStudent():
    # 为不确定的值赋None
    name = None
    age = 18
    course = "Python"

    def doHomework(self):
        print("I am doing my homework")
        return None


# 实例化Lisa
lisa = PythonStudent()
print(lisa.name)
print(lisa.age)
lisa.doHomework()
