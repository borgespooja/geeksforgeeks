# given infinte coins with values in s, determine the total number of solutions 
# to form value of 'n'
# order does not matter

# approach 1: recursive solution
def count_coin_change_solutions(s,m,n):
	if n is 0:
		return 1
	if n < 0:
		return 0
	if (m <= 0) and (n >= 1):
		return 0
	return count_coin_change_solutions(s,m-1,n) + count_coin_change_solutions(s,m,n-s[m-1])

# approach 2: DP, tabulation

def count_coin_change_solutions_DP(s,m,n):
	tab = [0] * (n+1)
	tab[0] = 1
	for i in range(m):
		for j in range(s[i], n+1):
			tab[j] += tab[j-s[i]]
	return tab[n]
	
print count_coin_change_solutions([1,2,3], 3, 4)
print count_coin_change_solutions([2,5,3,6], 4, 10)
	
print count_coin_change_solutions_DP([1,2,3], 3, 4)
print count_coin_change_solutions_DP([2,5,3,6], 4, 10)
	