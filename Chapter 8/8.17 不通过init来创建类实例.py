import time

class Date:
	def __init__(self,year,month,day):
		self.year = year
		self.month = month
		self.day = day

	@classmethod
	def today(cls):
		t = time.localtime()
		new_instance = Date.__new__(Date)
		new_instance.year = t.tm_year
		new_instance.month = t.tm_mon
		new_instance.day = t.tm_mday
		return new_instance

	def __str__(self):
		return '{}/{}/{}'.format(self.year,self.month,self.day)


d = Date.today()
print(d)
