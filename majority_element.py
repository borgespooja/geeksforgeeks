#find majorty elem, approach 1 : brute force 
def maj_elem_bf(a):
	for i in range(len(a)):
		count  = 0
		for j in range(len(a)):
			if a[i] is a[j]:
				count += 1
			if count > (len(a)/2):
				return a[i]
	return None

# approach 2: using dictionary
def	maj_elem_dict(a):
	dict = {u:0 for u in a}
	for i in a:
		dict[i] += 1
	for i in dict:
		if dict[i] > (len(a)/2):
			return i
	return None

# approach 3: moore's candidate elem algo
def cand_elem(a):
	maj_index,count = 0, 1
	for i in range(1, len(a)):
		if a[maj_index] is a[i]:
			count += 1
		else:
			count -= 1
		if count is 0:
			maj_index = i
			count = 1
	return a[maj_index]
	
def is_majority(a,cand):	
	count = 0
	for i in a:
		if i is cand:
			count += 1
	if count > (len(a)/2):
		return True
	else:
		return False
		
def maj_elem_moore(a):
	cand = cand_elem(a)
	if is_majority(a, cand):
		return cand
	else:
		return None

print maj_elem_bf([1, 3, 3, 1, 2])
print maj_elem_bf([1, 1, 1, 1, 2])
print maj_elem_dict([1, 3, 3, 1, 2])
print maj_elem_dict([1, 1, 1, 1, 2])
print maj_elem_moore([1, 3, 3, 1, 2])
print maj_elem_moore([1, 1, 1, 1, 2])		
		
			