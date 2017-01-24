def is_pow_of_2(n):
	return n and not (n & (n-1))
	
print is_pow_of_2(7)
print is_pow_of_2(8)
print is_pow_of_2(16)	