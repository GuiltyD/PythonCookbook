class layzproperty:
	def __init__(self,func):
		self.func = func
	#只有一个__get__方法的时候，描述符和宿主类会呈现弱绑定的关系，只有在要取的值不在底层字典里面的时候才会使用该方法
	def __get__(self,instance,cls):
		value = self.func(instance)
		#这个值一旦被计算出来，就通过类属性的方式保存在类中了，下次在调用这个属性的时候就不会再计算了
		setattr(instance,self.func.__name__,value)
		#这里要返回一次值，否则第一次打印的时候是不会显示计算的值的
		return value

	#当我设置了其他两个函数的时候，每次调用都会重新计算一次
	def __set__(self, instance, value):
		pass

	def __delete__(self, instance):
		pass

import math

class Circle:
	def __init__(self,radius):
		self.radius = radius
	@layzproperty
	def area(self):
		print('computing area')
		return math.pi*self.radius**2


c = Circle(2)

print(c.area)
print(c.area)

