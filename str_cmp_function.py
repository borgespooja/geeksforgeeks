def str_cmp_func(s1,s2):
	i = 0
	if (not s1) or (not s2):
		return -1
	while (i < len(s1)) and (i < len(s2)) and (s1[i] and s2[i]):
		if (s1[i] == s2[i]) or ((ord(s1[i]) ^ 32) is ord(s2[i])):
			i += 1
			continue
		else:
			break
	if i < len(s1) and i < len(s2) and (s1[i] == s2[i]):
		return 0
	elif i < len(s1) and i < len(s2) and ((ord(s1[i]) | 32) < (ord(s2[i]) | 32)):
		return -1
	return 1
print str_cmp_func('Geeks', 'apple')
print str_cmp_func('', 'ABCD')
print str_cmp_func('ABCD', 'z')
print str_cmp_func('ABCD', 'abcdEghe')
print str_cmp_func('GeeksForGeeks', 'gEEksFORGeEKs')#handle this, giving wrong ans
print str_cmp_func('GeeksForGeeks','geeksForGeeks')#handle this, giving wrong ans
	