def swap_even_odd_bits(x):
	even_bits_set = x & 0xAAAAAAAA
	odd_bits_set = x & 0x55555555
	even_bits_set >>= 1
	odd_bits_set <<= 1
	return (even_bits_set | odd_bits_set)
	
print swap_even_odd_bits(23)
print swap_even_odd_bits(43)	