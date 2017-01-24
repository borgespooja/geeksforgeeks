def generate_grey_code(n):
	n -= 1
	l1 = ['0','1']
	l2 = l1[::-1]
	while n:
		l1 = ['0'+i for i in l1]
		l2 = ['1'+i for i in l2]
		l1 += l2
		l2 = l1[::-1]
		n -= 1
	return l1	
print generate_grey_code(4)
print generate_grey_code(3)
print generate_grey_code(2)
print generate_grey_code(1)	