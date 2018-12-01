#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-01 20:49:09
# @Author  : Zhang Yahan (zyahan1997@163.com)
# @Link    : http://www.github.com/zhangyahan/
# @Version : $Id$


# 单例模式: 用来创建单个实例

class Foo:

	instance = None

	def __init__(self, name):
		print('初始化方法被调用')
		self.name = name

	@classmethod  # definition class method
	def get_instance(cls, name):
		if cls.instance:  # if class variable is not None
			return cls.instance  # reutrn 
		else:
			obj = cls(name)  #  create class object
			cls.instance = obj  # definition class variable equal class object
			return obj   # return object

obj1 = Foo.get_instance('alex')
obj2 = Foo.get_instance('whh')
obj3 = Foo.get_instance('alex')
obj4 = Foo.get_instance('alex')
obj5 = Foo.get_instance('alex')
obj6 = Foo.get_instance('alex')
obj7 = Foo.get_instance('alex')
obj8 = Foo.get_instance('alex')
