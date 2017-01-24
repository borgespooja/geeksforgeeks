def print_sub_set_util(a, i, n, v, s):
	if (s < 0) or (i >= n):
		return
	if (s is 0):
		for j in range(len(v)):
			print v[j],
		print "\n"	
		return
	print_sub_set_util(a, i+1, n, v, s)
	v.append(a[i])
	print_sub_set_util(a, i+1, n, v, s - a[i])
	v.pop()
	
def print_sub_set(a, n, s):
	v = []
	print_sub_set_util(a, 0, n, v, s)

def main():
	print_sub_set(range(1,6), 5, 5)

main()	