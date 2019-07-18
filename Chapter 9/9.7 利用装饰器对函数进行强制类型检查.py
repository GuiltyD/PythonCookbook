from inspect import signature
from functools import wraps
__DEBUG__ = True
def typeassert(*ty_args,**ty_kwargs):
	def decorate(func):
		if not __DEBUG__:
			return func
		sig =signature(func)
		#sig.bind_partial可以部分绑定函数的签名信息
		bound_type = sig.bind_partial(*ty_args,**ty_kwargs).arguments
		@wraps(func)
		def wrapper(*args,**kwargs):
			#bind是全部绑定
			bound_values = sig.bind(*args,**kwargs)
			#检查函数全部签名信息，在装饰器参数信息里的就会被强制检查到
			for name,value in bound_values.arguments.items():
				if name in bound_type:
					if not isinstance(value, bound_type[name]):
						raise TypeError('Arguments {} must be {}'.format(name,bound_type[name]))
			return func(*args,**kwargs)
		return wrapper
	return decorate


@typeassert(int,float)
def add(x,y):
	print(x+y)


add(1,2.0)