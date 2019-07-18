class OpenFile:
	def __init__(self,filename,method):
		self.filename = filename
		self.method = method

	def __enter__(self):
		self.f = open(self.filename,self.method)
		print('已经打开文件')
		return self.f

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.f.close()
		print('文件已经关闭')

file = OpenFile(r'C:\Users\Administrator\Desktop\maomao.txt','a')

with file as f:
	f.write('我是毛毛虫')
	