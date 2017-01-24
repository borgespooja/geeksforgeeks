def xor(a,b):
	result = []
	for i in range(1,len(b)):
		if a[i] == b[i]:
			result.append('0')
		else:
			result.append('1')
	return ''.join(result)

def modulo2(divident,divisor):
	pick = len(divisor)
	tmp = divident[0:pick]
	while pick < len(divident):
		if tmp[0] == '1':
			tmp = xor(divisor, tmp) + divident[pick]
		else:
			tmp = xor('0'*pick, tmp) + divident[pick]
		pick += 1
	if tmp[0] == '1':
		tmp = xor(divisor, tmp)
	else:
		tmp = xor('0'*pick, tmp)
	return tmp

def encodedata(data,key):
	appended_data = data+'0'*(len(key)-1)
	remainder = modulo2(appended_data, key)
	#print 'Appended_data:',appended_data
	print 'Remainder:', remainder
	print 'Code Word:', data+remainder

encodedata("100100", "1101")
