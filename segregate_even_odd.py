# segregate even on first(left) and then odd(right)
def  seg_even_odd(a):
	l,r = 0, len(a)-1
	while l < r:
		while not (a[l] & 1) and (l < r):
			l += 1
		while (a[r] & 1) and (l < r):
			r -= 1
		if l < r:
			a[l],a[r] = a[r],a[l]
			l += 1
			r -= 1
	return a

print seg_even_odd([12, 34, 45, 9, 8, 90, 3])