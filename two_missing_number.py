def two_missing_num(a):
	XOR = a[0]
	for i in range(1, len(a)):
		XOR ^= a[i]
	for i in range(1, len(a) + 3):
		XOR ^= i
	set_r_bit = XOR & ~(XOR - 1)
	x, y = 0, 0
	for i in a:
		if i & set_r_bit:
			x ^= i
		else:
			y ^= i
	for i in range(1,len(a)+3):
		if i & set_r_bit:
			x ^= i
		else:
			y ^= i
	print x,y

two_missing_num([1,3,5,6])

two_missing_num([1,3,5,4,6])
	