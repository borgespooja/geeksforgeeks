def print_bin(n):
	bin_rep = []
	i = 1 << 31
	while i > 0:
		print '1' if n & i else '0',
		i >>= 1
def print_bin_2(n):
	if n > 1:
		print_bin(n/2)
	print n%2
	
print_bin(5)
print ('\n')
print_bin(11)
print ('\n')
print_bin_2(5)
print('\n')
print_bin_2(11)	