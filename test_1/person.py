class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    # __str__方法允许直接打印出实例，而不用打印他的特定属性，返回一个字符串
    def __str__(self):
        # __class__方法指向实例化对象的类
        return '<%s=>%s>' % (self.__class__.__name__, self.name)

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0+percent)


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    print(bob.name, sue.pay)

    print(bob.lastName())
    sue.giveRaise(.10)
    print(sue.pay)

    print(sue)