#find subsets in a set 's' with given target sum 't'
def find_val(s, q, t):
	import pdb
	pdb.set_trace()
	if not s:
		return
	if sum(q) is t:
		print q
		return
	else:
		for i in range(len(s)):
			e = s.pop(0)
			q.append(e)
			find_val(s, q, t)
			del q[-1]
			s.insert(i, e)
		
def main():
	find_val([1,2,3,4,5], [], 5)

main()	
			
	