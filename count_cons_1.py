def count_non_cons_1(n):
	a,b = [],[]
	a.append(1)
	b.append(1)
	for i in range(1,n):
		a.append(a[i-1] + b[i-1])
		b.append(a[i-1])
	return a[n-1]+b[n-1]

def count_cons_1(n):
	return (2**n)-count_non_cons_1(n)

print count_cons_1(8)
print count_cons_1(10)
print count_cons_1(3)
print count_cons_1(5)	
	