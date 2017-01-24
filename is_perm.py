def is_perm(string,dict):
	s,e = 0,1
	flag = False
	while e <= len(string):
		if string[s:e] not in dict:
			e += 1
			flag = False
		elif string[s:e] in dict:
			s = e
			e += 1
			flag = True
			if e is len(string):
				return True
	return flag
	
print is_perm('badactorgoodacting',['good', 'actor', 'act','bad'])
print is_perm('badactorgoodacting',['good', 'actor', 'acting','bad'])