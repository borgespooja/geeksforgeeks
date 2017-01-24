# You are given an array of integers(with all valid input) You have to write a function which will produce another array,
# where the value in each index of the array will be the product of all values in the given array accept that index. 

def prod_array(a):
	if not a:
		return
	zi = -1
	zeroed_list = False
	prod = 1
	B = []
	for i in range(len(a)):
		if a[i] is 0:
			if zi is -1:
				zi = 1
			else:
				zeroed_list = True
		else:
			prod *= a[i]
	for i in range(len(a)):
		if ((zi is not -1) and (zi is not i)) or zeroed_list:
			B.append(0)
			continue
		if zi is i:
			B.append(prod)
			continue
		B.append(prod/a[i])
	return B

def main():
	print prod_array([1,2,3,4,5])#array without any zero
	print prod_array([1,2,0,4,5])#array with 1 zero
	print prod_array([1,2,0,4,0])#array with more than 1 zero
main()	
			