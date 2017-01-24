def copy_set_bits_in_range(x,y,l,r):
	for i in range(l,r+1):
		if (y & (1<<(i-1))):
			x |= (1<<(i-1))
	print x		
	return x

copy_set_bits_in_range(10,13,2,3)
copy_set_bits_in_range(8,7,1,2)	