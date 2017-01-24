def segregate_0s_1s(a):
	c, n = 0, len(a) 
	for i in a:
		if not i:
			c += 1
	for i in range(n):
		if c:
			a[i] = 0
			c -= 1
		else:
			a[i] = 1
	return a	
	
def segregate_0s_1s_1(a):
	l, r = 0, len(a)-1
	while l < r:
		while (not a[l]) and (l < r):
			l += 1
		while (a[r]) and (l < r):
			r -= 1
		if l < r:
			a[l], a[r] = a[r], a[l]
			
	return a

print segregate_0s_1s([0, 1, 0, 1, 0, 0, 1, 1, 1, 0])
print segregate_0s_1s_1([0, 1, 0, 1, 0, 0, 1, 1, 1, 0])	