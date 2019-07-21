def test():
	x = 12
	loc = locals()
	exec('b = x +1')
	b = loc['b']
	print(b)
test()
	