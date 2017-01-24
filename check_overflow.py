def check_overflow(a, b):
	num_sum = a+b
	if (a > 0) and (b> 0) and (num_sum < 0):
		return -1
	if (a < 0) and (b < 0) and (num_sum > 0):
			return -1
	else:
			return 0
			
def check_overflow_1(a, b):
	import sys
	if a > (sys.maxint - b):
		return -1
	else:
		result = a+b
		return 0,result
#comented below call as it is giving wrong ans in python
#print check_overflow(2147483640, 10)
print check_overflow_1(2147483640, 10)		