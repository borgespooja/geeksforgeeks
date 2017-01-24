# longest common subsequence

#approach 1 : using recursion, optimal substructure

#If last characters of both sequences match (or X[m-1] == Y[n-1]) then
#LCS(X[0..m-1], Y[0..n-1]) = LCS(X[0..m-2], Y[0..n-2]) + X[n-1]
#Length, L(X[0..m-1], Y[0..n-1]) = 1 + L(X[0..m-2], Y[0..n-2])
#If last characters of both sequences do not match (or X[m-1] != Y[n-1]) then
#LCS(X[0..m-1], Y[0..n-1]) = MAX ( LCS(X[0..m-2], Y[0..n-1]), LCS(X[0..m-1], Y[0..n-2])

def longest(X, Y):
	return X if len(X) > len(Y) else Y
	
def LCS(x , y):
	if (not x) or (not y):
		return ''
	elif x[-1] == y[-1]:
		return LCS(x[ : -1], y[ : -1]) + x[-1]
	else:
		return longest(LCS(x, y[ : -1]), LCS(x[ : -1], y))

#approach 2: overlapping subproblems, using DP tabulation, recheck
def LCS_2(x, y):
	L = [['']*(len(y)) for j in range(len(x))]
	for i in range(len(x)):
		for j in range(len(y)):
			if (i is 0) or (j is 0):
				L[i][j] = ''
			elif x[i-1] == y[j-1]:
				L[i][j] = x[i] + L[i-1][j-1]
			else:
				L[i][j] = longest(L[i-1][j], L[i][j-1])
	return L[len(x)-1][len(y)-1]
def LCS_2_length(x,y):
	L = [[None]*(len(y)+1) for j in range(len(x)+1)]
	for i in range(len(x)+1):
		for j in range(len(y)+1):
			if (i is 0) or (j is 0):
				L[i][j] = 0
			elif x[i-1] == y[j-1]:
				L[i][j] = 1 + L[i-1][j-1]
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])
	return L[len(x)][len(y)]

	
def main():
	lcs = LCS('BANANA', 'ATANA')
	print "lcs of BANANA,ATANA:",lcs, ",length of lcs",len(lcs) 
	#lcs = LCS_2('BANANA', 'ATANA')
	print "lcs_2  length of BANANA,ATANA:",LCS_2_length('BANANA', 'ATANA') 
	lcs = LCS('ABCDGH', 'AEDFHR')
	print "lcs of ABCDGH, AEDFHR:",lcs, ",length of lcs",len(lcs) 
	lcs = LCS('AGGTAB','GXTXAYB')
	print "lcs of AGGTAB,GXTXAY:B",lcs, ",length of lcs",len(lcs) 
	
main()	