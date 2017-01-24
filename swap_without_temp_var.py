def swap_without_temp_var(a,b):
	a = a^b
	b = a^b
	a = a^b
	return (a,b)
a,b = 4,5	
a,b = swap_without_temp_var(a,b)
print a,b
a,b = 12,90
a,b = swap_without_temp_var(a,b)	
print a,b