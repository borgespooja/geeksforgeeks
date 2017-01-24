def find_single_occur_num(a):
	ones, twos = 0, 0
	for x in a:
		twos |= (ones & x)
		ones ^= x
		common_bit_mask = ~((ones & twos) & 0xFFFF)
		ones &= common_bit_mask
		twos &= common_bit_mask
	return ones

def find_single_occur_num1(a):
	res = 0
	for i in range(32):
		sum_num = 0
		y = (1 << i)
		for x in a:
			if x & y:
				sum_num += 1
		if sum_num % 3:
			res |= y
	return res		
		
print find_single_occur_num([5,5,5,8])	
print find_single_occur_num1([5,5,5,8])
print find_single_occur_num([12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3, 7])
print find_single_occur_num1([12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3, 7])