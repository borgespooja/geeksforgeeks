def square_brute_force(n):
	if n < 0:
		n = -n
	return sum([n for _ in range(n)])

def square_bit(n):
	if n is 0:
		return 0
	if n < 0:
		n = -n
	x = (n >> 1)	
	if (n & 1):
		return ((square_bit(x) << 2)+ (x << 2) + 1)
	else:
		return (square_bit(x) << 2) 
		
print square_brute_force(3)
print square_brute_force(4)
print square_bit(3)
print square_bit(4)		