import weakref

class Node:
	def __init__(self, value):
		self.value = value
		self._parent = None
		self.children = []

	@property
	def parent(self):
		return self._parent if self._parent is None else self._parent()

	@parent.setter
	def parent(self,node):
		self._parent = weakref.ref(node)


	def add_child(self,node):
		self.children.append(node)
		node.parent = self

	def __str__(self):
		return 'Node({})'.format(self.value)



root = Node('parent')
c1 = Node('child')
root.add_child(c1)

print(c1.parent)
del root
print(c1.parent)



