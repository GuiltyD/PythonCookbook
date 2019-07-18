def log_getattribute(cls):
	super_getattribute = cls.__getattribute__
	def __getattribute__(self,name):
		print('get:',name)
		return super_getattribute(self,name)
	cls.__getattribute__ =__getattribute__
	return cls

@log_getattribute
class A:
	def __init__(self,x):
		self.x = x

	def spam(self):
		pass

a = A(2)
print(a.x)