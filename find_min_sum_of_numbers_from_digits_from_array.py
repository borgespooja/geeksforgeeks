# fin the sum of two numbers formed by the digits givn in an array

# using min heap

def parent(i):
	return ((i - 1) >> 1)

def left(i):
	return (i << 1) + 1
	
def right(i):
	return (i << 1) + 2

def min_heapify(a, i, heap_size):
	l = left(i)
	r = right(i)
	smallest = i
	if l < heap_size and (a[l] < a[i]):
		smallest = l
	if r < heap_size and (a[r] < a[smallest]):
		smallest = r
	if smallest is not i:
		a[i], a[smallest] = a[smallest], a[i]
		min_heapify(a, smallest, heap_size)
		
def build_min_heap(a, heap_size):
	for i in range(heap_size >> 1, -1, -1):
		min_heapify(a, i, heap_size)

def extract_min(a, heap_size):
	min_elem = a[0]
	a[0], a[heap_size - 1] = a[heap_size - 1], a[0]
	heap_size -= 1
	min_heapify(a, 0, heap_size)
	return min_elem
	
def find_min_sum(a):
	heap_size = len(a)
	build_min_heap(a, heap_size)
	b,c = [],[]
	while heap_size > 0:
		b.append(extract_min(a, heap_size))
		heap_size -= 1
		if heap_size > 0:
			c.append(extract_min(a, heap_size))
			heap_size -= 1
	b_sum, c_sum = 0, 0
	for i in range(len(b)):
		b_sum += (b[i] * pow(10,len(b)-i-1))
	for j in range(len(c)):
		c_sum += (c[j] * pow(10,len(c)-j-1))
	return b_sum + c_sum

def main():
	print find_min_sum([6, 8, 4, 5, 2, 3])	
	print find_min_sum([5, 3, 0, 7, 4])	
	
main()	