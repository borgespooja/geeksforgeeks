import random
def ran50():
	return (random.randint(0,1) & 1)
def rand75():
	return (ran50() | ran50())
def main():
	for i in range(50):
		print rand75(),
		
main()		