from functools import wraps,partial
import logging

def logged(func = None,level=logging.DEBUG,name = None, message = None):
	if func is None:
		return partial(logged,level = level,name = name,message=message)
	logname = name if name else func.__module__
	log = logging.getLogger(logname)
	logmsg = message if message else func.__name__
	@wraps(func)
	def wrapper(*args,**kwargs):
		log.log(level,logmsg)
		return func(*args,**kwargs)
	return wrapper

@logged
def add(x,y):
	print(x+y)

logging.basicConfig(level = logging.DEBUG)
add(100,3000)
@logged(level = logging.WARNING,name = 'maomao',message = 'doudou')
def add1(x,y):
	print(x+y)

add1(100,3000)