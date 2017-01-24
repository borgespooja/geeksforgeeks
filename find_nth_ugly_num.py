# find nth ugly number- number whose only prime factors are 2,3 or 5
# approach 1: naive method
def max_divide(a, b):
	while not (a % b):
		a /= b
	return a

def is_ugly(n):
	n = max_divide(n, 2)
	n = max_divide(n, 3)
	n = max_divide(n, 5)
	return 1 if n is 1 else 0
	
def get_nth_ugly_num(n):
	i = 1
	u_count = 1
	while n > u_count:
		i += 1
		if is_ugly(i):
			u_count += 1
	return i		

# approach 2: DP using tabulation
def get_nth_ugly_num_DP(n):
	ugly = [0]*n
	ugly[0] = 1
	next_ugly_num = 1
	i2,i3,i5 = 0,0,0
	next_mul_2, next_mul_3, next_mul_5 = 2, 3, 5
	i = 1
	while i < n:
		next_ugly_num = min(next_mul_2, next_mul_3, next_mul_5)
		if next_ugly_num != ugly[i-1]:
			ugly[i] = next_ugly_num
			i += 1
		else:
			i -= 1
		if next_ugly_num == next_mul_2:
			i2 += 1
			next_mul_2 = ugly[i2] * 2
		if next_ugly_num == next_mul_3:
			i3 += 1
			next_mul_3 = ugly[i3] * 3
		if next_ugly_num == next_mul_5:
			i5 += 1
			next_mul_5 = ugly[i5] * 5
	return next_ugly_num
	
def main():
	print get_nth_ugly_num(150)
	print get_nth_ugly_num_DP(150)
main()	