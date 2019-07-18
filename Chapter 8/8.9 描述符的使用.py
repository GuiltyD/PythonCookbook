class Integer:
	def __init__(self,name ):
		self.name = name

	def __get__(self,instance,value):
		print('get attr')
		if instance is None:
			return self
		else:
			return instance.__dict__[self.name]

	def __set__(self, instance, value):
		print('set attr')
		if not isinstance(value,int):
			raise TypeError('Only integer')

		instance.__dict__[self.name] = value

	def __delete__(self, instance):
		del instance.__dict__[self.name]


class Point:
	x = Integer('x')
	y = Integer('y')
	def __init__(self,x,y):
		self.x = x
		self.y = y


class Typed:
	def __init__(self,name,typestr):
		self.name = name
		self.typestr = typestr

	def __get__(self,instance,value):
		if instance is None:
			return self
		else:
			return instance.__dict__[self.name]

	def __set__(self, instance, value):
		if not isinstance(value,self.typestr):
			raise TypeError('Tpye Error,only{0.typestr}'.format(self))

		instance.__dict__[self.name] = value

	def __delete__(self, instance):
		del instance.__dict__[self.name]


def typeassert(**kwargs):
	def decorate(cls):
		for key,value in kwargs.items():
			setattr(cls,key,Typed(key,value))
		return cls
	return decorate


@typeassert(name = str ,age = int)
class Person:
	def __init__(self,name,age):
		self.myname = name
		self.myage = age


p = Person('maomao',18)
print(p.myname)
p.myname = 18
print(p.myname)


