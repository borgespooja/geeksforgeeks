# finding min number of operations required in matrix chain multiplication
# given is p[1....n]: dimension of n-1 matrices such that matrix Ai has dimension p[i-1]*p[i]
# n matrices can be multiplied in n-1 ways

# approach 1: using recursion-optimal substructure property DP-solution of subproblems leads to final solution 
import sys
def min_op_matrix_chain_multi(p, i, j):
	if i is j:
		return 0
	count = 0
	min_op = sys.maxint
	for k in range(i,j):
		count = min_op_matrix_chain_multi(p, i, k)+min_op_matrix_chain_multi(p, k+1, j)+(p[i-1] * p[k] * p[j])
		min_op = min(count, min_op)
	return min_op

# approach 2: using overlapping subproblems property DP	, tabulation
def min_op_matrix_chain_multi_DP(p , n):
	m = [[0]*n for i in range(n)]
	for i in range(1,n):
		m[i][i] = 0
	for l in range(2,n):
		for i in range(1,n-l+1):
			j = i+l-1
			m[i][j] = sys.maxint
			for k in range(i,j):
				q = m[i][k] + m[k+1][j] + (p[i-1] * p[k] * p[j])
				if q < m[i][j]:
					m[i][j] = q
	return m[1][n-1]

	
		
def main():
	p = [1,2,3,4]
	i = 1
	j = len(p) - 1	
	print min_op_matrix_chain_multi(p, i, j)
	print min_op_matrix_chain_multi_DP(p, j+1)
main()	