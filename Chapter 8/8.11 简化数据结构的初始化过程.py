# class Integer:
# 	def __init__(self,name):
# 		self.name = name
# 	def __set__(self, instance, value):
# 		if not isinstance(value,int):
# 			raise TypeError('Excepted int!')
# 		instance.__dict__[self.name] = value
# 	def __get__(self, instance, owner):
# 		if instance is None:
# 			return self
# 		else:
# 			return instance.__dict__[self.name]
# 	def __delete__(self, instance):
# 		pass
#
# # class StructureMate(type):
# # 	def __init__(self, classname, bases, clsdict):
# #
# # 		fields = getattr(self, '_fields', [])
# # 		for item in fields:
# # 			setattr(self, item, Integer(item))
# def setperporty(obj):
# 	def wrapper(*args):
# 		fields = getattr(obj,'_fields')
# 		for item in fields:
# 			setattr(obj,item,Integer(item))
# 		for name,value in zip(fields,args):
# 			setattr(obj,name,value)
# 		return obj
# 	return wrapper


# class Structure():
# 	_fields = []
# 	def __init__(self,*args):
# 		self.args = args
# 		if len(self._fields) != len(self.args):
# 			raise TypeError('Expected {} arguments'.format(len(self._fields)))
#
# 		for name, value in zip(self._fields,self.args):
# 			setattr(self,name,value)





# import math
#
#
#
# class Circle(Structure):
# 	_fields = ['radius']
# 	@property
# 	def area(self):
# 		return math.pi*self.radius**2
#
# c = Circle(2)
# print(c.area)

class Structure():
	_fields = []
	def __init__(self,*args,**kwargs):
		self.args = args
		if len(self._fields) < len(self.args):
			raise TypeError('Expected {} arguments'.format(len(self._fields)))

		for name, value in zip(self._fields,self.args):
			setattr(self,name,value)

		for name in self._fields[len(args):]:
			setattr(self,name,kwargs.pop(name))

		extra_args = kwargs.keys() - self._fields
		for name in extra_args:
			setattr(self,name, kwargs.pop(name))

		# if kwargs:
		# 	raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))

import math


class Circle(Structure):
	_fields = ['radius','D']
	@property
	def area(self):
		return math.pi*self.radius**2

c = Circle(2, D = 2,a=3)