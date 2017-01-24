def xor_without_xor_op(a,b):
	return ((a|b) & ((~a & 0xFF)|(~b & 0xFF)))
	
print xor_without_xor_op(3,5)
print xor_without_xor_op(14,6)
print xor_without_xor_op(2,1)
print xor_without_xor_op(0,1)
	