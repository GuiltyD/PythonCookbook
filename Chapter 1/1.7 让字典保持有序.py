from collections import OrderedDict
d =OrderedDict()

d['foo'] = 2
d['bar'] = 3
d['spam'] = 4
d['grok'] = 5

for key in d:
	print(key)