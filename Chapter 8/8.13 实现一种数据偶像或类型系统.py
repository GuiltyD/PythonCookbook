class Descriptor:
	def __init__(self,name =None,**opts):
		self.name = name
		for key,value in opts.items():
			setattr(self,key, value)
	def __set__(self, instance, value):
		instance.__dict__[self.name] = value


class Typed(Descriptor):
	excepted_type = type(None)

	def __set__(self, instance, value):
		if not isinstance(value,self.excepted_type):
			raise TypeError('Excepted {}'.format(self.excepted_type))
		super().__set__(instance,value)

class Unsigned(Descriptor):
	def __set__(self, instance, value):
		if value<0:
			raise ValueError('Expected >= 0')

		super().__set__(instance,value)


class MaxSized(Descriptor):
	def __init__(self,name = None,**opts):
		if 'size' not in opts:
			raise TypeError('missing size option')
		super().__init__(name,**opts)

	def __set__(self, instance, value):
		if len(value)>self.size:
			raise TabError('size must br < {}'.format(self.size))
		super().__set__(instance,value)

# Mixin
class Ingeter(Typed):
	excepted_type = int


class Float(Typed):
	excepted_type = float


class UnsignedFloat(Unsigned,Float):
	pass


class UnsignedIngeter(Unsigned,Ingeter):
	pass


class String(Typed):
	excepted_type = str



class MaxsizeString(String,MaxSized):
	pass

#设置类装饰器
def check_attributes(**kwargs):
	def decorate(cls):
		for key,value in kwargs.items():
			if isinstance(value, Descriptor):
				value.name = key
				setattr(cls,key, value)
			else:
				raise TypeError('Arguments must be instance of Descript')
		return cls
	return decorate


#设置元类
class CheckAttrabutesMate(type):
	def  __new__(cls, classname,bases,methods):
		for key,value in methods.items():
			if isinstance(value, Descriptor):
				value.name = key
		return type.__new__(cls,classname,bases,methods)

class Stock(metaclass=CheckAttrabutesMate):
	name = MaxsizeString( size = 8)
	shares = UnsignedIngeter()
	price = UnsignedFloat()


	def __init__(self,name,shares,price):
		self.name = name
		self.shares = shares
		self.price = price



stock = Stock('maomao',50,21.3)

print(stock.name)
print(stock.shares)
print(stock.price)

