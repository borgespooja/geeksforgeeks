# find leader elements in array: leader is the one which is > all elements to its right

def find_leader(a):
	lead_elem = a[len(a) - 1]
	print lead_elem,
	for i in range(len(a)-2, -1,-1):
		if lead_elem < a[i]:
			lead_elem = a[i]
			print lead_elem,	
		
find_leader([16, 17, 4, 3, 5, 2])		