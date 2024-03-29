from functools import wraps
import logging

def logged(level,name = None, message = None):
	def decorate(func):
		logname = name if name else func.__module__
		log = logging.getLogger(logname)
		logmsg = message if message else func.__name__
		@wraps(func)
		def wrapper(*args,**kwargs):
			log.log(level,logmsg)
			return func(*args,**kwargs)
		return wrapper
	return decorate

@logged(logging.DEBUG)
def add(x,y):
	print(x+y)

logging.basicConfig(level = logging.DEBUG)
add(100,3000)