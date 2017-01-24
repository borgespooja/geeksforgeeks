def is_ok(b):
	dict = {}
	for i in b:
		if i in dict:
			dict[i] += 1
		else:
			dict[i] = 1
	for i in range(1,len(b)-1):
		if b[i] == b[i-1]:
			i += 1
			continue
		elif b[i] == b[i+1]:
			i += 2
			continue
		elif b[i] != b[i+1]:
			if '_' not in dict:
				print "NO"
				return
	print "YES"
	return
is_ok('AABA')
is_ok('AAAB')	
	