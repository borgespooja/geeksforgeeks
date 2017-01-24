def nth_5_pow_magic_number(n):
	pow, res = 1, 0
	while n:
		pow *= 5
		if n & 1:
			res += pow
		n >>= 1
	return res

print nth_5_pow_magic_number(2)
print nth_5_pow_magic_number(5)
print nth_5_pow_magic_number(10)	