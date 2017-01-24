def number_occur_odd_times(a):
	res = 0
	for i in a:
		res ^= i
	return res

print number_occur_odd_times([1, 2, 3, 2, 3, 1, 3])

