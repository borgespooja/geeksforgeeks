# WAP to find k largest/smallest elements in an array

# approach 1: using bubble sort, O(n*k)
def find_k_largest_using_bubble_sort(a, k):
	n = len(a)
	newn = 0
	ki = k
	while n and k:
		for i in range(1,n):
			if a[i-1] > a[i]:
				a[i-1],a[i] = a[i],a[i-1]
				newn = i
		k -= 1
		n = newn
	return a[len(a)-ki:] if ki <= len(a) else a	

def find_k_smallest_using_bubble_sort(a, k):
	n = len(a)
	newn = 0
	ki = k
	while n and k:
		for i in range(1,n):
			if a[i-1] < a[i]:
				a[i-1],a[i] = a[i],a[i-1]
				newn = i
		k -= 1
		n = newn
	return a[len(a)-ki:] if ki <= len(a) else a
 	
# approach 2: using quick sort O(nlogn + k) => O(nlogn)
def q_sort(a):
	if not a:
		return []
	return q_sort([i for i in a[1:] if i < a[0]]) + [a[0]] + q_sort([i for i in a[1:] if i >= a[0]])

def find_k_largest_using_quick_sort(a, k):
	a = q_sort(a)
	return a[len(a)-k:] if k <= len(a) else a

def find_k_smallest_using_quick_sort(a, k):
	a = q_sort(a)
	return a[:k] if  k <= len(a) else a

# approach 3: using selection sort, O(n*k)

def find_k_smallest_using_selection_sort(a, k):
	n = len(a)
	for i in range(k):
		min_idx = i
		for j in range(i+1,n): 
			if a[min_idx] > a[j]:
				min_idx = j
		a[i], a[min_idx] = a[min_idx],a[i]
	return 	a[:k]
	
def find_k_largest_using_selection_sort(a, k):
	n = len(a)
	for i in range(k):
		max_idx = i
		for j in range(i+1,n): 
			if a[max_idx] < a[j]:
				max_idx = j
		a[i], a[max_idx] = a[max_idx],a[i]
	return 	a[:k]
	
# approach 4: using temp array of size k, O((n-k)*k)

def find_k_largest_using_temp_array(a, k):
	temp = a[:k]
	min_idx = temp.index(min(temp))
	n = len(a)
	for i in range(k,n):
		if a[i] > temp[min_idx]:
			temp[min_idx] = a[i]
			min_idx = temp.index(min(temp))
	return temp

def find_k_smallest_using_temp_array(a, k):
	temp = a[:k]
	max_idx = temp.index(max(temp))
	n = len(a)
	for i in range(k,n):
		if a[i] < temp[max_idx]:
			temp[max_idx] = a[i]
			max_idx = temp.index(max(temp))
	return temp
	
# approach 5: using min and max heap
def parent(i):
	return i>>1
	
def left(i):
	return i << 1

def right(i):
	return ((i<<1) | 1)

def heapify_max(a, i, heap_size):
	l = left(i)
	r = right(i)
	largest = i
	if l < heap_size and a[l] > a[i]:
		largest = l
	if r < heap_size and a[r] > a[largest]:
		largest = r
	if largest is not i:
		a[i],a[largest] = a[largest], a[i]
		heapify_max(a, largest, heap_size)

def heapify_min(a, i, heap_size):
	l = left(i)
	r = right(i)
	largest = i
	if l < heap_size and a[l] < a[i]:
		largest = l
	if r < heap_size and a[r] < a[largest]:
		largest = r
	if largest is not i:
		a[i],a[largest] = a[largest], a[i]
		heapify_min(a, largest, heap_size)
		
def build_max_heap(a, heap_size):
	for i in range(len(a)/2, -1, -1):
		heapify_max(a, i, heap_size)

def build_min_heap(a, heap_size):
	for i in range(len(a)/2, -1, -1):
		heapify_min(a, i, heap_size)
		
def find_k_largest_using_heap_sort(a, k):
	heap_size = len(a)
	n = len(a)-1
	build_max_heap(a, heap_size)
	for i in range(n, n-k, -1):
		a[0],a[i] = a[i],a[0]
		heap_size -= 1
		heapify_max(a, 0, heap_size)
	return a[n-k+1:]
	
def find_k_smallest_using_heap_sort(a, k):	
	heap_size = len(a)
	n = len(a) - 1
	build_min_heap(a, heap_size)
	for i in range(n, n-k, -1):
		a[0],a[i] = a[i],a[0]
		heap_size -= 1
		heapify_min(a, 0, heap_size)
	return a[n-k+1:]

def main():
	a = [1, 23, 12, 9, 30, 2, 50]
	k = 3
	print "finding k largest:"
	print find_k_largest_using_bubble_sort(a, k)
	print find_k_largest_using_quick_sort(a, k)
	print find_k_largest_using_selection_sort(a, k)
	print find_k_largest_using_temp_array(a, k)
	print find_k_largest_using_heap_sort(a, k)
	print "finding k smallest:"
	print find_k_smallest_using_bubble_sort(a, k)
	print find_k_smallest_using_quick_sort(a, k)
	print find_k_smallest_using_selection_sort(a, k)
	print find_k_smallest_using_temp_array(a, k)
	print find_k_smallest_using_heap_sort(a, k)
	
main()	
	
	