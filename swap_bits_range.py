def swap_bits_range(x,n,p1,p2):
	set1 = (x >> p1) & ((1 << n)- 1)
	set2 = (x >> p2) & ((1 << n) - 1)
	xor = set1 ^ set2
	xor = (xor << p1) | (xor << p2)
	return (x ^ xor)

#alternate implementation
def swap_bits_range1(x,n,p1,p2):
	xor = (((x>>p1) ^ (x>>p2)) & ((1 << n) - 1))
	return x ^ ((xor << p1)|(xor << p2))
	
print swap_bits_range(28,2,0,3)	
print swap_bits_range1(28,2,0,3)
print swap_bits_range(47,3,1,5)
print swap_bits_range1(47,3,1,5)