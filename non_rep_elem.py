def non_rep_elem(a):
	x, y, xor, set_bit_no = 0, 0, 0, 0
	for i in a:
		xor ^= i
	set_bit_no = xor & ~(xor-1)
	for i in a:
		if i & set_bit_no:
			x ^= i
		else:
			y ^= i
	return (x,y)		
print non_rep_elem([2, 3, 7, 9, 11, 2, 3, 11])