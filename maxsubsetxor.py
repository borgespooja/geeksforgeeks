import sys
def maxsubsetxor(set):
	index = 0
	min_int = -(sys.maxint)-1
	for i in range(31,-1,-1):
		maxind = index
		maxelem = min_int
		for j in range(index,len(set)):
			if (set[j] & (1<<i)) and set[j] > maxelem:
				maxelem = set[j]
				maxind = j
		if maxelem is min_int:
			continue
		set[maxind],set[index] = set[index],set[maxind]
		maxind = index
		for j in range(0,len(set)):
			if (j is not maxind) and (set[j] & (1<<i)):
				set[j] = set[j] ^ set[maxind]
		index += 1
	res = 0	
	for i in range(len(set)):
		res ^= set[i]
	return res

print maxsubsetxor([2,4,5])
print maxsubsetxor([9,8,5])
print maxsubsetxor([8,1,2,12,7,6])
print maxsubsetxor([4,6])
	