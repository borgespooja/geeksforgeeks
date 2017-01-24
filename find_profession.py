#Tree Structure 
#			E
#		 E  		D
#      E	D      D    E	
#	  E D  D E    D  E E D

def countsetbit(n):
	count = 0
	while n:
		n &= (n-1)
		count += 1
	return count

def findprofession1(level,pos):
	print 'Doctor' if (countsetbit(pos-1) & 1) else 'Engineer'
	
def findprofession2(level,pos):
	if level is 1:
		return 'e'
	if findprofession2(level - 1, (pos + 1)/2) is 'd':
		return 'd' if (pos & 1) else 'e'
	return 'e' if (pos & 1) else 'd'

def main():
	l,p = 4,2
	findprofession1(l,p)
	print 'Engineer' if (findprofession2(l,p) == 'e') else 'Doctor'	

main()	