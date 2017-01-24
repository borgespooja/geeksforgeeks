def q_sort(a):
	if not len(a):
		return []
	return q_sort([i for i in a[1:] if i <= a[0]]) + [a[0]] + q_sort([i for i in a[1:] if i > a[0]])


def has_sum(a, s):
	a = q_sort(a)
	l = 0
	r = len(a) - 1
	while l < r:
		if (a[l] + a[r]) is s:
			print "pair with given sum is : ", a[l],a[r]
			return 
		elif (a[l] + a[r]) < s:
			l += 1
		else:
			r -= 1

def has_sum_1(a, s):
	dict = {u:0 for u in range(100000)}
	for i in a:
		if (s - i >= 0) and dict[s-i] is 1:
			print "pair with sum is : ",i, s-i
		dict[i] = 1 
			
has_sum([1,4,45,6,10,-8], 16)
has_sum_1([1,4,45,6,10,-8], 16)