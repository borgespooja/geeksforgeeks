#Given two integers n and m, find all the stepping numbers in range [n, m].
#A number is called stepping number if all adjacent digits have an absolute difference of 1.
#321 is a Stepping Number while 421 is not.
def stepping_num_bfs(n,m,num):
	lst = []
	lst.append(num)
	while lst:
		step_num = lst[0]
		lst.pop(0)
		if step_num <= m and step_num >= n:
			print step_num,
		if num is 0 or step_num > m:
			continue
		ld = step_num % 10
		a = (step_num * 10) + (ld + 1)
		b = (step_num * 10) + (ld - 1)
		if ld is 0:
			lst.append(a)
		elif ld is 9:
			lst.append(b)
		else:
			lst.append(a)
			lst.append(b)
			
def stepping_num_dfs(n,m,num):
	if num <= m and num >= n:
		print num,
	if num is 0 or num > m:
		return
	ld = num % 10
	a = (num * 10) + (ld + 1)
	b = (num * 10) + (ld - 1)
	if ld is 0:
		stepping_num_dfs(n,m,a)
	elif ld is 9:
		stepping_num_dfs(n,m,b)
	else:
		stepping_num_dfs(n,m,a)
		stepping_num_dfs(n,m,b)
		

def  main():
	n,m = map(int,raw_input().split())
	for i in range(10):
		stepping_num_bfs(n, m, i)
	print "\n"	
	for i in range(10):
		stepping_num_dfs(n, m, i)

main()		