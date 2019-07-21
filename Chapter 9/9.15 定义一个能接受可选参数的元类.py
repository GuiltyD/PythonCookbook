class Mymate(type):
	@classmethod
	def __prepare__(metacls, name, bases,*,debug=True,syn =True):
		return super().__prepare__(name, bases)

	def __new__(cls, name,bases,ns,*,debug=True, syn = True):
		return super().__new__(name,bases,ns)

	def __init__(self, name, bases,ns,debug =True,syn = True):
		return  super().__init__(name,bases,ns)