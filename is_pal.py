def is_pal(s):
	if len(s) % 2 is 0:
		if s[:len(s)/2] == s[:len(s)/2 - 1:-1]:
			return True
		else:
			return False
	else:
		if s[:len(s)/2] == s[:len(s)/2:-1]:
			return True
		else:
			return False

print is_pal('aabaa')
print is_pal('aaaa')
print is_pal('abab')			
		
			