def is_majority_in_sorted_array(a, x):
	n = len(a)
	li = ((n/2) + 1) if (n & 1) else (n/2)
	for i in range(li):
		if (a[i] is x) and (a[i + (n/2)] is x):
			return 1
	return 0

def bin_search(a,l,h,x):
	if l <= h:
		mid = (l + h)/2
		if ((mid is 0) or (x > a[mid - 1])) and (a[mid] is x):
			return mid
		elif (x > a[mid]):
			return bin_search(a, mid + 1, h, x)
		else:
			return bin_search(a, l, mid - 1, x)
	return -1

def is_majority_in_sorted_array_1(a,x):
	n = len(a)
	i = bin_search(a, 0, n-1, x)
	if i is -1:
		return 0
	if (((n/2) + i) <= (n-1)) and (a[((n/2) + i)] is x):
		return 1
	else:
		return 0
		
print is_majority_in_sorted_array([1, 2, 3, 3, 3, 3, 10], 3)
print is_majority_in_sorted_array_1([1, 2, 3, 3, 3, 3, 10], 3)		