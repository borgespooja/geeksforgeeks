def sum_bitwise_and(a):
	ans = 0
	for i in range(32):
		k = 0
		for j in range(len(a)):
			if (a[j] & (1<<i)):
				k += 1
		ans += (1<<i) * (k*(k-1)/2)		
	return ans

print sum_bitwise_and([5,10,15])	
print sum_bitwise_and([3,4,5,6,12,13])	