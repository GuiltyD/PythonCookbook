import heapq

class Priority:
	def __init__(self):
		self.queue = []
		#_index是为了防止优先级相同，按照先入堆的顺序弹出元素
		self._index = 0

	def push(self,priority,item):
		heapq.heappush(self.queue,(-priority,self._index,item))
		self._index+=1
	#按照最小的元素先弹出的顺序
	def pop(self):
		return heapq.heappop(self.queue)[-1]

class Item:
	def __init__(self,name):
		self.name = name

	def __repr__(self):
		return 'Item({})'.format(self.name)

q = Priority()
q.push(5,Item('maomao'))
q.push(15,Item('doudou'))
q.push(2,Item('jack'))
q.push(26,Item('danny'))
q.push(15,Item('Tom'))
q.push(6,Item('jessy'))

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())