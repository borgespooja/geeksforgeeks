def is_multiple_of_3(n):
	if not n:
		return 1
	elif n is 1:
		return 0
	odd_count, even_count = 0, 0
	while n > 0:
		if n & 1:
			odd_count += 1
		n >>= 1
		if n & 1:
			even_count += 1
		n >>= 1
	return is_multiple_of_3(abs(odd_count - even_count))
	
print is_multiple_of_3(27)
print is_multiple_of_3(8)	