def is_multiple_of_4(n):
	if n is 1:
		return False
	else:
		xor = 0
		for i in range(1,n+1):
			xor ^= i
		return (xor is n)
		
def is_multiple_of_4_alt(n):
	return ((n>>2)<<2) is n
		
print is_multiple_of_4(12)
print is_multiple_of_4(11)
print is_multiple_of_4(27)
		
print is_multiple_of_4_alt(12)
print is_multiple_of_4_alt(11)
print is_multiple_of_4_alt(27)		