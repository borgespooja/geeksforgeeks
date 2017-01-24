# finding duplicates in an array of size n , elements ranging from 0 to n-1

def find_duplicates(a):
	for i in range(len(a)):
		if a[abs(a[i])] >= 0:
			a[abs(a[i])] = -a[abs(a[i])]
		else:
			print abs(a[i]),
	print "\n"

find_duplicates([1, 2, 3, 1, 3, 6, 6])	