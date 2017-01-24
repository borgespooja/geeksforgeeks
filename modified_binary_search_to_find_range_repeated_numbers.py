# Modified binary search to find start and end indices of repeated number in a sorted array
def cust_min(a, b):
	return a if a < b and a is not -1 else b
	
def cust_max(a, b):
	return a if a > b else b

def modified_binary_search(a, l, h, n):
	if l <= h:
		mid = (l + h)/2
		if a[mid] is n:
			n_s = cust_min(modified_binary_search(a, l, mid-1, n), mid)
			n_e = cust_max(modified_binary_search(a, mid+1, h, n), mid)
			if n_s is not mid or n_e is not mid:
				return n_s,n_e
			else:
				return mid
		elif n < a[mid]:
			return modified_binary_search(a, l, mid-1, n)
		else:
			return modified_binary_search(a, mid+1, h, n)
	else:
		return -1
	
print modified_binary_search([1,3,4,8,8,8,10,13,14], 0, 8, 8)
print modified_binary_search([1,3,4,5,8,8,10,13,14], 0, 8, 5)	