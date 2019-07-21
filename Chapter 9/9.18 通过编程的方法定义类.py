import operator
import types
import sys
def named_tuple(classname,filednames):
	cls_dict = {name:property(operator.itemgetter(n)) for n,name in enumerate(filednames)}

	def __new__(cls,*args):
		if len(args) != len(filednames):
			raise TypeError('Excepted {} arguments'.format(len(filednames)))
		return tuple.__new__(cls,args)


	cls_dict['__new__'] = __new__

	cls = types.new_class(classname,(tuple,),{},lambda ns:ns.update(cls_dict))


	cls.__module__ = sys._getframe(1).f_globals['__name__']

	return cls


Point= named_tuple('Point',['x','y'])

p = Point(1,2)
print(p.x,p.y)

