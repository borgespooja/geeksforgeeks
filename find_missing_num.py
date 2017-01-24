# given a sorted array of len "n" with elements ranging between 0 to m-1, find smallest missing number
def find_missing_num_lin(a):
	for i in range(len(a)):
		if a[i] is not i:
			return i

def find_missing_num_lin2(a):
	for i in range(len(a) - 1):
		if (a[i+1] - a[i]) > 1:
			return a[i]+1
			
def find_missing_num_bs(a,l,h):
	if l > h:
		return h+1
	if a[l] is not l:
		return l
	mid = (l+h)/2	
	if a[mid] > mid:
		return find_missing_num_bs(a, l, mid)
	else:
		return find_missing_num_bs(a, mid+1, h)


print find_missing_num_lin([0, 1, 2, 3, 4, 5, 6, 7, 10])
print find_missing_num_lin([0, 1, 2, 3, 4, 5, 6, 7, 10])
print find_missing_num_bs([0, 1, 2, 3, 4, 5, 6, 7, 10], 0, 9)		