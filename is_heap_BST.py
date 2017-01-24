# check if given BST is heap or not

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.key = key
		
def create_tree():
	root = Node(10)
	root.left = Node(9)
	root.right = Node(8)
	root.left.left = Node(7)
	root.left.right = Node(6)
	root.right.left = Node(5)
	root.right.right = Node(4)
	root.left.left.left = Node(3)
	root.left.left.right = Node(2)
	root.left.right.left = Node(1)
	return root
	
def count_nodes(root):
	if not root:
		return 0
	return 1 + count_nodes(root.left) + count_nodes(root.right)

def is_heap_util(root):
	if not root.left and not root.right:
		return True
	if not root.right:
		return (root.key >= root.left.key)
	else:	
		if ((root.key >= root.left.key) and (root.key >= root.right.key)):
			return is_heap_util(root.left) and is_heap_util(root.right)
		else:
			return False

def is_complete_BST(root, idx, num_nodes):
	if not root:
		return True
	if idx >= num_nodes:
		return False
	return is_complete_BST(root.left, (2 * idx) + 1, num_nodes) and is_complete_BST(root.right, (2 * idx) + 2, num_nodes)
	
			
def is_heap(root):
	if not root:
		return True
	num_nodes = count_nodes(root)
	idx = 0	
	return (is_complete_BST(root, idx, num_nodes) and is_heap_util(root))

def main():
	root = create_tree()
	if is_heap(root):
		print "Yes , given BST is max_heap"
	else:
		print "No, given BST is not max_heap"

main()		