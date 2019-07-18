from collections import deque

my_deque = deque(maxlen = 2)

for i in range(10):
	my_deque.append(i)
	print(my_deque)