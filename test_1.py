def row_col_zero(mat):
	if 0 in mat[0]:
		first_row_has_zero = True
	mat[0] = [0 if mat[0][i] is not 0 else -1 for i in range(len(mat))]
	for i in range(1,len(mat)):
		row_already_set = False
		for j in range(len(mat)):
			if (0 in mat[i][j]) or (mat[i][j] is -1 and (mat[0][j] is 0 or row_already_set)):
				row_already_set = true
					
				