from collections import defaultdict

a = defaultdict(list)
a['maomao'].extend([1,2,3])
a['doudou'].append(2)
print(a)
b = defaultdict(dict)
b['maomao'].update(a=1,b=2)
b['doudou'].update({
	'name':'doudou',
	'age':18,
})
print(b)