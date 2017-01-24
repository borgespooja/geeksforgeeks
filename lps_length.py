def lps_length(a, i, j):
	if j is i:
		return 1
	elif j is i+1 and (a[i] == a[j]): 
		return 2
	elif (a[i] == a[j]):
		return lps_length(a, i+1, j-1) + 2
	else:
		return max(lps_length(a, i+1, j), lps_length(a, i, j-1))

def lps_length_DP(a):
	L = [[0]*len(a) for i in range(len(a))]
	for i in range(len(a)):
		L[i][i] = 1
	for cl in range(2,len(a)+1):
		for i in range(len(a)-cl+1):
			j = i+cl-1
			if a[i] == a[j] and cl is 2:
				L[i][j] = 2
			elif a[i] == a[j]:
				L[i][j] = L[i+1][j-1] + 2
			else:
				L[i][j] = max(L[i+1][j], L[i][j-1])
	return L[0][len(a)-1]			
				
		
def main():		
	print lps_length("GEEKSFORGEEKS", 0, len("GEEKSFORGEEKS")-1)
	print lps_length("BBABCBCAB", 0, len("BBABCBCAB")-1)
	print lps_length_DP("GEEKSFORGEEKS")
	print lps_length_DP("BBABCBCAB")

main()	