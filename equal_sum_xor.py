def equal_sum_xor(n):
	unset_bits = 0
	while n:
		if (n & 1) is 0:
			unset_bits += 1
		n = n >> 1
	return 2**unset_bits

for i in range(13):
	print equal_sum_xor(i)
		