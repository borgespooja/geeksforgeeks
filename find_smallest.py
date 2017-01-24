def find_smallest(x,y,z):
	c = 0
	while x and y and z:
		x -= 1
		y -= 1
		z -= 1
		c += 1
	return c

#alternate approach
def  min_1(x,y):
	return y ^ ((x ^ y) & -(x < y))
	
def find_smallest_1(x,y,z):
	return min_1(x, min_1(y,z))

#alternate approach
def find_smallest_2(x,y,z):
	if not (y/x):
		return y if not (y/z) else z
	return x if not (x/z) else z
	
	
print find_smallest(1,2,3)
print find_smallest_1(1,2,3)
print find_smallest_2(1,2,3)
#print find_smallest(-1,-2,-3) # not workin for neg num
#print find_smallest_1(-1,-2,-3)	
	