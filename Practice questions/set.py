

"""Write a function that takes two lists and returns the common elements (use set)"""

def common_element(a,b):
	return list(set (a) & set (b))
#input two list
a= list(map(int,input('enter some number :').split()))
b= list(map(int,input('Enter some number :').split()))
 print('common elements are :', common_element(a,b))

