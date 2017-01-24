def multiply_by_7_by_8_v1(n):
	return (n - (n >> 3))

def multiply_by_7_by_8_v2(n):
	return (((n << 3) - n) >> 3)
	
print multiply_by_7_by_8_v1(9)
print multiply_by_7_by_8_v2(9)

print multiply_by_7_by_8_v1(15)
print multiply_by_7_by_8_v2(15)	