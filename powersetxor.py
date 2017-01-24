def powersetxor(set):
	if len(set) is 1:
		return set[0]
	elif len(set) > 1:
		return 0
		
print powersetxor([1,2,3])
print powersetxor([3])	