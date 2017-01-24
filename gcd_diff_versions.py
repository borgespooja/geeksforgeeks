def gcd_v1(a, b):
	if a is b:
		return a
	elif a > b:
		return gcd_v1(a-b,b)
	else:
		return gcd_v1(a,b-a)
	
def gcd_v2(a, b):
	if a is 0:
		return b
	else:
		return gcd_v2(b%a, a)
		
def gcd_v3(a, b):
	if (a is 0) or (a is b):
		return b
	if b is 0:
		return a
	if not (a & 1) and not (b & 1):
		return (gcd_v3(a>>1, b>>1) << 1)
	elif not (a & 1) and (b & 1):
		return gcd_v3(a>>1, b)
	elif (a & 1) and not (b & 1):
		return gcd_v3(a, b>>1)
	return gcd_v3(a-b, b) if (a > b) else gcd_v3(a, b-a)

print gcd_v1(6, 35)
print gcd_v2(6, 35)
print gcd_v3(6, 35) 	

print gcd_v1(1386, 3213)
print gcd_v2(1386, 3213)
print gcd_v3(1386, 3213)		