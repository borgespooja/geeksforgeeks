# n mod d, where  is in pow of 2
def n_mod_d(n,d):
	return (n & (d-1))
	
print n_mod_d(3,4)
print n_mod_d(8,2)
print n_mod_d(19,4)	