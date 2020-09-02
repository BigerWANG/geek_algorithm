# coding: utf-8

"""


Python中的 元类
type是python中的元类
使用场景比较少
一般用来修改和拦截类的创建的
1，改变类的行为，（继承行为，封装行为，多态行为）
2，

"""



class Person:
    def __init__(self):
        self.ability = 1

    def eat(self):
        print("Eat", self.ability)


    def sleep(self):
        print("Sleep", self.ability)

    def save_life(self):
        print("+", self.ability, "s")



class Wang(Person):
    def eat(self):
        print("Eat", self.ability * 2)


class Zhang(Person):
    def sleep(self):
        print("Sleep", self.ability * 2)


class Jiang(Person):
    def save_life(self):
        print("+ inf s")



# 自定义一个元类
class Mixture(type):
    def __new__(cls, name, base, attr):
        # 元类接收的三个参数
        print(name)
        print(base)
        print(attr)
        p1, p2, p3 = base

        def eat(self):
            p1.eat(self)

        def sleep(self):
            p2.sleep(self)

        def save_life(self):
            p3.save_life(self)

        attr["eat"] = eat
        attr["sleep"] = sleep
        attr["save_life"] = save_life
        return type(name, base, attr)



class Hong(Wang, Zhang, Jiang, metaclass=Mixture):
    pass

def test(Person):
    Person.eat()
    Person.sleep()
    Person.save_life()









if __name__ == '__main__':
    test(Hong())




