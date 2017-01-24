def max_contiguous_product(a):
	max_prod = 1
	cur_prod = 1
	neg_prod = 1
	for i in a:
		if i is 0:
			cur_prod = 1
			neg_prod = 1
		elif i < 0:
			neg_prod *= i
		else:
			cur_prod *= i
		max_prod = max(cur_prod * neg_prod , cur_prod, max_prod)
	return max_prod
	
def main():
	print max_contiguous_product([2,-5,-3,0,7,1,-4,3,-10])#840
	print max_contiguous_product([-1,8,-16,4,7,90,23,-40])#296755200, TODO: check for such input, output is wrong	
	
main()	
			