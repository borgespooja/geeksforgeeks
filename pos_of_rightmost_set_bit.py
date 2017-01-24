import math
def pos_of_rightmost_set_bit(n):
	return int(math.ceil(math.log((n&-n),2)+1))
	
print pos_of_rightmost_set_bit(12)
print pos_of_rightmost_set_bit(4)
print pos_of_rightmost_set_bit(16)
	