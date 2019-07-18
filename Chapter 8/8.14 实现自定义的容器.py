import collections
import bisect
class A(collections.Sequence):
	def __init__(self,initial=None):
		self._item = sorted(initial) if initial else []

	def __getitem__(self, item):
		return self._item[item]

	def __len__(self):
		return len(self._item)

	def add(self,item):
		bisect.insort(self._item,item)

	def __str__(self):
		return str(self._item)


a = A([1,2,5])
a.add(4)
print(a)
for i in a:
	print(i)

