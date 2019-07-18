class People:
	def __init__(self,name,age):
		self.name = name
		self.age = age


	@property
	def get_name(self):
		return self.name

	@get_name.setter
	def get_name(self,value):
		self.name = value


people = People('maomao',18)
print(people.get_name)
people.get_name = 'douodou'
print(people.get_name)