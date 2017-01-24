def isdivby9(n):
	if (n is 0 ) or (n is 9):
		return True
	elif n < 9:
		return False
	return isdivby9((n>>3) - (n&7))

print isdivby9(10)
print isdivby9(6)
print isdivby9(27)

	