# 0-1 knap sack problem

# approach 1: optimal substructure property of DP, using recursion

def ks(W, wt, v, n):
	if (n is 0) or (W is 0):
		return 0
	elif wt[n-1] > W:
		return ks(W, wt, v, n-1)
	else:
		return max(v[n-1]+ks(W-wt[n-1], wt, v, n-1), ks(W, wt, v, n-1))

# approach 2: overlapping subproblems in DP using tabulation
def ks_DP(W, wt, v, n):
	k = [[0] * (W+1) for i in range(n+1)]
	for i in range(n+1):
		for w in range(W+1):
			if (i is 0) or (w is 0):
				k[i][w] = 0
			elif wt[i-1] <= W:
				k[i][w] = max(v[i-1]+k[i-1][w-wt[i-1]], k[i-1][w])
			else:
				k[i][w] = k[i-1][w]
	return k[n][W]
	
def main():
	print ks(50, [10,20,30], [60, 100, 120], 3)
	print ks_DP(50, [10,20,30], [60, 100, 120], 3)	

main()	