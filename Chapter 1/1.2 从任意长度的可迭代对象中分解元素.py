# my_tuple = tuple(range(10))
# # #b = [1, 2, 3, 4, 5, 6, 7, 8]
# # a, *b, c = my_tuple
# # print(b)

my_tuple = [
	('foo',1,2),
	('foo',2,5),
	('bar',3,7),
	('bar',5,6),
	('bar',7,9),
]
def do_foo(x,y):
	print('foo=',x+y)

def do_bar(x,y):
	print('bar=',x+y)

for item,*tup in my_tuple:
	if item == 'foo':
		do_foo(*tup)
	else:
		do_bar(*tup)