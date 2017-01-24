def check_parity(n):
	parity = 0
	while n:
		parity = int(not(parity))
		n &= (n-1)
	return parity

print check_parity(13)
print check_parity(14)
print check_parity(15)	