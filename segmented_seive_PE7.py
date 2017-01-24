import math
import time
start_time = time.time()

def simplesieve(limit,prime):
	mark = [True] * (limit + 1)
	p = 2
	while (p**2) < limit:
		for i in range(2*p,limit,p):
			if mark[i] == True:
				mark[i] = False
		p += 1
	for i in range(2,limit):
		if mark[i] == True:
			prime.append(i)
	
def segmentedseive(n,prime):
	limit = int(math.sqrt(n)) + 1
	simplesieve(limit,prime)
	#print prime
	low = limit
	high =2 * limit
	while low < n:
		mark = [True] * (limit + 1)
		for i in range(len(prime)):
			lowlim = int(math.floor(low/prime[i]) * prime[i])
			if lowlim < low:
				lowlim += prime[i]
			for j in range(lowlim, high, prime[i]):
				#print j - low
				if mark[j-low] == True:
					mark[j-low] = False
		for i in range(low, high):
			if mark[i-low] == True:
				prime.append(i)
		low += limit
		high += limit
		if high >= n:
			high = n
	
def main():
	prime = []
	segmentedseive(460300,prime)
	print "Enter nth prime to be found:"
	#for i in range(6): 
		#n = int(raw_input())
		#print "th prime:".format(n),prime[n-1]
	print prime[10001]
main()	
print("--- %s seconds ---" % (time.time() - start_time))