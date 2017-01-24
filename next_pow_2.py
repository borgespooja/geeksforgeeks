def next_pow_2(n):
	if n and not (n & (n-1)):
		return n
	bit_count = 0
	while n:
		n >>= 1
		bit_count += 1
	return (1 << bit_count)

def next_pow_2_1(n):
	import math
	pos = int(math.ceil(math.log(n, 2)))
	return pow(2,pos)

def next_pow_2_2(n):
	if n and not (n & (n-1)):
		return n
	p = 1
	while p < n:
		p <<= 1
	return p

def next_pow_2_3(n):
	n -= 1
	n |= n >> 1
 	n |= n >> 2
	n |= n >> 4
	n |= n >> 8
	n |= n >> 16
	return n+1
	
print next_pow_2(17)
print next_pow_2_1(17)
print next_pow_2_2(17)
print next_pow_2_3(17)	