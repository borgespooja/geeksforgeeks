# find k smallest element in unsorted array
def parent(i):
	return (i-1)>>1
	
def left(i):
	return (i<<1)+1

def right(i):
	return (i<<1)+2
	
def min_heapify(a, i, heap_size):
	l = left(i)
	r = right(i)
	largest = i
	if l <= heap_size and a[l] < a[i]:
		largest = l
	if r <= heap_size and a[r] < a[largest]:
		largest = r
	if largest is not i:
		a[i],a[largest] = a[largest],a[i]
		min_heapify(a, largest, heap_size)
		
def build_heap(a, k):
	for i in range(k>>1, -1, -1):
		min_heapify(a, i, k)

def get_min(a):
	return a[0]

def replace_min(a,x, k):
	a[0] = x
	min_heapify(a, 0, k)
	
def find_k_smallest_using_min_heap(a, k):
	n = len(a)
	build_heap(a, k)
	for i in range(k, n):
		if a[i] > get_min(a):
			replace_min(a, a[i], k)
			
	return get_min(a)

print find_k_smallest_using_min_heap([12, 3, 5, 7, 19], 4)	
		