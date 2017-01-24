# sort k sorted array: in which every val is k distance away from its actual postion

# appproach 1: using insertion sort, inner loop will run atmost k times - compexity is O(nk)
def insertion_sort(a):
	for i in range(1, len(a)):
		j = i - 1
		k = a[i]
		while j >= 0 and a[j] >= k:
			a[j + 1] = a[j]
			j -= 1
		a[j + 1] = k
	print a
	
insertion_sort([2,6,3,12,56,8])	
			
#approach 2: using heap
def parent(i):
	return (i - 1) >> 1

def left(i):
	return (i << 1) + 1

def right(i):
	return (i + 1) << 1

def min_heapify(a, i, heap_size):
	l = left(i)
	r = right(i)
	smallest = i
	if l < heap_size and a[l] < a[i]:
		smallest = l
	if r < heap_size and a[r] < a[smallest]:
		smallest = r
	if smallest is not i:
		a[i],a[smallest] = a[smallest],a[i]
		min_heapify(a, smallest, heap_size)
		
def build_min_heap(a, heap_size):
	for i in range((heap_size >> 1) - 1, -1, -1):
		min_heapify(a, i, heap_size)

def extract_min(a, heap_size):
	min_elem = a[0]
	a[0] = a[heap_size - 1]
	heap_size -= 1
	min_heapify(a, 0, heap_size)

def replace_min(a, x, heap_size):
	min_elem = a[0]
	a[0] = x
	if min_elem < x:
		min_heapify(a, 0, heap_size)
		
		
def insert_heap(a, heap_size):
	heap_size += 1
		
	
def sort_k_sorted_elems_using_min_heap(a, k):
	result = []
	heap_size = k + 1
	build_min_heap(a, heap_size)
	ti = 0
	for i in range(k+1,n):
		if i < n:
			result.append(replace_min(a,a[i] heap_size))
		else:
			result.append(extract_min(a, heap_size))
			