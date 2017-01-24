# build k-ary heap
#TODO: heap is not correct check all the functions again
#maxHeapify - to restore the max heap  
def restore_down(a, a_len, idx, k):
	child = [0] * (k + 1)
	while 1:
		for i in range(1,k+1):
			child[i] = (k*idx)+1 if ((k*idx)+1) < a_len else -1
		max_child, max_child_idx = -1, 0
		for i in range(1, k+1):
			if (child[i] is not -1) and (a[child[i]] > max_child):
				max_child_idx = child[i]
				max_child = a[child[i]]
		if max_child is -1:
			break
		if a[idx] < a[max_child_idx]:
			a[max_child_idx],a[idx] = a[idx],a[max_child_idx]
		idx = max_child_idx

#decrease_key() and insert() - to restore a given node up in a heap	
def restore_up(a, idx, k):
	parent = (idx - 1) / k
	while parent >= 0:
		if a[idx] > a[parent]:
			a[idx], a[parent] = a[parent], a[idx]
			idx = parent
			parent = (idx - 1) / k
		else:
			break
			
def build_heap(a, n, k):
	for i in range((n-1)/k, -1, -1):
		restore_down(a, n, i, k)
		
		
def insert_heap(a, n, k, elem):
	a[n] = elem
	n += 1
	restore_up(a, n-1, k)
	
	
def extract_max(a, n, k):
	max_elem = a[0]
	a[0] = a[n-1]
	n -= 1
	restore_down(a, n, 0, k)
	return max_elem

def main():
	a = [0] * 100
	a[:7] = [4, 5, 6, 7, 8, 9, 10]
	n, k = 7, 3
	build_heap(a, n, k)
	print "built heap: ", a[:n]
	elem = 3
	insert_heap(a, n, k, elem)
	n += 1
	print "after insertion of 3: ", a[:n]
	print "extracted max is: ", extract_max(a, n, k)
	n -= 1
	print "heap after extract_max: ", a[:n]
	
main()	