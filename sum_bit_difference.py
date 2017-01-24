def sum_bit_difference(a):
	ans = 0
	for i in range(31, -1, -1):
		count = 0 
		for j in range(len(a)):
			if a[j] & (1<<i):
				count += 1
		ans += (count * (len(a)-count) * 2)
	return ans

print sum_bit_difference([1,2])
print sum_bit_difference([1,3,5])
	
		