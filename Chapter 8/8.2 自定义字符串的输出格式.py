class Date:
	def __init__(self,year,month,day):
		self.year = year
		self.month  = month
		self.day = day
		self._format = {
			'y-m-d':'{d.year}-{d.month}-{d.day}',
			'm/d/y':'{d.month}/{d.day}/{d.year}',
			'd/m/y':'{d.day}/{d.month}/{d.year}',
		}


	def __format__(self, code = ''):
		if code == '':
			code = 'y-m-d'
		fmt = self._format[code]
		return fmt.format(d = self)

date = Date(2019,7,10)
print(format(date))
print(format(date,'m/d/y'))
print(format(date,'d/m/y'))
