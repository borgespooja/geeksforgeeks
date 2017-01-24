# convert min heap to max heap : this can be done by simple build_max_heap method in bottom-up manner, since buil heap takes O(n) time to build heap from an unsorted array
# build takes O(n) time, proof:http://net.pku.edu.cn/~course/cs101/2007/resource/Intro2Algorithm/book6/chap07.htm 

def parent(i):
	return (i - 1) >> 1
	
def left(i):
	return (i << 1)	+ 1
	
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
	for i in range(((heap_size) >> 1) - 1, -1, -1):
		max_heapify(a, i, heap_size)
		
def main():
	a = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]			
	heap_size = len(a)
	build_max_heap(a, heap_size)
	print a
	
main()	