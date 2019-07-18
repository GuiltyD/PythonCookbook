import os


file_list = os.listdir('.')
n = 0

for file in file_list:
	p = 0
	f = open(file, 'r', encoding ='utf-8')
	for i in f.readlines():
		p+=1
		n+=1
	print(file+'有'+str(p)+'行')
	f.close()
print('您这个文件夹一共写了{}行代码'.format(n))
# f = open(file_list[0],'r',encoding='utf8')
# for i in f.readlines():
# 	print(i)
# 	n+=1
# print(n)