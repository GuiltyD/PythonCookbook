def deque(items):
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)


mylist = [1,2,3,1,2,3,4,5,6,7,1,2,5,4,5]
print(list(deque(mylist)))