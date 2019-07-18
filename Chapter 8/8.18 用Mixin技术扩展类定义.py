from collections import UserDict

class LoggeMappingMixin:
	def __getitem__(self, item):
		print('Get {}'.format(item))
		return super().__getitem__(item)

	def __setitem__(self, key, value):
		print('set {}'.format(key))
		super().__setitem__(key,value)

	def __delitem__(self, key):
		print('del {}'.format(key))
		super().__delitem__(key)


class LogDict(LoggeMappingMixin,UserDict):
	pass

d = LogDict()
d['a'] = 1
d['a']
del d['a']

###########################################

class SetOnceDictMixin:
	def __setitem__(self, key, value):
		if key in self:
			raise TypeError('{} arealdy  setted in you dict')


class OnceDict(SetOnceDictMixin,dict):
	pass

o = OnceDict({'a':1})

# o['a'] =2

############################################

def LoggeMappingMixin(cls):
	super_getitem = cls.__getitem__
	super_setitem = cls.__setitem__
	super_delitem = cls.__delitem__
	super_init = cls.__init__

	def __init__(self,*arg,excepted_str,**kwargs):
		self.excepted_str = excepted_str
		super_init(self,*arg,**kwargs)

	def __getitem__(self,key):

		print('Get {}'.format(key))
		return super_getitem(self,key)

	def __setitem__(self, key,value):
		if not isinstance(key, self.excepted_str):
			raise TypeError('Excepted {}'.format(self.excepted_str))
		print('Set {}'.format(key))
		super_setitem(self, key,value)

	def __delitem__(self,key):
		print('del {}'.format(key))
		super_delitem(self,key)

	cls.__init__ = __init__
	cls.__getitem__ = __getitem__
	cls.__setitem__ = __setitem__
	cls.__delitem__ = __delitem__


	return cls

@LoggeMappingMixin
class MyDict(UserDict):
	pass



m = MyDict(b = 'maomao',excepted_str = str)



