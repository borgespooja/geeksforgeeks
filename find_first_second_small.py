# find first and second smallest elements in array
import sys
def find_first_second_small(a):
	max_val = sys.maxint
	first = max_val
	second = max_val
	for i in a:
		if i < first:
			second = first
			first = i
		elif i < second and (i is not first):
			second = i
	if second is max_val:
		print "no second minimum"
	else:
		print first,second
		
find_first_second_small([12, 13, 1, 10, 34, 1])		
find_first_second_small([1 for i in range(6)])		
			