def n_rotate_left_d_bits(n,d):
	return ((n << d) | (n >> (32-d)))

#TODO: gives wrong ans, check again	
def n_rotate_right_d_bits(n, d):
	return ((n >> d) | (n << (32-d)))

print bin(43)[2:], bin(n_rotate_left_d_bits(43,5))[2:], n_rotate_left_d_bits(43,5)
print bin(43)[2:], bin(n_rotate_right_d_bits(43,5))[2:], n_rotate_right_d_bits(43,5)

print bin(16)[2:], bin(n_rotate_left_d_bits(16,2))[2:], n_rotate_left_d_bits(16,2)
print bin(16)[2:], bin(n_rotate_right_d_bits(16,2))[2:], n_rotate_right_d_bits(16,2)

