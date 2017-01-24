def add_without_add_op(x,y):
	while y:
		carry = (x & y)
		x ^= y
		y = (carry << 1)
	return x

def add_without_add_op_rec(x,y):
	return x if not y else add_without_add_op_rec(x^y, ((x & y) << 1)) 
	
print add_without_add_op(5,6)
print add_without_add_op_rec(5,6)	