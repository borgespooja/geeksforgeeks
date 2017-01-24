def is_sparse(n):
	return not(bool(n & (n>>1)))

print is_sparse(12)
print is_sparse(7)
print is_sparse(72)	