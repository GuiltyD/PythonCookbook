from functools import wraps
import time



def timeis(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		res = func(*args, **kwargs)
		end = time.time()
		print(func.__name__, end - start)
		return res

	return wrapper


class Spam:

	@timeis
	def instance_method(self,n):
		print(self,n)
		while n>0:
			n-=1

	@classmethod
	@timeis
	def class_method(self,n):
		print(self,n)
		while n>0:
			n-=1

	@staticmethod
	@timeis
	def static_method( n):
		print( n)
		while n > 0:
			n -= 1

s = Spam()
s.instance_method(1000000)
Spam.class_method(1000000)
Spam.static_method(1000000)
