def parent(i):
	return (i>>1)

def left(i):
	return (i<<1)
	
def right(i):
	return ((i<<1) | 1)
	
def build_heap(a):
	heap_size = len(a)
	for i in range(len(a)/2,-1,-1):
		heapify(a, i, heap_size)
		
def heapify(a, i, heap_size):
	l = left(i)
	r = right(i)
	largest = i
	if l < heap_size and a[l] > a[i]:
		largest = l
	if r < heap_size and a[r] > a[i]:
		largest = r
	if largest is not i:
		a[i],a[largest] = a[largest],a[i]
		heapify(a, largest, heap_size)

def extract_max(a, heap_size):
	max_elem = 	a[0]
	a[0] = a[heap_size-1]
	heap_size -= 1
	heapify(a, 0, heap_size)
	return max_elem
	
def parent_custom_insert(i):	
	return (i>>1) if (i & 1) else ((i>>1)-1)
	
def insert_key(a, k, heap_size):
	i = heap_size
	while (i > 0) and (a[parent_custom_insert(i)] < k):
		a[i] = a[parent_custom_insert(i)]
		i = parent_custom_insert(i)
	a[i] = k	

def build_heap_using_insert(a):
	heap_size = 0
	for i in range(1, len(a)):
		heap_size += 1
		insert_key(a, a[i], heap_size)
		
def heap_sort(a):
	heap_size = len(a)
	print "before heap conversion",a
	build_heap(a)
	print "after heap conversion",a
	for i in range(len(a)-1,0,-1):
		t = a[i]
		a[i] = a[0]
		a[0] = t
		heap_size -= 1
		heapify(a, 0, heap_size)
	print "after sorting", a	

def heap_sort_using_insert_build(a):
	heap_size = len(a)
	print "before heap conversion",a
	build_heap_using_insert(a)
	print "after heap conversion",a
	for i in range(len(a)-1,0,-1):
		t = a[i]
		a[i] = a[0]
		a[0] = t
		heap_size -= 1
		heapify(a, 0, heap_size)
	print "after sorting", a	
	
heap_sort([3,1,8,0,9])

b = [3,1,8,0,9]	
build_heap(b)
print b

b = [3,1,8,0,9]
build_heap_using_insert(b)
print extract_max(b, len(b))
print b