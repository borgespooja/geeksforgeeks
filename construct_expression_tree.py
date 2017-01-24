# construct expression tree
class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

def get_left_child(node):
	return node.left

def get_right_child(node):
	return node.right	

def insert_left(node, val):
		node.left = Node(val)

def insert_right(node, val):
		node.right = Node(val)	
		
def build_parse_tree(exp):
	exp_list = list(exp)
	pStack = []
	eTree = Node('')
	pStack.append(eTree)
	currentTree = eTree
	for i in exp_list:
		if i == '(':
			insert_left(currentTree, '')
			pStack.append(currentTree)
			currentTree = get_left_child(currentTree)
		elif i not in ['+', '-', '/', '*']:
			currentTree.val = int(i)
			parent = pStack.pop()
			currentTree = parent
		elif i in ['+', '-', '/', '*']:
			currentTree.val = i
			insert_right(currentTree, '')
			pStack.append(currentTree)
			currentTree = get_right_child(currentTree)
		elif i == ')':
			currentTree = pStack.pop()
		else:
			raise ValueError
	return eTree

def print_post_order(node):
	if not node:
		return
	else:	
		print_post_order(node.left)
		print_post_order(node.right)
		print node.val
		
pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
print_post_order(pt)	
			
	