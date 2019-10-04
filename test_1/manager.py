from person import Person

'''
    这是一个经理类，他与职员类的差别在工资的增长上略有不同，所以这里将他设置为一个新类继承员工类
    但需要特别修改他的工资增长函数
'''


class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1+percent+bonus)


if __name__ == '__main__':
    tom = Manager('Tom Foe', 50, 50000)
    print(tom.lastName())
    print(tom.pay)
    tom.giveRaise(.20)
    print(tom.pay)