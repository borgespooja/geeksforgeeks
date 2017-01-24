# find the pythagorean triplet in given array, (a^2 + b^2 = c^2) : a,b,c in given array
def find_pow(a, exp):
	if exp is 0:
		return 1
	if exp < 0:
		return 1 / find_pow(a, -exp)
	if not (exp % 2):
		return find_pow(a * a, exp >> 1)
	else:
		return a * pow(a, exp - 1)

# approach 1: naive approach, using 3 nsted loops
def pythagorean_triplet_1(a):
	for i in range(len(a)):
		for j in range(i+1, len(a)):
			for k in range(j+1 , len(a)):
				x = find_pow(a[i], 2)
				y = find_pow(a[j], 2)
				z = find_pow(a[k], 2)
				if (x + y is z) or (x + z is y) or (y + z is x): 
					return int(find_pow(x, 0.5)), int(find_pow(y, 0.5)), int(find_pow(z, 0.5))
	return "Does not exist"
	
# approach 2: using sorting
def q_sort(a):
	if not a:
		return []
	return q_sort([i for i in a[1:] if i < a[0]]) + [a[0]] + q_sort([i for i in a[1:] if  i >= a[0]])

	
def pythagorean_triplet(a):
	for i in range(len(a)): #O(n)
		a[i] = find_pow(a[i], 2)
	a = q_sort(a) #O(nlogn)
	for i in range(len(a)-1, 1, -1): #O(n-2) * O(n-3) = O(n^2)
		l = 0
		r = i - 1
		while l < r:
			if a[l] + a[r] is a[i]:
				return int(find_pow(a[l],0.5)), int(find_pow(a[r], 0.5)), int(find_pow(a[i], 0.5))
			elif (a[l] + a[r]) < a[i]:
				l += 1
			else:
				r -= 1
	return "Does not exist"
	
def main():
	print "pythagorean_triplet : ", pythagorean_triplet([3,1,4,6,5])
	print "pythagorean_triplet : ", pythagorean_triplet([2,6,8,0])
	print "pythagorean_triplet_1 : ", pythagorean_triplet_1([3, 1, 4, 6, 5])
	print "pythagorean_triplet_1 : ", pythagorean_triplet_1([2,6,8,0])
main()	