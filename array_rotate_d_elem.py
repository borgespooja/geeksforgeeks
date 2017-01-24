# approach 1: array rotation by d elements, using gcd
def gcd_num(a, b):
	if not b:
		return a
	return gcd_num(b, a%b)
	
def array_rotate_by_d_gcd(a,d,n):
	for i in range(gcd_num(d,n)):
		t = a[i]
		j = i
		while 1:
			k = j + d
			if k >= n:
				k -= n
			if k is i:
				break
			a[j] = a[k]
			j = k
		a[j] = t
	return a

# approach 2: array_rotate_by_d using temp array
def array_rotate_by_d_temp_arr(a, d, n):
	t = [a[i] for i in range(d)]
	a = [a[i+d] for i in range(n-d)] + a[n-d:]
	a[n-d:] = t[:]
	return a

# approach 3: array_rotate_by_d one at a time
def array_rotate_by_one(a,n):
	t = a[0]
	for i in range(n-1):
		a[i] = a[i+1]
	a[n-1] = t
	return a
def array_rotate_by_d(a, d, n):
	for i in range(d):
		a = array_rotate_by_one(a,n)

	return a
# approach 4: array_rotate_by_d using block swap
def swap(a,si,fi,d):
	for i in range(d):
		a[fi+i], a[si+i] = a[si+i],a[fi+i]
	return a
	
def array_rotate_by_d_block_swap_iter(a, d, n):
	if (not d) or (d is n):
		return
	i = d
	j = n - d
	while i is not j:
		if i < j:
			a = swap(a, d - i, d + j - i, i)
			j -= i
		else:
			a = swap(a, d - i, d, j)
			i -= j
	return swap(a, d-i, d, i)

def array_rotate_by_d_block_swap_rec(a, d, n):
	if (not d) or (d is n):
		return a
	if d is (n-d):
		a = swap(a, 0, n-d, d)
		return a
	if d < (n-d):
		a = swap(a, 0, n-d, d)
		array_rotate_by_d_block_swap_rec(a, d, n-d)
	else:
		a = swap(a, 0, d, n-d)
		array_rotate_by_d_block_swap_rec(a[:n-d], (2*d)-n, d)
	return a	
		
print array_rotate_by_d_gcd(range(1,13), 3, 12)
print array_rotate_by_d_temp_arr(range(1,13), 3, 12)	
print array_rotate_by_d(range(1,13), 3, 12)
print array_rotate_by_d_block_swap_iter(range(1,13), 3, 12)
print array_rotate_by_d_block_swap_rec(range(1,13), 3, 12)
		