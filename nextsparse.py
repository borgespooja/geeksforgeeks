def nextsparse(x):
	a = []
	while x:
		a.append(x & 1)
		x >>= 1
	a.append(0)
	lf = 0
	for i in range(1,len(a)-1):
		if (a[i] is 1) and (a[i-1] is 1) and (a[i+1] is not 1):
			a[i + 1] = 1
			for j in range(i,lf-1,-1):
				a[j] = 0
			lf = i + 1
	ans = 0
	for i in range(len(a)):
		ans += a[i] * (1 << i)
	return ans

print nextsparse(4)
print nextsparse(38)
print nextsparse(6)	
print nextsparse(44)	