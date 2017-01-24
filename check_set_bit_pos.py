def ispowerof2(n):
	return n and not (n & (n-1))

def check_set_bit_pos(n):
	if not ispowerof2(n):
		print "invalid number: number is 0" if n is 0 else "invalid number: has more than one set bit"
		return
	count = 0
	while n:
		n >>= 1
		count += 1
	print count

check_set_bit_pos(14)
check_set_bit_pos(8)
check_set_bit_pos(16)
check_set_bit_pos(0)
check_set_bit_pos(12)
check_set_bit_pos(128)
		
		