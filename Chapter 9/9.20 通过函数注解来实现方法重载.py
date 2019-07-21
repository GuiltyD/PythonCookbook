import inspect
def foo(x:int,y:str):
	print(x,y)

sig =inspect.signature(foo)
for name,parms in sig.parameters.items():
	print(parms.default)



