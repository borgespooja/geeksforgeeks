def are_opp_sign(x,y):
	return ((x ^ y) < 0)

def are_opp_sign1(x,y):
	return (y >= 0) if (x < 0) else (y < 0)

print are_opp_sign(-1, 100)
print are_opp_sign1(-1, 100)

print are_opp_sign(1, 1)
print are_opp_sign1(1, 1)	