# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 0029 14:30
# @Author  : Py_liyanfeng
# @Site    : 
# @File    : polymorphism.py
# @Software: PyCharm
"""
多态和多态性
"""
"""

1. 多态
    一类事物多种形态（一个抽象类有多种子类，所以的多态的实现，依赖于继承关系）
        例如：序列类型
            -str
            -list
            -tuple
            动物类型：
            -人
            -狗
            -猪
"""

import abc
# 定义动物类（抽象类）
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        pass

# 动物的人态
class People(Animal):
    def talk(self):
        print("hello people")

# 动物的狗态
class Dog(Animal):
    def talk(self):
        print("syy wangwang")

# 动物的猪态
class Pig(Animal):
    def talk(self):
        print("say aoao")



"""
2.多态性
    相同的函数名----定义不同的功能
    例如： 下课铃响了~~~
                老师----下班
                学生----放学
    
    静态多态性： 任何类型都可以使用+运算
    动态多态性：
"""

"""
同一个func函数，不同类型去调用，执行的结果大不相同
"""
# 相当于一个接口函数
def func_1(animal):
    animal.talk()

peo1 = People()
d1 = Dog()
pid1 = Pig()
func_1(peo1)
func_1(d1)
func_1(pid1)

"""
问题： 为什么要使用多态性？
        --增加程序灵活性，对象再是千变万化，使用者都是调用同一个接口
        --增加程序的可扩展性，创建另一个继承与Animal的新类，新类的对象
            也可以直接使用接口
"""
class Cat(Animal):
    def talk(self):
        print("say miao miao")

cat_1 = Cat()
func_1(cat_1)
