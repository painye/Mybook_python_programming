"""
    person类的实现，包括数据、行为和运算符重载（未用于对象的持久存储
"""


class Person:
    """
    一般数据： 数据+逻辑
    """

    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return '<%s => %s: %s %s %s>' % (self.__class__.__name__, self.name, self.age, self.pay, self.job)


class Manager(Person):
    """
    带有自定义加薪的Person
    继承了lastName, str
    """

    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent+bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith', 44)
    sue = Person('Sue Jones', 47, 40000, 'hardware')
    tom = Manager('Tom Doe', 50, 50000)
    print(sue, sue.pay, sue.lastName())
    for obj in (bob, sue, tom):
        obj.giveRaise(0.1)
        print(obj)