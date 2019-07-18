class Singlestance(type):
	def __init__(self,*args,**kwargs):
		self.__instance = None
		super().__init__(*args,**kwargs)

	def __call__(self, *args, **kwargs):
		if self.__instance is None:
			self.__instance = super().__call__(*args,**kwargs)
			return self.__instance
		else:
			return self.__instance

class Spam(metaclass=Singlestance):
	pass


a =Spam()
b =Spam()
print(a==b)
