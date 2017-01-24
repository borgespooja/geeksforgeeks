def lighthouse_radius():
	
	lighthouse_list = []
	for _ in range(int(raw_input())):
		lighthouse_list.append(list(raw_input()))
	r = 0	
	center = len(lighthouse_list)/2
	i,j = center,center
	if lighthouse_list[i][j] == '.':
		k = 1
		while i-k >= 0 and j-k >=0 and i+k < len(lighthouse_list) and j+k < len(lighthouse_list):
			if lighthouse_list[i+k][j] == '.' and lighthouse_list[i-k][j] == '.':
				if lighthouse_list[i][j-k] == '.' and lighthouse_list[i][j+k] == '.':
					r += 1
					k += 1
					print i,j,k
			else:
				return r
				
	return r
		

print lighthouse_radius()