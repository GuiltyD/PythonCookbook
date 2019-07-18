class Descriptor:
	def __init__(self,name =None,**opts):
		self.name = name
		for key,value in opts.items():
			setattr(self,key, value)
	def __set__(self, instance, value):
		instance.__dict__[self.name] = value


def Typed(expected_type, cls=None):
	if cls is None:
		return lambda cls:Typed(expected_type,cls)
	super_set = cls.__set__
	def __set__(self,instance,value):
		if not isinstance(value,expected_type):
			raise TypeError('Excepted {}'.format(expected_type))
		super_set(self,instance,value)
	cls.__set__ = __set__
	return cls

def Unsigned(cls):
	super_set = cls.__set__
	def __set__(self,instance,value):
		if value<0:
			raise TypeError('Must >=0')
		super_set(self,instance,value)
	cls.__set__ = __set__
	return cls

def MaxSized(cls):
	super_init = cls.__init__
	super_set = cls.__set__
	def __init__(self,name,**opts):
		if 'size' not in opts:
			raise TypeError('missing size option')
		super_init(self,name,**opts)
	cls.__init__ = __init__

	def __set__(self,instance,value):
		if len(value)>self.size:
			raise TypeError('The Lenth of {} must <= {}'.format(value,self.size))
		super_set(self,instance,value)
	cls.__set__ = __set__
	return cls





# Mixin
@Typed(int)
class Ingeter(Descriptor):
	pass

@Typed(float)
class Float(Descriptor):
	pass

@Unsigned
class UnsignedFloat(Float):
	pass

@Unsigned
class UnsignedIngeter(Ingeter):
	pass

@Typed(str)
class String(Descriptor):
	pass


@MaxSized
class MaxsizeString(String):
	pass

class Stock():
	name = MaxsizeString('name',size = 8)
	shares = UnsignedIngeter('shares')
	price = UnsignedFloat('price')

	def __init__(self,name,shares,price):
		self.name = name
		self.shares = shares
		self.price = price



stock = Stock('maoma',50,21.3)

print(stock.name)
print(stock.shares)
print(stock.price)

