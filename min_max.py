def min_1(x,y):
	return y ^ ((x^y) & -(x<y))
	
def max_1(x,y):
	return x ^ ((x^y) & -(x<y))	
	
def min_2(x,y):
	return y + ((x-y) & ((x-y)>> 31))

def max_2(x,y):
	return x - ((x-y) & ((x-y) >> 31))
	
print min_1(3,5)
print max_1(3,5)
print min_2(3,5)
print max_2(3,5)	