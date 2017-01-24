def msb_pos(a):
	return len(bin(a)[2:])-1
	
def and_op(x, y):
	result = 0
	while x >= 0  and y >= 0:
		msb_x = msb_pos(x)
		msb_y = msb_pos(y)
		if msb_x is not msb_y:
			break
		else:
			msb_val = 1 << msb_x
			result += msb_val
			x -= msb_val
			y -= msb_val
	return result

print and_op(12, 15)	
print and_op(10, 20)	
print and_op(17, 19)	
print and_op(1,15)	


