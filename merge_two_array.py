#There are two sorted arrays. First one is of size m+n containing only m elements. Another one is of size n and contains n elements. Merge these two arrays into the first array of size m+n such that the output is sorted.
def move_elem_to_end(a):
	j = len(a) - 1
	for i in range(len(a)-1, -1, -1):
		if a[i]:
			a[j] = a[i]
			j -= 1
	return a

def merge(a, b):
	n = len(b)
	m = len(a) - n
	i, j, k = n, 0, 0
	while k < (m+n):
		if ((i<(m+n)) and (a[i] <= b[j])) or (j is n):
			a[k] = a[i]
			k += 1
			i += 1
		else:
			a[k] = b[j]
			k += 1
			j += 1
	return a

def main():
	a = move_elem_to_end([2, 8, None, None, None, 13, None, 15, 20])
	b = [5, 7, 9, 25]
	a = merge(a,b)
	print a
	
main()	