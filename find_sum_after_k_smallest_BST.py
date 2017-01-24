class Node:
	def __init__(self,val):
		self.left = None
		self.right = None
		self.val = val
		self.subTsum = 0
		self.subTsize = 0
		
def sub_tree_sum(node):
	if not node:
		return 0
	else:
		return node.val + sub_tree_sum(node.left) + sub_tree_sum(node.right)
		
def sub_tree_size(node):
	if not node:
		return 0
	else:
		return 1 + sub_tree_size(node.left) + sub_tree_size(node.right)
		
def get_remaining_sum(node, k):
	import pdb
	pdb.set_trace()
	current_sum = node.subTsum
	s = []
	s.append([node, False])
	while s:
		c = s[-1][0]
		if c.subTsize is k:
			return current_sum
		if c.subTsize < k:
			k -= c.subTsize
			current_sum -= c.subTsum
			s.pop()
		elif not s[-1][1]:
			s[-1][1] = True
			if c.left:
				s.append([c.left, False])
			else:
				s.pop()
				if c.right:
					s.append([c.right, False])
		else:
			s.pop()
	return -1

def create_BST():	
	n1 = Node(8)
	n2 = Node(3)
	n3 = Node(8)
	n4 = Node(1)
	n5 = Node(4)
	n6 = Node(8)
	n7 = Node(10)
	n8 = Node(14)
	n9 = Node(13)

	n1.left = n2
	n1.right = n3

	n2.left = n4
	n2.right = n5

	n3.right = n6

	n6.right = n7

	n7.right = n8

	n8.left = n9
	
	return n1
	
def populate_subtree_size_and_sum(node):
	if not node:
		return 0
	else:
		node.subTsize = 1 + sub_tree_size(node.left) + sub_tree_size(node.right)
		node.subTsum = node.val + sub_tree_sum(node.left) + sub_tree_sum(node.right)
		populate_subtree_size_and_sum(node.left)
		populate_subtree_size_and_sum(node.right)
		

def print_inorder(node):
	if not node:
		return
	else:
		print_inorder(node.left)
		print node.val, node.subTsize, node.subTsum
		print_inorder(node.right)
		
def print_pre_order(node):
	if not node:
		return
	else:
		print node.val, node.subTsize, node.subTsum
		print_pre_order(node.left)
		print_pre_order(node.right)		

def main():
	root = create_BST()
	populate_subtree_size_and_sum(root)
	#print_inorder(root)
	print_pre_order(root)
	print get_remaining_sum(root, 2)
	
main()	