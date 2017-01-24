def max_contiguous_sum(a):
	max_sum = a[0]
	cur_sum = 0
	for i in a:
		if cur_sum < 0:
			cur_sum = i
		else:
			cur_sum += i
		max_sum = max(max_sum, cur_sum)
	return max_sum

def main():
	print max_contiguous_sum([-1,8,-16,4,7,90,23,-40])
	
main()	