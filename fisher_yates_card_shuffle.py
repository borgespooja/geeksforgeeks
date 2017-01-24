import random
def card_shuffle(a):
	for i in range(len(a)-1,1,-1):
		rnum = random.randint(0,i)
		if rnum is not i:
			a[i],a[rnum] = a[rnum],a[i]
	return a

print card_shuffle([i+1 for i in range(52)])
	