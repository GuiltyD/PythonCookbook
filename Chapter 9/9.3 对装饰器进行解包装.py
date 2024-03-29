import time
from functools import wraps

def timeis(func):
	@wraps(func)
	def wrapper(*args,**kwargs):
		start = time.time()
		result = func(*args,**kwargs)
		end = time.time()
		print(func.__name__,end-start)
		return result
	return wrapper


@timeis
def add(x,y):
	return  x+y

print(add.__wrapped__(1,2))