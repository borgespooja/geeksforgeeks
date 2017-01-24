# find kth lrgest element in online stream

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
	if l < heap_size and a[l] < a[i]:
		smallest = l
	if r < heap_size and a[r] < a[smallest]:
		smallest = r
	if smallest is not i:
		a[i], a[smallest] = a[smallest], a[i]
		min_heapify(a, smallest, heap_size)
		
def replace_min(a,x, heap_size):
	a[0] = x
	min_heapify(a, 0, heap_size)
	
def build_heap(a, heap_size):
	for i in range(heap_size >> 1):
		min_heapify(a, i, heap_size)

def get_min(a):
	return a[0]
	
def find_kth_largest_ol_stream(k):
	a = [0] * k
	count,x = 0,0
	while 1:
		x = input("Enter next element of stream : ")
		if count < k-1:
			a[count] = x
			count += 1
		else:
			if count is k-1:
				a[count] = x
				print a
				build_heap(a, k)
				print a
			elif x > get_min(a):
				replace_min(a, x, k)
				print a
			print "kth largest element is : ", get_min(a)
			count += 1
			
			
def main():
	k  = 3
	find_kth_largest_ol_stream(k)
	
main()	
	