class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

def cust_min(a, b):
	return a if a > -1 and a < b else b 
	
def bs(a,l,h,n):
	if l <= h:
		mid = (l+h)/2
		if a[mid] is n:
			mid = cust_min(bs(a,l,mid-1, n), mid)
			return mid
		elif n > a[mid]:
			return bs(a,mid+1,h,n)
		else:
			return bs(a,l,mid-1,n)
	else:
		return -1
		
def construct_tree_from_preorder(in_order, pre_order):
	if len(pre_order) is not len(in_order):
		raise Exception('Different input length, please check both inputs')
		return
	if not in_order or not pre_order:
		return None
	if len(in_order) is 1 and (in_order[0] is pre_order[0]):
		return Node(in_order[0])
	root = pre_order[0]
	root_index = bs(in_order, 0, len(in_order)-1, root)
	root = Node(root)
	root.left = construct_tree_from_preorder(in_order[:root_index], pre_order[1:root_index+1])
	root.right = construct_tree_from_preorder(in_order[root_index+1:], pre_order[root_index+1:])
	return root

def construct_tree_from_postorder(in_order, post_order):
	if len(in_order) is not len(post_order):
		raise Exception('Different input lengths, please check both inputs')
		return
	if not in_order or not post_order:
		return None
	if len(in_order) is 1 and (in_order[0] is post_order[0]):
		return Node(in_order[0])
	root = post_order[-1]
	root_index = bs(in_order, 0, len(in_order)-1, root)
	root = Node(root)
	root.left = construct_tree_from_postorder(in_order[:root_index], post_order[:root_index])
	root.right = construct_tree_from_postorder(in_order[root_index+1:], post_order[root_index:-1])
	return root
		
def print_inorder(node):
	if not node:
		return
	else:
		print_inorder(node.left)
		print node.val,
		print_inorder(node.right)

def print_preorder(node):
	if not node:
		return
	else:
		print node.val,
		print_preorder(node.left)
		print_preorder(node.right)
		
def print_postorder(node):
	if not node:
		return
	else:
		print_postorder(node.left)
		print_postorder(node.right)
		print node.val,
		
#root = construct_tree_from_preorder([1,3,4,6,7,8,10,13,14], [8,3,1,6,4,7,10,14,13])
#print_inorder(root)

print "Tree construction from Pre-order"
root = construct_tree_from_preorder([1,3,4,8,8,8,10,13,14], [8,3,1,4,8,8,10,14,13])
print_inorder(root)
print "\n"
print_preorder(root)
print "\n"
	
print "Tree construction from Post-order"
root = construct_tree_from_postorder([1,3,4,8,8,8,10,13,14], [1,4,3,13,14,10,8,8,8])
print_inorder(root)
print "\n"
print_postorder(root)

#negative cases, when accidently inputs of different size are given
#construct_tree_from_postorder([1,3,4,8,8,8,10,13,14], [1,4,3,13,14,10,8,8])
#construct_tree_from_preorder([1,3,4,8,8,8,10,13], [8,3,1,4,8,8,10,14,13])