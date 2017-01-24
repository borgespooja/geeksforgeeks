def addone(n):
	m = 1
	while m & n:
		n ^= m
		m <<= 1
	n ^= m
	return n

def addone1(n):
	return -(~n)

print addone(12)
print addone(13)
print addone1(12)
print addone1(13)

	