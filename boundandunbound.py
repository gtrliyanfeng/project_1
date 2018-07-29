# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 0029 16:10
# @Author  : Py_liyanfeng
# @Site    : 
# @File    : boundandunbound.py
# @Software: PyCharm
"""
绑定以非绑定方法
"""
"""
1.定义
    类的函数属性分为两类：
        1.绑定方法（绑定给谁，谁来调用就将自己作为第一个参数传入）
            1.类的绑定方法（classmethod装饰器）就是为类量身定制（cls）
                --ClassName.bound_method() 类（类实例的对象）去
                --调用这个方法的时候，就会将类（对象所属的类）作为第一
                --参数传入
                
            2.实例对象的绑定方法，不需要任何装饰器修饰，直接def定义（self）
                --实例对象.bund_method() 自动将实例对象作为第一个参数传入
                --属于类的函数吗、实例的绑定方法，类也可以使用，但是得手动传入
                --实例对象
        2.非绑定方法（使用staticmethod装饰过的方法）
            不与类或者实例所绑定，也没自动传值这么一说，就是一个普通函数
"""
import hashlib
import time
class MySQL:
    def __init__(self, host, port):
        self.i = self.create_id()
        self.host = host
        self.port = port

    @staticmethod
    def create_id():  # 就是一个普通工具
        m = hashlib.md5(str(time.clock()).encode('utf-8'))
        return m.hexdigest()


print(MySQL.create_id)  # <function MySQL.create_id at 0x0000000001E6B9D8> #查看结果为普通函数
conn = MySQL('127.0.0.1', 3306)
print(conn.create_id)  # <function MySQL.create_id at 0x00000000026FB9D8> #查看结果为普通函数

"""
@ classmethod
"""
# from knowledge.settings import *
# import hashlib
# import time
# class MySQL:
#     def __init__(self,host,port):
#         self.host=host
#         self.port=port
#
#     @classmethod
#     def from_conf(cls):
#         print(cls)
#         return cls(settings.HOST,settings.PORT)
#
# print(MySQL.from_conf) #<bound method MySQL.from_conf of <class '__main__.MySQL'>>
# conn=MySQL.from_conf()
#
# print(conn.host,conn.port)
# conn.from_conf() #对象也可以调用，但是默认传的第一个参数仍然是类

"""
比较staticmethod和classmethod的区别
"""
# from knowledge import settings
# class MySQL:
#     def __init__(self,host,port):
#         self.host=host
#         self.port=port
#
#     @staticmethod
#     def from_conf():
#         return MySQL(settings.HOST,settings.PORT)

    # @classmethod
    # def from_conf(cls):
    #     return cls(settings.HOST,settings.PORT)

#     def __str__(self):
#         return '就不告诉你'
#
#
#
# class Mariadb(MySQL):
#
#     def __str__(self):
#         return '主机:%s 端口:%s' %(self.host,self.port)
#
#
# m=Mariadb.from_conf()
# print(m) #我们的意图是想触发Mariadb.__str__,但是结果触发了MySQL.__str__的执行，打印就不告诉你
"""
小练习 ：---
"""
import time
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

a = Date("1996", 2, 18)
b = Date.now()
c = Date.tomorrow()
print(a.year, a.month, a.day)
print(b.year, b.month, b.day)
print(c.year, c.month, c.day)

import time
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

class EuroDate(Date):
    def __str__(self):
        return "year is %s month is %s day is %s"%(self.year, self.month, self.day)

e = EuroDate.now()
print(e)
"""
输出结果是<date 这个类的实例>

如果使用classmethod的结果就不同
"""
import time
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # @staticmethod
    # def now():
    #     t = time.localtime()
    #     return Date(t.tm_year, t.tm_mon, t.tm_mday)
    @classmethod
    def now(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

class EuroDate(Date):
    def __str__(self):
        return "year is %s month is %s day is %s"%(self.year, self.month, self.day)

e = EuroDate.now()
print(e)  # 此时结果就是EuroDate的__str__因为调用now的时候将cls（EuroDate这个类）传了进去