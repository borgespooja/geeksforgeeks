# find k largest element in unsorted array
def parent(i):
	return (i-1)>>1
	
def left(i):
	return (i<<1)+1

def right(i):
	return (i<<1)+2
	
def max_heapify(a, i, heap_size):
	l = left(i)
	r = right(i)
	largest = i
	if l <= heap_size and a[l] > a[i]:
		largest = l
	if r <= heap_size and a[r] > a[largest]:
		largest = r
	if largest is not i:
		a[i],a[largest] = a[largest],a[i]
		max_heapify(a, largest, heap_size)
		
def build_heap(a, k):
	for i in range(k>>1, -1, -1):
		max_heapify(a, i, k)

def get_max(a):
	return a[0]

def replace_max(a,x, k):
	a[0] = x
	max_heapify(a, 0, k)
	
def find_k_largest_using_max_heap(a, k):
	n = len(a)
	build_heap(a, k)
	for i in range(k, n):
		if a[i] < get_max(a):
			replace_max(a, a[i], k)
			
	return get_max(a)

print find_k_largest_using_max_heap([12, 3, 5, 7, 19], 4)	
		