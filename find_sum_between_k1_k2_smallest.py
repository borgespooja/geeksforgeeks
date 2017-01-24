# find sum of all eements between k1th and k2th smallest

#approach 1, first sort the array and then sum elemnts between k1 and k2 indices
def parent(i):
	return (i - 1) >> 1
	
def left(i):
	return (i << 1) + 1

def right(i):
	return (i << 1) + 2

def max_heapify(a, i, heap_size):
	l = left(i)
	r = right(i)
	largest = i	
	if l < heap_size and a[l] > a[i]:
		largest = l
	if r < heap_size and a[r] > a[largest]:
		largest = r
	if largest is not i:
		a[i], a[largest] = a[largest], a[i]
		max_heapify(a, largest, heap_size)
		
def build_max_heap(a, heap_size):
		for i in range(heap_size >> 1):
			max_heapify(a, i, heap_size)
		
def heap_sort(a, heap_size):
	build_max_heap(a, heap_size)	
	for i in range(len(a) - 1, 0, -1):
		a[0],a[i] = a[i],a[0]
		heap_size -= 1
		max_heapify(a, 0, heap_size)
		
def find_sum_between_k1_k2(a, k1, k2):
		heap_size = len(a)
		heap_sort(a, heap_size)
		return sum(a[k1:k2-1])

# approach 2 : constructing in_heap of all the elements, optimizing above approach
def min_heapify(a, i, heap_size):
	l = left(i)
	r = right(i)
	smallest = i	
	if l < heap_size and a[l] < a[i]:
		smallest = l
	if r < heap_size and a[r] < a[smallest]:
		smallest = r
	if smallest is not i:
		a[i], a[smallest] = a[smallest], a[i]
		max_heapify(a, smallest, heap_size)
		
def build_min_heap(a, heap_size):
		for i in range(heap_size >> 1):
			min_heapify(a, i, heap_size)

def extract_min(a, heap_size):
	min_e = a[0]
	a[0],a[heap_size - 1] =  a[heap_size - 1], a[0]
	heap_size -= 1
	min_heapify(a, 0, heap_size)
	return min_e

def get_min(a):
	return a[0]
	
def find_sum_between_k1_k2_min_heap(a, k1, k2):
	#import pdb
	#pdb.set_trace()
	heap_size = len(a)
	build_min_heap(a, heap_size)
	for i in range(k1):
		extract_min(a, heap_size)
		heap_size -= 1
	sum_elem = 0
	for i in range(k2-k1-1):
		sum_elem += extract_min(a, heap_size)
		heap_size -= 1
	return sum_elem
	
def main():
	print find_sum_between_k1_k2([20, 8, 22, 4, 12, 10, 14], 3, 6)
	print find_sum_between_k1_k2([10, 2, 50, 12, 48, 13], 2, 6)
	print find_sum_between_k1_k2_min_heap([20, 8, 22, 4, 12, 10, 14], 3, 6)
	print find_sum_between_k1_k2_min_heap([10, 2, 50, 12, 48, 13], 2, 6)

main()			