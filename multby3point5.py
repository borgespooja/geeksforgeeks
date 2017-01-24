def multbu3point5(n):
	return ((n << 1) + n + (n >> 1)) if not (n%2) else ((n << 1) + n + (n >> 1) + 0.5)

def multbu3point5_1(n):
	return (((n << 3) - n) >> 1) if not (n%2) else ((((n << 3) - n) >> 1) + 0.5)

print multbu3point5(5)
print multbu3point5_1(5)
print multbu3point5(2)
print multbu3point5_1(2)	