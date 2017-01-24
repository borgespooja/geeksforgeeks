def completepair(set1,set2):
	con_s1 = [0] * len(set1)
	con_s2 = [0] * len(set2)
	for i in range(len(set1)):
		con_s1[i] = 0
		for j in range(len(set1[i])):
			con_s1[i] = con_s1[i] | (1<<(ord(set1[i][j]) - ord('a')))
			
	for i in range(len(set2)):
		con_s2[i] = 0
		for j in range(len(set2[i])):
			con_s2[i] = con_s2[i] | (1<<(ord(set2[i][j]) - ord('a')))
			
	complete = (1 << 26)-1
	count = 0
	for i in range(len(set1)):
		for j in range(len(set2)):
			print bin(con_s1[i] | con_s2[j])[2:]
			if (con_s1[i] | con_s2[j]) == complete:
				count += 1
	
	print count

completepair(["abcdefgh", "geeksforgeeks", "lmnopqrst", "abc"],["ijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "defghijklmnopqrstuvwxyz"])
	