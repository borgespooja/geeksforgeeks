def mark_adjacent_island(a,i,j,m,n):
	flag = False
	if (i+1 < m) and  (j < n) and a[i+1][j]:
		a[i+1][j] += 1
		flag = True
	if (i-1 >= 0) and (j<n) and a[i-1][j]:
		a[i-1][j] += 1
		flag = True
	if (i < m)	and (j+1 < n) and a[i][j+1]:
		a[i][j+1] += 1
		flag = True
	if (i < m)	and (j-1 >= 0) and a[i][j-1]:
		a[i][j-1] += 1
		flag = True
	return flag	
		
		
def count_island(a):
	i_count = 0
	for i in range(len(a)):
		for j in range(len(a[0])):
			if a[i][j]:
				flag = mark_adjacent_island(a,i,j,len(a),len(a[0]))
				if a[i][j] is 1:
					i_count += 1 
				if flag:
					a[i][j] += 1
			else:
				continue
	print i_count

count_island(
			[[1,1,0,1,0],
			 [0,1,0,0,1],
			 [0,0,0,0,0],
			 [1,0,1,0,1]
			]
			)	
			
count_island(
			[[0,0,0,0,0],
			 [0,1,1,0,0],
			 [0,0,1,1,0],
			 [0,0,0,0,1],
			 [0,0,0,1,0]
			]
			)			