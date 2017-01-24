def is_bin_palindrome(n):
	bin_num = bin(n)[2:]
	for i in range(len(bin_num)):
		if bin_num[i] != bin_num[len(bin_num)-i-1]:
			return False
	return True
	
def is_kth_bit_set(n, k):
	return bool(n & (1 << k))
		
def is_bin_pal(n):
	r = len(bin(n)[2:])-1
	l = 0
	while l < r:
		if is_kth_bit_set(n, l) != is_kth_bit_set(n, r):
			return False
		l += 1
		r -= 1 
	return True

print is_bin_pal(9)
print is_bin_pal(10)
print is_bin_pal(11)	
print is_bin_palindrome(9)
print is_bin_palindrome(10)
print is_bin_palindrome(11)
