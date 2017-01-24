#finding cost for conversion frm s1 to s2
#ops : insert,remove,replace - all have equal op cost 
#approach 1: using recursion

def edit_distance(s1, s2):
	if not s1:
		return len(s2)
	if not s2:
		return len(s1)
	if s1[-1] == s2[-1]:
		return edit_distance(s1[:-1], s2[:-1])
	return 1 + min(edit_distance(s1, s2[:-1]),
	               edit_distance(s1[:-1], s2),
				   edit_distance(s1[:-1], s2[:-1]))
				   
def edit_distance_DP(s1,s2):
	m = len(s1)
	n = len(s2)
	dp = [[0]*(n+1) for i in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i is 0:
				dp[i][j] = j
			elif j is 0:
				dp[i][j] = i
			elif s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
	return dp[m][n]
	
print edit_distance('sunday', 'saturday')
print edit_distance('geek','gesek')
print edit_distance('cat','cut')
print edit_distance_DP('sunday', 'saturday')
print edit_distance_DP('geek','gesek')
print edit_distance_DP('cat','cut')
				   
	
