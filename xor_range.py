def xor_range(n):
	rem = n%4
	if rem is 0:
		return n
	elif rem is 1:
		return 1
	elif rem is 2:
		return n+1
	elif rem is 3:
		return 0
	
print xor_range(6)
print xor_range(7)	
		