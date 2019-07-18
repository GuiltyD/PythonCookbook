from collections import OrderedDict
class Typed:
	_expected_type = type(None)
	def __init__(self,name=None):
		self._name = name
	def __set__(self, instance, value):
		if not isinstance(value, self._expected_type):
			raise TypeError('argument {} must be {}'.format(value,self._expected_type))
		instance.__dict__[self._name] = value

class Int(Typed):
	_expected_type = int

class Str(Typed):
	_expected_type = str

class Float(Typed):
	_expected_type = float

class OrderMate(type):
	def __new__(cls,clsname,bases,clsdict):
		d  = dict(clsdict)
		order =[]
		for name,value in clsdict.items():
			if isinstance(value, Typed):
				value._name = name
				order.append(name)
			d['_order'] = order
		return type.__new__(cls,clsname,bases,d)

	@classmethod
	def __prepare__(metacls, name, bases):
		return OrderedDict()
class Spam(metaclass=OrderMate):
	x = Int()
	y = Str()
	z = Float()
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def get_order(self):
		print(self._order)
	def as_csv(self):
		return ','.join([str(getattr(self,name)) for name in self._order])


s = Spam(1,'x',2.1)
s.get_order()
print(s.as_csv())