class A:
	def spam(self):
		print('A.spam')
class B(A):
	def spam(self):
		print('B.spam')
		super().spam()

b = B()
b.spam()
print('-'*20)
# 调用父类的__init__()方法确保父类被正确初始化

class AA:
	def __init__(self):
		self.x = 0

class BB(AA):
	def __init__(self):
		super().__init__()
		self.y = 1

bb = BB()
print('bb.x=',bb.x)
print('bb.y=',bb.y)
print('-'*20)
#当覆盖了Python中的特殊方法后


class Proxy:
	def __init__(self,obj):
		self._obj = obj

	def __getattr__(self, item):
		return getattr(self._obj,item)

	def __setattr__(self, key, value):
		if key.startswith('_'):
			super().__setattr__(key,value)
		else:
			setattr(self._obj,key,value)

p = Proxy(bb)

p._maomao ='maomao'
p.maomao = 'maomao'
print(p.x)
print(p.y)
#p中也设置了maomao属性
print(p.maomao)

print(p._maomao)
#bb中也设置了毛毛属性
print(bb.maomao)
print('-'*20)
#钻石继承
class Base:
	def __init__(self):
		print('Base.__init__')

class AAA(Base):
	def __init__(self):
		Base.__init__(self)
		print('AAA.__init__')

class BBB(Base):
	def __init__(self):
		Base.__init__(self)
		print('BBB.__init__')


class CCC(AAA,BBB):
	def __init__(self):
		AAA.__init__(self)
		BBB.__init__(self)
		print('CCC.__init')

ccc =CCC()
