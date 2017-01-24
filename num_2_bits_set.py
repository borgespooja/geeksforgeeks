def num_2_bits_set(n):
	x = 1
	print "print all nums in range with 2 bits set:"
	while n >0:
		y = 0
		while y < x:
			print (1<<x)+(1<<y)
			n -= 1
			if n is 0:
				return
			y += 1
		x += 1

num_2_bits_set(3)		
num_2_bits_set(5)
num_2_bits_set(10)		