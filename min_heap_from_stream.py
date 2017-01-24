# WAP to build min heap and max heap from a stream of data
#TODO : program not working as expected, correct it
def parent(i):
	return (i-1) >> 1
	
def left(i):
	return (1 << 1)	+ 1

def right(i):
	return (i + 1) << 1

def heap_insert(a, k, heap_size):
#	import pdb
#	pdb.set_trace()
	heap_size += 1
	i = heap_size
	while i > 0  and a[parent(i)] > k:
		a[i] = a[parent(i)]
		i = parent(i)
	a[i] = k
	
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
		min_heapify(a, smallest, heap_size)

def build_min_heap_stream(a, heap_size):
		n = input("Enter next element in stream : ")
		
def build_min_heap(a, heap_size):
		for i in range(heap_size >> 1 , -1, -1):
			min_heapify(a, i, heap_size)
			
def main():
	heap_size = 0
	a = []
	try:
		while 1:
			n = raw_input("Enter next element in heap : ")
			if n is 'q':
				break
			if not heap_size:
				a.append(int(n))
				heap_size += 1
			else:
				a.append(int(n))
				heap_size += 1
				min_heapify(a, parent(heap_size - 1), heap_size)
		print a[:heap_size], heap_size
	except KeyboardInterrupt:
		print "interrupted!", a

main()		