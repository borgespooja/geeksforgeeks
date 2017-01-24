def count_set_bits(n):
	bitcount = 0
	while n:
		if n & 1:
			bitcount += 1
		n >>= 1	
	return bitcount
	
def count_bits_to_be_flipped_from_a_to_b(a,b):
	a_xor_b = (a ^ b)
	return count_set_bits(a_xor_b)
	
print count_bits_to_be_flipped_from_a_to_b(124 , 31)
	

	