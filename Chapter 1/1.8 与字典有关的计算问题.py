price = {
	'apple':18,
	'banana':15,
	'banana_new':15,
	'watermelon':14,
	'orange':10,
	'pineapple':23,
}
min_price = sorted(zip(price.values(),price.keys()))
print(min_price)
