from functools import wraps
import inspect

def optional_debug(func):
	if 'debug' in inspect.getargspec(func).args:
		raise TypeError('debug argument already defined')
	@wraps(func)
	def wrapper(*args,debug=False,**kwargs):
		if debug:
			print('Calling',func.__name__)
		return func(*args,**kwargs)
	return wrapper


@optional_debug
def add(x,y):
	return x+y

print(add(1,2,debug = True))

