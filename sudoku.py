class Sudoku_elem:
	def __init__(self,x,y,val):
		self.x = x
		self.y = y
		self.val = val
		
def sudoku_init():
	sudoku = [[None]*9 for i in range(9)]
		
	for i in range(9):
		for j in range(9):
			se = Sudoku_elem(i,j,None)
			sudoku[i][j] = se

	sudoku[0][2].val = 7
	sudoku[0][4].val = 3
	sudoku[0][6].val = 8
	sudoku[1][3].val = 2
	sudoku[1][5].val = 5
	sudoku[2][0].val = 4
	sudoku[2][3].val = 9		
	sudoku[2][5].val = 6		
	sudoku[2][8].val = 1
	sudoku[3][1].val = 4		
	sudoku[3][2].val = 3
	sudoku[3][6].val = 2
	sudoku[3][7].val = 1
	sudoku[4][0].val = 1
	sudoku[4][8].val = 5
	sudoku[5][1].val = 5		
	sudoku[5][2].val = 8
	sudoku[5][6].val = 6
	sudoku[5][7].val = 7
	sudoku[6][0].val = 5 
	sudoku[6][3].val = 1
	sudoku[6][5].val = 8
	sudoku[6][8].val = 9
	sudoku[7][3].val = 5	
	sudoku[7][5].val = 3
	sudoku[8][2].val = 2
	sudoku[8][4].val = 9
	sudoku[8][6].val = 5

	return sudoku
	
def init_pos_q(sudoku): 	
	q = []
	for i in range(9):
		for j in range(9):
			if not sudoku[i][j].val:
				q.append(sudoku[i][j])
	
	return q
	
def find_boundaries(i,j):
	if i in range(3):
		r = range(3)
	elif i in range(3,6):
		r = range(3,6)
	else:
		r = range(6,9)
	if j in range(3):
		return r, range(3)
	if j in range(3,6):
		return r, range(3,6)
	else:
		return r, range(6,9)
			
def check_valid_entry(sud):
	for i in range(9):
		for j in range(9):
			if sud[i][j].val:
				if sud[i][j].val in [sud[r][j].val for r in range(9) if r is not i]:
					return False
				if sud[i][j].val in [sud[i][r].val for r in range(9) if r is not j]:
					return False
				r, c = find_boundaries(i, j)
				if True in [True if (sud[k][l].val is sud[i][j].val) and ((k is not i) and (l is not j)) else False for k in r for l in c]:
					return False
	return True				
					
				
def is_valid_sudoku(r, sudoku):
	temp_sudoku = sudoku[:]
	for i in r:
		temp_sudoku[i.x][i.y].val = i.val
		if not check_valid_entry(temp_sudoku):
			return False,temp_sudoku
	return True,temp_sudoku
	
def is_sudoku_full(sudoku):
	for i in range(9):
		for j in range(9):
			if not sudoku[i][j].val:
				return False
	return True			
def print_sudoku(r, sudoku):
	flag, temp_sudoku = is_valid_sudoku(r, sudoku) 
	if flag and is_sudoku_full(temp_sudoku):
		for i in range(9):
			for j in range(9):
				print temp_sudoku[i][j].val,
			print "\n"
	return
	
def find_sudoku_value(q, r, sudoku):
	import pdb
	pdb.set_trace()
	if not q:
		print_sudoku(r, sudoku)
		return
	else:
		while q:
			e = q.pop()
			r.append(e)
			for i in range(1,10):
				r[-1].val = i
				flag,temp_sudoku = is_valid_sudoku(r, sudoku)	
				if flag:
					find_sudoku_value(q, r, sudoku)
			del r[-1]
			e.val = None
			q.append(e)

def main():
	sudoku = sudoku_init()
	q =	init_pos_q(sudoku)
	find_sudoku_value(q, [], sudoku)
	
main()	