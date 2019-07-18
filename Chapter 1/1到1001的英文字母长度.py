mapping = {
	0:'',
	1:'one',
	2:'two',
	3:'three',
	4:'four',
	5:'five',
	6:'six',
	7:'seven',
	8:'eight',
	9:'nine',
	10:'ten',
	11:'eleven',
	12:'twelve',
	13:'thirteen',
	14:'fourteen',
	15:'fifteen',
	16:'sixteen',
	17:'seventeen',
	18:'eighteen',
	19:'nineteen',
	20:'twenty',
	30:'thirty',
	40:'forty',
	50:'fifty',
	60:'sixty',
	70:'seventy',
	80:'eighty',
	90:'ninety',
	100:'onehundred',
	200:'twohundred',
	300:'threehundred',
	400:'fourhundred',
	500:'fivehundred',
	600:'sixhundred',
	700:'sevenhundred',
	800:'eighthundred',
	900:'ninehundred',
	1000:'thousand',
}


def count_in_mapping(num):
	return  len(mapping[num])

def count_less_than_100(num):
	print((num // 10) * 10,num % 10)
	return  len(mapping[(num // 10) * 10]) + len(mapping[num % 10])

def count_less_than_1000(num):

	return  len(mapping[(num // 100) * 100]) + len('and') +count_less_than_100(num%100)

def count(num):
	if (num >= 1 and num <= 20) or (num < 100 and num % 10 == 0) or num % 100 == 0 or num % 1000 == 0:
		return count_in_mapping(num)
	elif num<100:

		return count_less_than_100(num)
		# return  count_less_than_100(num)
	elif num>100 and num<1000:
		return count_less_than_1000(num)
sum = 0
for i in range(1,1001):
	sum+=count(i)
print(sum)
print(count_less_than_100(30))