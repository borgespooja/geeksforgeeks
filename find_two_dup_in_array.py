#find 2 duplicates in array of size n+2 and elements in range 1 to n
# approach 1: brute force
def find_two_dup_bf(a):
	for i in range(len(a)):
		count = 0
		for j in range(len(a)):
			if a[i] is a[j]:
				count += 1
		if count is 2:
			print a[i],
	print "\n"		

# approach 2: using num count
def find_two_dup_num_count(a):
	count = [0] * (len(a)-1)
	for i in a:
		count[i] += 1
	for i in range(1,len(count)):
		if count[i] is 2:
			print i,
	print "\n"
	
# approach 3: using sum and diff formula
def fact(n):
	if n is 1 or n is 0:
		return 1
	return (n* fact(n-1))
	
def find_two_dup_sum_diff(a):
	s = sum([i for i in a])
	p = 1
	for i in a:
		p *= i
	n = len(a) - 2	
	s = s - ((n * (n+1)) / 2)
	p = p / fact(n)
	import math
	d = math.sqrt((s*s) - (4*p))
	x = (s+d)/2
	y = (s-d)/2
	print int(x),int(y)
	
# approach 4: using xor
def find_two_dup_xor(a):
	xor,x,y = 0,0,0
	for i in a:
		xor ^= i
	for i in range(1,len(a)-1):
		xor ^= i
	set_bit_no = (xor & (~(xor-1) & 0xFF))
	n = len(a) - 1
	for i in a:
		if i & set_bit_no:
			x ^= i
		else:
			y ^= i
	for i in range(1,n):
		if (i & set_bit_no):
			x ^= i
		else:
			y ^= i
	print x,y

# approach 5: using negation of num
def find_two_dup_neg_num(a):
	for i in range(len(a)):
		if a[abs(a[i])] > 0:
			a[abs(a[i])] = -a[abs(a[i])]
		else:
			print abs(a[abs(a[i])]),
			
find_two_dup_bf([4, 2, 4, 5, 2, 3, 1])
find_two_dup_num_count([4, 2, 4, 5, 2, 3, 1])
find_two_dup_sum_diff([4, 2, 4, 5, 2, 3, 1])
find_two_dup_xor([4, 2, 4, 5, 2, 3, 1])			
find_two_dup_neg_num([4, 2, 4, 5, 2, 3, 1])
			