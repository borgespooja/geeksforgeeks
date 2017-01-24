# find the delta min(abs min diff) between two elements from two different array
# approach1:using binary search, (m+n)logm
def q_sort(a):
	if not a:
		return []
	return q_sort([i for i in a[1 : ] if i < a[0]]) + [a[0]] + q_sort([i for i in a[1 : ] if i >= a[0]])

def find_min(a, x, l, u):
	return a[l] if abs(a[l] - x) < abs(a[u] - x) else a[u]
	
def b_search(a, x, s, e):
	if s > e:
		return find_min(a, x, s, e)
	mid = (s + e) / 2
	if a[mid] is x:
		return x
	if x < a[mid]:
		return b_search(a, x, s, mid-1)
	else:
		return b_search(a, x, mid+1, e)
	
def find_closest_diff(a, b):
	a = q_sort(a)
	min_diff = abs(a[0] - b[0])
	for b_num in b:
		a_min = b_search(a, b_num, 0, len(a)-1)
		if abs(b_num - a_min) < min_diff:
			min_diff = abs(b_num - a_min)
	return min_diff	

#approach2: similar to merge sort, when both the arrays are already sorted comlexity- (m+n) , else (m+n+mlogm+nlogm)
def find_closest_diff_2(a, b):
	a = q_sort(a)
	b = q_sort(b)
	i,j = 0,0
	min_dif = abs(a[0] - b[0])
	while (i < len(a)) and (j < len(b)):
		if abs(a[i] - b[j]) < min_dif:
			min_dif = abs(a[i] - b[j])
		if a[i] <= b[j]:
			i += 1
		elif a[i] >= b[j]:
			j += 1
	return min_dif
	
			
def main():
	print find_closest_diff([-4, 7, 57, 98, 999], [99, 57])
	print find_closest_diff_2([-4, 7, 57, 98, 999], [99, 57])
	print find_closest_diff([-3,1,999],[-1,2,3])
	print find_closest_diff_2([-3,1,999],[-1,2,3])
main()	
 	
		