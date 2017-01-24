def turn_off_rightmost_set_bit(n):
	return n&(n-1)
	
print '12',bin(12)[2:], bin(turn_off_rightmost_set_bit(12))[2:]
print '4',bin(4)[2:], bin(turn_off_rightmost_set_bit(4))[2:] 
print '7',bin(7)[2:], bin(turn_off_rightmost_set_bit(7))[2:]	