from operator import methodcaller
import math
class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __repr__(self):
		return 'Point({},{})'.format(self.x,self.y)

	def distance(self,x,y):
		return math.hypot(self.x-x,  self.y-y)

p = Point(2,3)
print(methodcaller('distance',0,0)(p))
