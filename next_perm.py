list_str = []
def next_perm(w, s):
	temp = w[:]
	if not temp:
		list_str.append(''.join(s))
		print ''.join(s)
		return
	for i in range(len(temp)):
		s.append(temp[i])
		if len(temp) >= 2:
			v = temp[:i] + temp[i+1:]
		else:
			v = []
		next_perm(v, s)
		s.pop()
	return

next_perm('abc', [])
print list_str	
		