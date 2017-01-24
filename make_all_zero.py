def make_all_zero(a):
	a[0] = a[a[0]]
	a[1] = a[0]
	return a
	
def make_all_zero_1(a):
	a[a[1]] = a[not a[1]]
	return a
	
def make_all_zero_2(a):
	a[a[1]] = a[a[0]]
	return a
	
def make_all_zero_3(a):
	a[not a[0]] = a[not a[1]]
	return a

print make_all_zero([0,1])
print make_all_zero_1([0,1])
print make_all_zero_2([0,1])
print make_all_zero_3([0,1])
	
	