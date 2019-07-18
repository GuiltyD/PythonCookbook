from functools import total_ordering

class Room:
	def __init__(self,name,length,width):
		self.name = name
		self.length = length
		self.width = width
		self.square_feet = self.length*self.width
@total_ordering
class House:
	def __init__(self,name,style):
		self.name = name
		self.style = style
		self.rooms = list()

	@property
	def all_room_square(self):
		return sum(r.square_feet for r in self.rooms)

	def add_rooms(self,room):
		self.rooms.append(room)

	def __str__(self):
		return '{}:{} square foot {}'.format(self.name,self.all_room_square,self.style)

	def __eq__(self, other):
		return self.all_room_square == other.all_room_square

	def __lt__(self, other):
		return self.all_room_square < other.all_room_square



h1 = House('maomao','capa')
h1.add_rooms(Room('1',20,30))
h1.add_rooms(Room('2',20,30))
h1.add_rooms(Room('3',60,50))
h1.add_rooms(Room('4',30,20))
h1.add_rooms(Room('5',10,30))


h2 = House('doudou','pipi')
h2.add_rooms(Room('1',10,30))
h2.add_rooms(Room('2',70,30))
h2.add_rooms(Room('3',90,50))
h2.add_rooms(Room('4',330,20))
h2.add_rooms(Room('5',10,30))
print(h2.all_room_square)
print(h1.all_room_square)
print(h1 >= h2)