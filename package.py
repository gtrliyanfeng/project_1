# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 0029 14:53
# @Author  : Py_liyanfeng
# @Site    : 
# @File    : package.py
# @Software: PyCharm
"""
封装
"""
"""
1.封装的定义
    将抽象得到的数据和函数相结合，形成一个整体（类）
    目的：
        增强安全；简化编程
        安全：使用者的调用只通过接口，增加接口公开与非公开权限
        简化：使用者不必知道内部细节如何实现
        保护隐私，隔离复杂
        
2，封装的层面
    第一层面：（什么都不做）
        -定义一个类，实例一个对象的过程中都会自动创建他们的命名空间
        ---只能用 类名.属性名（实例对象），实例对象.属性名（）的途径去访问
        ---这样对类内部的数据或者函数来说，本身就是一种封装，
        ---而想要访问内部属性都需要通过类名、实例对象名这两个（接口）才能访问
    第二层面：（双前下划线隐藏）
        ---这种方式只能在类的内部访问
        ---外部只能通过内部定义的接口访问，或者特殊的方法访问
        ---  _ClassName__methodname
        注意：
            ---子类中的__xxx并不覆盖父类的__xxx,两者变形之后的结果不同
            ---只要知道了类名，也能直接在外部访问内部隐藏数据
            ---在继承中，如果父类不想子类覆盖自己的属性，可以将属性名私有了
3.特性
    @property  将函数属性当做数据属性来用
            
"""
"""
@property
"""
import math
class Circle(object):
    # 初始化圆的半径
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        # 返回圆的面积
        return math.pi*self.radius**2

    @property
    def perimeter(self):
        # 返回圆的周长
        return 2*math.pi*self.radius

circ1 = Circle(10)
print(circ1.area)
print(circ1.perimeter)
# circ1.area = 3

"""
问题： 为甚么要使用特性？
    ---使用特性后，统一了访问的方式，就怕有些客户不想xxx.xxx()
    ---都改成xxx.xxx一劳永逸（只针对不用传参的方法）
"""
"""
面向对象的封装方式有三种：
    1.public----对要公开（不做任何操作）
    2.protected---不对外公开，但对friend或者子类公开
    3.private---对谁都不公开
然而Python并没将三种方式内建到自己的class机制中
但是我们可以同过property去实现这种机制
"""
class Foo(object):
    def __init__(self, val):
        self.__name = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # 检查传入的数据类型
        if not isinstance(value, str):
            raise TypeError("%s 必须是字符串类型"%value)
        self.__name = value

    @name.deleter
    def name(self):
        raise TypeError("不可被删除")

foo = Foo("张三")
print(foo.name)
# foo.name = "lisi"
# del foo.name

"""
一种property的古老用法：通过将属性名实例化为property的一个对象来实现
                     这种方式明显没有装饰器的方式可读性强
"""
class Foo(object):
    def __init__(self, val):
        self.__name = val

    def getname(self):
        return self.__name

    def setname(self, value):
        if not isinstance(value, str):
            raise TypeError("%s必须是字符串类型"%value)
        self.__name = value

    def delname(self):
        raise TypeError("不可被删除")

    name = property(getname, setname, delname)

"""
4.封装与扩展性
    因为通过封装：
                ---程序员可以修改封装内部的数据不对外部造成影响
                ---客户端只需要知道接口就可以使用内部的功能
"""
# 类的设计者（程序员）
class Room(object):
    def __init__(self, name, ower, width, length, high):
        self.name = name
        self.ower = ower
        self.__width = width
        self.__length = length
        self.__high = high

    # 定义对外提供的接口，隐藏内部实现的细节，此时我们想去求房子的面积
    def tall_area(self):
        return self.__width * self.__length



# 用户
r1 = Room("厕所", "高智商", 20, 20, 20)
print(r1.tall_area())

# 如果想计算体积，而不需要面积
class Room(object):
    def __init__(self, name, ower, width, length, high):
        self.name = name
        self.ower = ower
        self.__width = width
        self.__length = length
        self.__high = high

    # 还是原来的接口，只需要修改内部的某些代码就能实现，而且用户还是调用原来的接口不变，但是功能变了
    def tall_area(self):
        return self.__length * self.__width * self.__high

r1 = Room("厕所", "高智商", 20, 20, 20)
print(r1.tall_area())