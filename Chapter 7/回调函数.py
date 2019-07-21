from functools import wraps
from queue import Queue


def async_func(func,args, *,callback):
	res = func(*args)
	callback(res)
	# return res


class Async:	
	def __init__(self,func,args):
		self.func = func
		self.args = args


class Myqueue:
	def __init__(self):
		self.queue = Queue()
	def put(self,value):
		self.queue.put(value)
	def get(self):
		return self.queue.get()
	def callback(self,value):
		print('res:',value)
		self.put(value)
		

def inline_async(func):
	@wraps(func)
	def wrapper(*args):
		#得到生成器
		f = func(*args)
		res_queue = Queue()
		#第一次没有值先压入None
		res_queue.put(None)
		while True:
			a = res_queue.get()
			try:
				'''send在有值的时候会把值送入上一个yield，并且恢复环境继续运行，在没有值(None)时，相当于None,
				这里第一次传入的是None，所以只会运行Next，把yield返回的值赋给res，下一次的时候拿到的是这一次运行
				得到的值，所以会将其传给上一个yield。
				'''
				res = f.send(a)
				async_func(res.func,res.args,callback = res_queue.put)
			except StopIteration:
				break
		return wrapper

def add(x,y):
	return x+y


@inline_async
def test():
	r = yield Async(add,(2,3))
	print(r)
	r = yield Async(add, (2, 3))
	print(r)

test()

	