# find longest path from root to leaf in binary tree, given pointer to root
class Node:
	def __init__(self,val):
		self.left = None
		self.right = None
		self.val = val
		
def check_ht(node):
		if not node:
			return 0
		return 1 + max(check_ht(node.left), check_ht(node.right))

def long_path(node, p):
		if not node:
			return
		else:
			p.append(node.val)
			if check_ht(node.left) > check_ht(node.right):
				return long_path(node.left, p)
			else:
				return long_path(node.right, p)

def main():
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)
	n5 = Node(5)

	n1.left = n2
	n1.right = n3

	n2.left = n4

	n4.left = n5

	q = []
	long_path(n1, q)
	print q  
	
main()	
			