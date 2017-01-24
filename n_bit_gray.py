def gen_gray(n):
	a = []
	a.append('0')
	a.append('1')
	i = 2
	while i < (1<<n):
		for j in range(i-1,-1,-1):
			a.append(a[j])
		for j in range(0,i):
			a[j] = '0' + a[j]
		for j in range(i,2*i):
			a[j] = '1' + a[j]
		i = i << 1
	for i in range(len(a)):
		print a[i]
print "4 bit gray code"		
gen_gray(4)
print "3 bit gray code"		
gen_gray(3)
print "2 bit gray code"		
gen_gray(2)
print "1 bit gray code"		
gen_gray(1)
		