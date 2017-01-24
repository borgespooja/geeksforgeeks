def make_equal_length(a,b):
	if len(a) is len(b):
		return (a,b)
	elif len(a) > len(b):
		b = ('0' *(len(a)-len(b))) + b
	elif len(b) > len(a):
		a = ('0' *(len(b)-len(a))) + a
	return a,b

def add_bit_strings(a,b):
	a,b = make_equal_length(a,b)
	carry = 0
	result = ''
	for i in range(len(a)-1,-1,-1):
		firstbit = ord(a[i]) - ord('0')
		secondbit = ord(b[i]) - ord('0')
		bit_sum = (firstbit ^ secondbit ^ carry)+ord('0')
		result = chr(bit_sum) + result
		carry = ((firstbit & secondbit) | (secondbit & carry) | (carry & firstbit))
	if carry:
		result = '1' + result
	return result

print add_bit_strings('1100011', '10')	