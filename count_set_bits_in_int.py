def count_set_bits_in_int(n):
	bit_count = 0
	while n:
		bit_count += (n&1)
		n >>= 1
	return bit_count

def count_set_bits_in_int_1(n):
	bit_count = 0
	while n:
		n &= (n-1)
		bit_count += 1
	return bit_count

print count_set_bits_in_int(6)
print count_set_bits_in_int_1(6)

print count_set_bits_in_int(13)
print count_set_bits_in_int_1(13)
	
		