def subtract_iter(x, y):
	while y:
		bor = ((~x) & 0xFF) & y
		x ^= y
		y = bor << 1
	return x

def subtract_rec(x, y):
	if not y:
		return x
	return subtract_rec(x^y, (((~x) & 0xFF) & y) << 1)

print subtract_iter(9,4)
print subtract_rec(9,4)	