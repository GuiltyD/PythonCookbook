import inspect
import logging


class MatchSigntureMate(type):
	def __init__(self, clsname, bases, clsdict):
		super().__init__(clsname, bases, clsdict)
		sup = super(self, self)
		for name, value in clsdict.items():
			if name.startswith('_') or not callable(value):
				continue
			prev_dfn = getattr(sup, name, None)

			if prev_dfn:
				prev_sig = inspect.signature(prev_dfn)
				val_sig = inspect.signature(value)
				if prev_sig != val_sig:
					logging.warning('Signature mismatch in {},{}!={}'.format(value.__qualname__, prev_sig, val_sig))



class Root(metaclass=MatchSigntureMate):
	pass


class A(Root):
	def foo(self,x,*,y):
		print(x,y)

					
class B(A):
	def foo(self,x,y):
		print(x,y)