def rev_arr_iter(a, start, end):
	while start < end:
		a[start], a[end] = a[end], a[start]
		start += 1
		end -= 1
	return a

def rev_arr_rec(a, start, end):
	if start >= end:
		return a
	a[start],a[end] = a[end],a[start]
	return rev_arr_rec(a, start+1, end-1)

a = [1,2,3,4,5,6]	

print rev_arr_iter(a, 0, len(a)-1)
a = [1,2,3,4]
print rev_arr_rec(a, 0, len(a)-1)

	