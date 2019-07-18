from functools import wraps
import time

class A:
	
	def timeis(self,func):
		@wraps(func)
		def wrapper(*args,**kwargs):
			start = time.time()
			res = func(*args,**kwargs)
			end = time.time()
			print(func.__name__,end-start)
			return res
		return wrapper


a = A()
@a.timeis
def count(n):
	while n<10000:
		n+=1
count(0)