import heapq
my_list = [1,6,-5,65,-3,12,15,45,78,-84]
largest3 = heapq.nlargest(3,my_list)
smallest3 = heapq.nsmallest(3,my_list)
print(largest3)
print(smallest3)

#dict
my_dict_list = [{'name':'jack','age':28},
				{'name':'tom','age':25},
				{'name':'danny','age':15},
				{'name':'ham','age':16},
				{'name':'papi','age':20},
                ]
largest3_dict = heapq.nlargest(3,my_dict_list,key = lambda t:t['age'])
smallest3_dict = heapq.nsmallest(3,my_dict_list,key = lambda t:t['age'])
print(largest3_dict)
print(smallest3_dict)