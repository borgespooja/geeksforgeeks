def xor_c(a, b):
	return '0' if a == b else '1'

def flip(c):
	return '1' if c == '0' else '0'

def bin_to_gray(bina):
	gray = ''
	gray += bina[0]
	for i in range(1, len(bina)):
		gray += xor_c(bina[i-1], bina[i])
	return gray	
		
def gray_to_bin(gray):
	bina = ''
	bina += gray[0]
	for i in range(1, len(gray)):
		if gray[i] == '0':
			bina += bina[i-1]
		else:
			bina += flip(bina[i-1])
	return bina
	
print bin_to_gray('01001')	
print gray_to_bin('01101')