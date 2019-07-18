from abc import ABCMeta,abstractmethod
import io
class IStream(metaclass=ABCMeta):
	@abstractmethod
	def read(self,maxbytes=-1):
		pass
	@abstractmethod
	def write(self,data):
		pass

IStream.register(io.IOBase)
f = open('foo.txt','r')

print(isinstance(f,IStream))

a= [1,2,3]
import collections
print(isinstance(a,collections.Iterable))