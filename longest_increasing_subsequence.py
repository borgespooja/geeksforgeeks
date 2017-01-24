# find longest increasing subsequece
#approach1 : using recursion
def lis(a, n , max_lis_len):
	if n is 1:
		return 1
	curr_lis_len = 1
	for i in range(n):
		sub_p_lis_len = lis(a, i, max_lis_len)
		if (a[i] < a[n-1]) and (curr_lis_len < (1 + sub_p_lis_len)):
			curr_lis_len = 1 + sub_p_lis_len
	if max_lis_len < curr_lis_len:
		max_lis_len = curr_lis_len
	return curr_lis_len

def max_lis(a):
	max_lis_len = 1
	return lis(a, len(a), max_lis_len)

# approach2: using overlappng suproblem property DP
def lis_2(a, n):
	lst = [1] * n
	for i in range(n):
		for j in range(i):
			if (a[j] < a[i]) and (lst[i] < (lst[j]+1)):
				lst[i] = lst[j] + 1
		max_lis_len = 0
		for i in range(n):
			if max_lis_len < lst[i]:
				max_lis_len = lst[i]
	return max_lis_len
	
def main():
	print max_lis([10, 22, 9, 33, 21, 50, 41, 60])
	print lis_2([10, 22, 9, 33, 21, 50, 41, 60], 8)
main()

	