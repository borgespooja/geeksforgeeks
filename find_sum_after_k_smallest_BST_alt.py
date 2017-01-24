# find sum of bst after kth smallest node
class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val
		
# approach 1: using inorder traversal
def find_sum_after_kth_smallest_inorder_bst(node, k, sum_k):
	if not node:
		return k,sum_k
	else:
		k,sum_k = find_sum_after_kth_smallest_inorder_bst(node.left, k, sum_k)
		if not k:
			sum_k += node.val
		else:
			k -= 1
		k,sum_k = find_sum_after_kth_smallest_inorder_bst(node.right, k, sum_k)
		return k,sum_k

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

def main():
	sum_k = 0
	k = 3
	print find_sum_after_kth_smallest_inorder_bst(create_BST(), k, sum_k)[1]

main()	