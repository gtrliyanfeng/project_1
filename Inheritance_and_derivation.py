# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 0028 21:15
# @Author  : Py_liyanfeng
# @Site    : 
# @File    : Inheritance_and_derivation.py
# @Software: PyCharm
'''
继承和派生
'''
'''
通过继承的方式创建新类可以减少一些不必要的重复
    创建的新类可以继承一个或者多个类
    被继承的类称为基类或者超类
    新创建的类称为派生类或子类
'''
'''
单继承和多继承
'''


class A(object):
    pass


class B(object):
    pass


# 单继承
class C(A):
    pass


# 多继承
class D(A, B):
    pass


'''
    可以通过subclass.__base__或者subclass.__bases__查看这个sunclass所继承的类
    如果没有填写所继承的类，那么这个类会自动继承object类，他是所有类的基类
'''
print(C.__base__)
print(D.__bases__)

'''
如何确定是否设置继承？
    继承和抽象的关系密不可分，
    抽象：我们可以将一些类的相似部分抽出来出来
    继承：将抽出来的东西定义成一个基类
    ---通过抽象---得到抽象的结果----将结果写成基类
'''
'''
还讨论英雄联盟，我们不管去创建Riven还是Garen这两个类，还是其他的英雄类
他们都少不了那几个属性那几个方法，都有血量，攻击力，普通攻击等等，然而，每创建一次
都需要重新写一遍，很麻烦，所以我们将其抽出（抽象）
抽出的结果定义成一个基类，那么我们的其他类去继承他
这就少了许多重复性的代码
'''


class Hero(object):
    def __init__(self, nickname, aggressivity, life_value):
        self.nickname = nickname
        self.aggressivity = aggressivity
        self.life_value = life_value

    def move_forword(self):
        print("%s向前移动" % self.nickname)

    def move_backward(self):
        print("%s向后移动" % self.nickname)

    def move_left(self):
        print("%s向左移动" % self.nickname)

    def move_right(self):
        print("%s向右移动" % self.nickname)

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity


class Garen(Hero):
    pass


class Riven(Hero):
    pass


g1 = Garen("大宝剑", 100, 1000)
r1 = Riven("社会文", 120, 800)
print(g1.nickname)
print(r1.life_value)
g1.attack(r1)
print(r1.life_value)
r1.move_left()
g1.move_backward()
'''
当对象去引用属性的时候，会从自己的命名空间内检索，检索不到就往类的命名空间
检索，发现还没有，就会向父类的命名空间检索，发现找到了，然后返回引用的结果
'''
'''
不仅仅可以继承，我们还能给自己，添加自己独有的属性
'''


class Noshou(Hero):
    # 添加自己的类属性
    camp = "Noxus"

    # 重写自己的attact
    def attack(self, enemy):
        enemy.life_value -= self.aggressivity
        print("我把你打出花了")

    # 给自己添加新的功能
    def defend(self):
        print("我格挡了你的攻击")


n1 = Noshou("砍死你", 100, 1200)
n1.attack(g1)
n1.defend()

'''
4.组合与重用性
    属性重用的方式不仅仅是继承一个，另一个就是组合
    组合：在一个类中，以另一个类的对象作为数据属性，将其组合到这个类中
    
'''


# 定义武器装备类
class Equip(object):
    def fire(self):
        print("释放技能")


class Zhaoxin(object):
    camp = "Demacia"

    def __init__(self, nickname):
        self.nickname = nickname
        # 产生一个Equip的对象，将其赋值给实例对象一个equip属性
        self.equip = Equip()


z1 = Zhaoxin("菊花王者")
print(z1.nickname)
# 这样z1就能直接引用Equip类中的属性了
z1.equip.fire()
"""
继承也好，还是组合也好，两个途径都可以有效的共享已有类的资源，但是二者的概念和使用场景都不同
    1.继承方式
    继承是一种类和类之间的关系，，如果两个甚至多个类具有很多相似的地方，使用继承可以使编程简单化
    突出“是”的关系，，，白马，是马。教授是老师，老师是人，学生也是人
    
"""


class Teacher(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def say(self):
        print("hello")


class Professor(Teacher):
    pass


p1 = Professor("高智商", "男")
print(p1.name)
p1.say()

'''
    2.组合方式
    组合是类与类之间的另一种关系，它主要体现的是“有”,当某些类之间只有
    少部分不同的时候，可以使用这种方式（相当于个管道，接通两者关系）
    教授有生日，教授开设python课程
'''


class Birthday(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class Couse(object):
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period


# class Professor(Teacher):
#     def __init__(self, name, sex):
#         super().__init__(name, sex)
#         self.birth = Birthday('1996', '02', '18')
#         self.course = Couse("Python", "19800", "bjm13")


class Professor(Teacher):
    def __init__(self, name, sex, birth, couse):
        super().__init__(name, sex)
        self.birth = birth
        self.course = couse


p2 = Professor("高智商", "男", Birthday('1996', '02', '18'), Couse("Python", "19800", "bjm13"))
print(p2.name)
print(p2.birth.year)
print(p2.course.period)

'''
5.接口和归一化的设计
    接口：某些方法特征的合集，对各个基类的再次抽象
    继承有两种用途：
        1.继承基类的属性，并作出自己的改变或者扩展（重写和扩展）
        2.声明某个派生类兼容与某个基类，定义一个接口类（Interface），接口中定义了一些
            接口名（就是函数名），但是没实现接口的功能（直接pass）类比于object中的好多
            函数都是只有名字没有功能的，直接pass，而继承与这个接口类的派生类，实现了接口
            中的函数的功能
'''


# 定义一个接口（python中没有直接定义接口的关键字，----qaq）
class Interface:
    def read(self):
        pass

    def write(self):
        pass


class Txt(Interface):
    def read(self):
        print("文本数据的读取方法")

    def write(self):
        print("文本数据的写入方法")


class Sata(Interface):
    def read(self):
        print("硬盘数据的读取方法")

    def write(self):
        print("硬盘数据的写入方法")


"""
    在实践中，使用直接继承的方法意义不是很大，甚至会出现危险
    因为，它使得派生类和基类之间产生极强的耦合
    通过接口继承的方式，作出了更实质性的抽象，这个抽象规定了一个兼容的
    接口，是外部调用者无需关心具体的细节，可以一视同仁的处理实现了特定接口的所有对象
    -----称为归一化
    归一化---使得高层的外部调用者可以不加区分的处理所有接口兼容的对象集合
    ----好比Linux的泛文件概念一样，所有的东西都可以当做文件处理，不用关心
    他是内存、磁盘、网络、屏幕。
    
"""

'''
问题： 为什么要使用接口？
    ---
    ---接口提取以个类群（好多类）---的函数名，封装但不去实现
    继承他的子类去实现接口中的函数，目的就是为了归一化

问题：  什么是归一化？
    ---只要是基于同一个接口实现的类，那么所有的这些类的实例化对象自使用时，用法上来说是一样的
    ---归一化让使用者无需关心对象的类是什么， 只需要知道这些对象都具有什么功能，降低了使用者的难度
    
例如： 
    ---定义一个动物接口，结构定义了  跑， 吃， 呼吸， 等接口函数名
    ---定义了一个老鼠类，去实现了这个接口内部的方法
    ---定义了松鼠类实现了接口内部的方法
    ---现在分别实例化一个老鼠和一个松鼠到你的面前
    ---就算分不出他们那个是哪个，但是我只需要知道他们会跑会吃会呼吸就可以了
    
例如：
    ---我们有一个汽车接口，里面定义了汽车所有的功能，然后由本田汽车的类，奥迪汽车的类，大众汽车的类，
    ---他们都实现了汽车接口，这样就好办了，大家只需要学会了怎么开汽车，那么无论是本田，还是奥迪，
    ---还是大众我们都会开了，开的时候根本无需关心我开的是哪一类车，操作手法（函数调用）都一样。
'''
'''
6.抽象类：
    这种类只能被继承，不能被实例
    
问题： 为什么要有抽象类？
    同样是从多个类中再抽出相同的成分，但还与接口不同
    现实对象--->类--->抽象类
    抽象类 归根到底还是类，有数据属性和函数属性，而接口类只有函数属性
    抽象类的子类必须定义抽象类的函数，（不一定实现，但是必须定义）
'''
import abc


class All_file(metaclass=abc.ABCMeta):
    all_type = "file"

    # 定义抽象方法，无需实现功能,
    @abc.abstractmethod
    def read(self):  # 这些功能在子类中必须实现，否则会报错
        pass

    @abc.abstractmethod
    def write(self):
        pass


class Txt(All_file):
    def read(self):
        print("文本数据读取方法")

    def write(self):
        print("文本数据写入方法")


class Exe(All_file):
    def read(self):
        print("exe数据读取方法")

    def write(self):
        print("exe数据写入方法")


wenben = Txt()
exe_f = Exe()
print(wenben.all_type)
print(exe_f.all_type)
exe_f.read()

"""
7.继承的顺序
"""


class A(object):
    def test(self):
        print("from A")


class B(A):
    def test(self):
        print("from B")


class C(A):
    def test(self):
        print("from C")


class D(B):
    def test(self):
        print("from D")


class E(C):
    def test(self):
        print("form E")


class F(D, E):
    def test(self):
        print("from F")

    pass


f1 = F()
f1.test()
print(F.__mro__)
"""
新式类:F---D---B---E---C---A
经典类:F---D---B---A---E---C
"""
"""
继承的原理：
    C3线性算法，合并父类的所有MRO列表
    准则为：
        1.子类先于父类被检索
        2.多个父类会根据他们在列表中的顺序被检索
        3.如果对下一个类存在两个合法的选择，选择第一个父类
"""

"""
问题： 子类如何准确调用父类中的方法？
    1.父类名.父类方法名（）
"""


# 定义交通工具类
class Vehicle(object):
    Country = "China"

    def __init__(self, name, speed, load, power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print("开动了~~~~~")


class Subway(Vehicle):

    def __init__(self, name, speed, load, power, line):
        Vehicle.__init__(self, name, speed, load, power)
        self.line = line

    def run(self):
        print("地铁%s号线欢迎您"%self.line)
        Vehicle.run(self)

line13 = Subway("北京地铁", "180m/s", "1000人/箱", "电", 13)
print(line13.speed)
line13.run()

"""
 2.使用super()
"""
class Mobick(Vehicle):

    def __init__(self, name, speed, load, power, num):
        super().__init__(name, speed, load, power)
        self.num = num

    def run(self):
        print("摩拜单车%s号欢迎您的使用，祝您一路顺风"%self.num)
        super().run()


mobike2 = Mobick("摩拜单车", "20m/s", "1人", "人力", 2)
print(mobike2.name)
mobike2.run()
"""
注意：
    当使用super的时候， Python就会在Mor列表中继续向上一个类检索.只要每个重定义的方法同一使用
    super并且只调用它一次，那么控制流最终会便利完整个MOR列表，每一个方法也只会被调用一次
    
    使用super调用的所有属性，都是从rom类表的当前位置向后找的，千万不要通过看代码找继承关系，一定
    要看ROm表
"""
print(Mobick.__mro__)

