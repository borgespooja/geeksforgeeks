def find_even_occurence(a):
	pos,xor = 0,0L
	for i in range(len(a)):
		pos = 1 << a[i]
		xor ^= pos
	for i in range(len(a)):
		pos = 1 << a[i]
		if not (pos & xor):
			print a[i]
			xor ^= pos

find_even_occurence([9, 12, 23, 10, 12, 12, 15, 23, 14, 12, 15])			
			
	