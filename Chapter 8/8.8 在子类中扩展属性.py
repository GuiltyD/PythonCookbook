class Person:
	def __init__(self,name):
		self.name = name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self,value):
		if not isinstance(value,str):
			raise TypeError(
				'Excepted a string'
			)
		else:
			self._name = value

	@name.deleter
	def name(self):
		raise AttributeError('can\'t delete')


class SubPerson(Person):
	@property
	def name(self):
		print('Get name')
		return super().name

	@name.setter
	def name(self,value):
		print('setting name')
		super(SubPerson,SubPerson).name.__set__(self,value)

	@name.deleter
	def name(self):
		print('del name')
		super(SubPerson,SubPerson).name.__delete__(self)




s  =SubPerson('MAOMAO')
print(s._name)
