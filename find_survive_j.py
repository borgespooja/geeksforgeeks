# after removing evry nth elemnt mentioned in j from a, find if a is not or a survives or not
# assumptions : here idx -1 assumed survival of n
def remove_every_xth(a, x, n):
	i = n
	idx = -1
	while i < len(a):
		if a[i-1] is n:
			idx = i-1
			del a[i-1]	
			return idx, a
		del a[i-1]	
		i += n
	return idx,a
# approach 1: by deleting evry a[j[i]th] elemnt in a	
def will_survive_j(a, j, n):
	for x in j:
		idx,a = remove_every_xth(a, x, n)
		if idx is not -1:
			return idx
 	return True
		
# approach 2: without modifying
def bs(a, l, h, n):
	if l <= h:
		mid = (l + h)/2
		if a[mid] is n:
			return mid
		elif n > a[mid]:
			return bs(a, mid + 1, h, n)
		else:
			return bs(a, l, mid-1, n)
	else:
		return -1
		
def	will_survive_j_alt(a, j, n):
	try:
		n_idx = bs(a, 0, len(a)-1, n)
		#n_idx = a.index(n)+1
	except ValueError:
		n_idx = 0
	except IndexError:
		n_idx = 0
	if n_idx is 0:
		return False
	for i in j:
		if not n%i:
			return False
		n_idx -= n_idx / i
	return True
	
print will_survive_j(range(1,1112), [2,3,4],142) 
print will_survive_j(range(1,1112), [2,3,4],1111)
print will_survive_j(range(1,9), [2,3,4],2)
print will_survive_j_alt(range(1,1112), [2,3,4],142) 
print will_survive_j_alt(range(1,1112), [2,3,4],1111)
print will_survive_j_alt(range(1,9), [2,3,4],2)
		