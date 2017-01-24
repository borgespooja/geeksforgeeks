def abs_fun(n):
	if n > 0:
		return n
	mask = n >> 31
	return ((mask+n) ^ mask)

def abs_fun_1(n):
	if n > 0:
		return n
	mask = n >> 31
	return ((mask^n)-mask)

print abs_fun(-1)
print abs_fun_1(-1)
print abs_fun(-127)
print abs_fun_1(-127)
print abs_fun(2)
print abs_fun_1(2)	