def turn_off_a_bit(n, k):
	return n & (~(1 << (k-1)) & 0xFF)

for i in range(1,6):
	print turn_off_a_bit(15, i)
