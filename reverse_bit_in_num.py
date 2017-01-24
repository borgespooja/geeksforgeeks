import math
import sys
def reverse_bits_in_num(n):
	int_size = int(math.ceil(math.log(sys.maxint, 2))) + 1
	reverse_num = 0
	temp = 0
	for i in range(int_size):
		temp = n & (1 << i)
		if temp:
			reverse_num |= (1 << ((int_size-1) - i))
	return reverse_num

def reverse_bits_in_num_1(n):
	int_size = int(math.ceil(math.log(sys.maxint, 2))) + 1
	reverse_num = 0
	for i in range(int_size):
		if (n & (1 << i)):
			reverse_num |= (1 << ((int_size-1)-i))
	return reverse_num

def reverse_bits_in_num_2(n):
	bit_count = int(math.ceil(math.log(sys.maxint, 2)))
	reverse_num = n
	n >>= 1
	while n:
		reverse_num <<= 1
		reverse_num |= (n & 1)
		n >>= 1
		bit_count -= 1
	reverse_num <<= bit_count
	return reverse_num
		
print reverse_bits_in_num(1)
print reverse_bits_in_num_1(1)
print reverse_bits_in_num_2(1) 	