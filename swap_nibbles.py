def swap_nibbles(n):
	return ((n & 0x0F)<<4 | (n & 0xF0)>>4)
print bin(0b11001111)[2:], bin(swap_nibbles(0b11001111))[2:]	