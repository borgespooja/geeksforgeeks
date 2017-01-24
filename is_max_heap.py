# find if given array is max_heap
#approach 1: iterative
def is_heap_1(a, n):
	for i in range(n >> 1):
		if (((i<<1) + 1) < n) and (a[(i << 1) + 1] > a[i]):
			return False
		if (((i<<1) + 2) < n) and (a[(i << 1) + 2] > a[i]):
			return False
	return True
	
#TODO: approach 2 giving wrong answer , recheck
# approach 2: recursive, using fact that last internal node is at index (n-1)/2, in 0-based indexing	
def is_heap(a, i, n):
	#import pdb
	#pdb.set_trace()
	#leaf node
	if i > ((n-2) >> 1):
		return True
	l = (i << 1) + 1 #left
	r = (i << 1) + 2 #right
	#internal node
	if ((l < n) and (a[i] >= a[l])):
		return is_heap(a, l, n)
	if ((r < n) and (a[i] >= a[r])):
		return is_heap(a, r, n)
	return False

def main():
	print is_heap_1([90, 15, 10, 7, 12, 2, 7, 3], 8)
	print is_heap([90, 15, 10, 7, 12, 2, 7, 3], 0, 8)

main()	
		

	
			