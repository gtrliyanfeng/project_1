# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 0028 17:02
# @Author  : Py_liyanfeng
# @Site    : 
# @File    : facetoobject.py
# @Software: PyCharm
'''
面向对象
'''
'''
1.定义：一切皆是对象
    基于面向对象设计一款英雄联盟，一个玩家选择一个英雄，每个英雄有自己的特征和技能
        特征：数据属性
        技能：方法属性
        （英雄 = 特征 + 技能）那么（对象 = 数据属性 + 方法属性）
        具有相似特征，相似技能的英雄属于同一类英雄（刺客类、射手类、战士类、辅助类、法师类、坦克类）
        那么，具有相似数据属性和方法属性的就是同一个类
    在python的面向对象那个中：
        特征==数据属性==用变量表示
        技能==方法属性==用函数表示
        类 = [变量与函数的集合体]
        对象 = [变量与方法的集合体]
    区分方法（method）和函数（function）:
        对于类来说，就是function
        对于对象来说，就是method(东西是一样的东西)
2.python中合并新式类和经典类（默认继承object）养成好习惯就算默认也要写上继承（object）
3.类的两种方法：
    1.属性引用：
    2.类的实例化

    
'''
# 3.1类的属性引用
# 定义盖伦类，不同的玩家实例出来的都是同一个盖伦（假设没有皮肤）
class Garen(object):
    # 所有玩家的盖伦都是一个阵营“德玛西亚”
    camp = "Demacia"
    # 盖伦具有平A的方法,攻击的时候需要传入一个敌人
    def attack(self,enemy):
        # 每一次平A敌人的生命值都会减去自己的攻击力值
        enemy.life_value -= self.aggressivity

# 数据属性引用，数据属性为类/实例对象共享 打印自己所处的阵营
print(Garen.camp)
# 类的函数属性引用，函数属性为类/是实例对象共享 打印函数属性
print(Garen.attack)
# 查看属性字典，或者说命名空间
print(Garen.__dict__)
'''
# 在类的外部也可以增加和删除属性
# 添加指向“Garen”属性
# Garen.name = "Garen"
# 添加指向“func函数”的属性
# def fun(self):
#   pass
# Garen.func = func
# 删除name属性
# del Garen.name
# 删除指向“func函数”的属性
# del Garen.func
# 删除已存在，而非添加的属性
# del Garen.attack
'''


# 类的实例化，变量=类名()，实例化自动调用__init__函数，可以用其来设置实例对象的初始参数
class Garen(object):
    camp = "Demacia"

    # 初始化盖伦  别名， 攻击力   初始是生命值
    def __init__(self, nickname, aggressivity=58, list_value=455):
        self.nickname = nickname
        self.aggressivity = aggressivity
        self.life_value = list_value

    def attalk(self, enemy):
        enemy.life_value -= self.aggressivity

# 实例化一个盖伦对象g1 出来，此时自动执行 Garen.__init__(g1,“大宝剑”)函数,然后自动执行函数内部的代码
g1= Garen("大宝剑")
# 打印g1这个对象
print(g1)
# g1 去引用g1对象的nickname属性（指向“大宝剑”）
print(g1.nickname)
"""
问题1：我们所定义的类属性到底储存在哪里？
    print(dir(类名)):可以查出一个名字列表,这是这个类的命名空间内的所有属性名（键）
    print(类名.__dict__):得到一个字典，这是命名空间内的属性名和对应的属性值
问题2：有些属性名增加前后双下划綫？
    类名.__name__     类的名字
    类名.__doc__      类的文档字符串
    类名.__base__     所继承的第一个父类
    类名.__bases__    继承所有父类所构成的元组
    类名.__dict__     类的字典属性
    类名.__module__   类定义所在的模块，如果在当前脚本就是__main__
    类名.__class__    实例所对应的类
"""

"""
4.对象的产生和引用
    4.1对象，类所产生的一个现实的例子（实力对象）
"""
# 让一个实际的参数去指向一个类（初始信息完整）就是实例化
g2 = Garen("二保健")
# type(对象)可以得到这个对象的类型<class'__main__.Garen'>
print(type(g2))
# 判断前面的对象是否是后面的类的实例
print(isinstance(g2, Garen))
'''
    4.2对象只能进行属性引用
        对象/实例--它本身其实只有数据属性
'''
# 对象g2引用nickname属性，指向“二保健”
print(g2.nickname)
# aggressivity属性指向58
print(g2.aggressivity)
# life_value属性指向455
print(g2.life_value)
print("=="*20)
'''
    4.2Python的class机制将类的函数绑定到对象上，被称作对象的方法
    而且这种绑定是唯一的，同一个类实例出来不同的对象，每个对象的方法都是不同的
    都具有自己独有的内存地址
        这种机制的特殊在于：实例对象去调用方法的时候，会吧自己作为第一个参数（self）
        传入进去（效果等同于ClassName.funcname(实例对象)）
'''
'''
5.每个对象都是独立存在的，但是通过某种机制可以将不同的对象联系起来
产生交互作用（互相引用）
'''
class Garen(object):
    camp = "Demacia"

    def __init__(self, nickname, aggressivity=58, life_value=455):
        self.nickname = nickname
        self.aggressivity = aggressivity
        self.life_value = life_value

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity


class Riven(object):
    camp = "Noxus"

    def __init__(self, nickname, aggressivity=54, life_value=414):
        self.nickname = nickname
        self.aggressivity = aggressivity
        self.life_value = life_value

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity

g1 = Garen("盖伦")
r1 = Riven("瑞文")
print(g1.life_value)
print(r1.attack(g1))
print(g1.life_value)
'''
得到：
    455
    None
    401
这里体现出了两个不同的类，实例化出两个不同的对象g1和r1的交互,改变了对方的数据属性
实现这个结果的途径是r1引用r1的attack方法，attack方法传入一个参数enemy（实例化的g1）
内部操作是g1（enemy）的lift_value属性减少了r1（self）的aggressivity属性所对应的值
-------------得出：对象之间的交互需要一个方法属性。这份方法属性得传入一个参数（parameter），这个参数
                    是想要被作用的对象，方法属性的内部就可以引用这个对象的属性(方法)，格式是
                    parameter.attributename
'''
"""
6.类的命名空间，实例对象的命名空间
    每当定义一个类的时候，就会划出一部分内存来储存这个类的属性：
            1.数据属性
            2.函数属性
        而且，这种属性是共享给实例对象的（共享非拷贝）
        虽然我们通过print(objectname.methodname)得到的结果不同
        但是并不代表他们的内存地址不同id(objectname.methodname)
    当我们print(objectname.methodname)的时候，会发现结果是类似于
    <bound method ClassName.methodname of <__main__.ClassName object at 0x000001B9C4647CC0>>
    从翻译上就可以直白看出  这是个绑定方法，ClassName的methodname这个方法被绑订到 0x000001B9C4647CC0 这个对象上了
    ==========================
    当我们执行r1.attack(g1)的时候其实是在执行Riven.attack(r1, g1)
    ==========================
    但是id(Riven.attack) != id(r1.attack)
    这说明类的方法虽然绑定到对象身上，但是不是直接指向，类有类的命名空间，对象
    有实例的命名空间：
        类的命名空间存放类的 属性
        实例的命名空间存放对象的属性
    当引用的时候索引指针会先从实例的名空间检索，无果后再去类的命名空间检索，无果后，继续向父类命名空间---
    找到后就引用，找不到就抛出异常AttributeError:属性错误
"""
