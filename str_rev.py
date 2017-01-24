# string reversal
#approach 1: recursive
def rev_rec(s,st):
	if not s:
		return ''.join(st)
	else:	
		st.append(s.pop())
	return rev_rec(s, st)

# approach 2: iterative
def rev_iter1(s):
	res = []
	for i in range(len(s)-1, -1, -1):
		res.append(s[i])
	return ''.join(res)

# approach 3: iterative
def rev_iter2(s1):
	s = list(s1)
	n = len(s)
	for i in range(len(s)/2):
		s[i], s[n-i-1] = s[n-i-1],s[i]
	return ''.join(s)

print rev_rec(list('abcde'),[])
print rev_iter1('abcde')
print rev_iter2('abcde')	