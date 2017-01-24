def ispowof4(n):
	if n is 0:
		return 0
	while n is not 1:
		if (n%4):
			return 0
		n /= 4
	return 1

def ispowof4_1(n):
	if n and not (n & (n-1)):
		count = 0
		while n > 1:
			n >>= 1
			count += 1
		return 0 if (count & 1) else 1
	return 0
print ispowof4(16)
print ispowof4_1(16)
print ispowof4(27)
print ispowof4_1(27)		