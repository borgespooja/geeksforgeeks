# WAF that takes 2 parameters 'n' and 'k' and returs the value of binomial Coefficient C(n,k)
# approach 1 : optimal substructure property of DP and using recursion
def binomial_coef(n, k):
	if (k is 0) or (k is n):
		return 1
	return binomial_coef(n-1, k-1) + binomial_coef(n-1, k)


# approach 2: overlapping subproblem property of DP, tabulisation
def binomial_coef_DP(n, k):
	c = [[0]*(k+1) for i in range(n+1)]
	for i in range(n+1):
		for j in range(min(i,k)+1):
			if (j is 0) or (j is i):
				c[i][j] = 1
			else:
				c[i][j] = c[i-1][j-1] + c[i-1][j]
	return c[n][k]			

# approach 3: DP but spae efficient tabulisation	
def binomial_coef_DP_2(n, k):
	c = [0] * (k+1)
	c[0] = 1
	for i in range(1, n+1):
		for j in range(min(i,k), 0, -1):
			c[j] = c[j] + c[j-1]
	return c[k]
	
def main(): 
	print binomial_coef(5, 2)
	print binomial_coef_DP(5, 2)	
	print binomial_coef_DP_2(5, 2)
	
main()	