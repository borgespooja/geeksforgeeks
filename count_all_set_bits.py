def count_all_set_bits(n):
	bitcount = 0
	for i in range(32):
		for x in range(1,n+1):
			if x & (1<<i):
				bitcount += 1
	return bitcount
	
## alternate implementation
def count_all_set_bits1(n):
	bitcount = 0
	for i in range(1,n+1):
		bitcount += countsetbitutil(i)
	return bitcount

def countsetbitutil(x):
	if x <= 0:
		return 0
	return ((1 if (x % 2) else 0) + count_all_set_bits1(x >> 1))

## alternate approach
#def count_all_set_bits2(n):
	

print count_all_set_bits(3)
print count_all_set_bits(6)
print count_all_set_bits(7)
print count_all_set_bits(8)	
print count_all_set_bits(4)
print "alternate implementation result"
print count_all_set_bits1(3)
print count_all_set_bits1(6)
print count_all_set_bits1(7)
print count_all_set_bits1(8)	
print count_all_set_bits1(4)
	