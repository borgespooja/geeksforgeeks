# egg dropping problem
# given n eggs k floors : find min number of drops required without braking eggs, ecide floors from which eggs should be dropped so that total number of trials are minimized
# approach 1: using optial substructure proerty of DP, using recursion

def egg_Drop(n,k):
	if k is 0 or k is 1:
		return k
	if n is 1:
		return k
	min_t, res = k, 0
	for x in range(1,k+1):
		res = max(egg_Drop(n-1, x-1), egg_Drop(n, k-x))
		if res < min_t:
			min_t = res
			
	return min_t + 1

def egg_Drop_DP(n, k):
	eD_DP = [[0] * (k+1) for i in range(n+1)]
	for i in range(1, n+1):
		eD_DP[i][1] = 1
		eD_DP[i][0] = 0
	for j in range(1, k+1):
		eD_DP[1][j] = j
	for i in range(2, n+1):
		for j in range(2, k+1):
			eD_DP[i][j] = k
			for x in range(1, j+1):
				res = 1 + max(eD_DP[i-1][x-1], eD_DP[i][j-x])
				if res < eD_DP[i][j]:
					eD_DP[i][j] = res
	return eD_DP[n][k]

def main():
	print egg_Drop(2, 10)
	print egg_Drop_DP(2, 10)
	
main()	