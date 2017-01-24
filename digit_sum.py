def digit_sum(n):
	if n < 10 and n >= 0:
		return n
	else:
		dsum = 0
		while n:
			dsum += (n % 10)
			n /= 10
		return dsum

print digit_sum(12)
print digit_sum(98)
		