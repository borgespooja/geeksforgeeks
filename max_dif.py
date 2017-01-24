def max_dif_bf(a):
	n = len(a)
	max_dif = a[1] - a[0]
	for i in range(n):
		for j in range(i+1, n):
			if (a[j]-a[i]) > max_dif:
				max_dif = a[j]-a[i]
	return max_dif

def max_dif_min_elem(a):
	n = len(a)
	max_dif = a[1] - a[0]
	min_elem = a[0]
	for i in range(1, n):
		if (a[i] - min_elem)  > max_dif:
			max_dif = a[i] - min_elem
		elif min_elem > a[i]:
			min_elem = a[i]
	return max_dif

def max_dif_max_elem(a):
	n = len(a)
	max_elem = a[n-1]
	max_dif = -1
	for i in range(n-2, -1, -1):
		if a[i] > max_elem:
			max_elem = a[i]
		else:
			dif = max_elem - a[i]
			if dif > max_dif:
				max_dif = dif
	return max_dif

def max_dif_temp_dif_array(a):
	n = len(a)
	dif = [0] * (n-1)
	for i in range(n-1):
		dif[i] = a[i+1] - a[i]
	max_dif = dif[0]
	for i in range(1,n-1):
		if dif[i-1] > 0:
			dif[i] += dif[i-1]
		if max_dif < dif[i]:
			max_dif = dif[i]
	return max_dif

def max_dif_temp_var(a):
	n = len(a)
	dif = a[1] - a[0]
	cur_sum = dif
	max_sum = cur_sum
	for i in range(1, n-1):
		dif = a[i+1] - a[i]
		if cur_sum > 0:
			cur_sum += dif
		else:
			cur_sum = dif
		if cur_sum > max_sum:
			max_sum = cur_sum
	return max_sum

print max_dif_bf([1, 2, 90, 10, 110])
print max_dif_min_elem([1, 2, 90, 10, 110])
print max_dif_max_elem([1, 2, 90, 10, 110])
print max_dif_temp_dif_array([1, 2, 90, 10, 110])
print max_dif_temp_var([1, 2, 90, 10, 110])	
		