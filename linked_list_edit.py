class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		

def prepare_llist():
	head = Node(9)
	node = head
	l_list_data = [1,3,5,9,4,10,1]
	for i in range(len(l_list_data)):
		node.next = Node(l_list_data[i])
		node = node.next
	return head

def print_l_list(node):
	while node:
		print node.data,
		node = node.next
	print "\n"

def lledit(head,M,N):
	node = head
	mi = M - 1
	ni = N - 1
	while node:
		while mi and node.next:
			node = node.next
			mi -= 1
			mi = M - 1
		if node.next:    
			node2 = node.next
		else:
			break
		while ni and node2.next:
			node2 = node2.next
			ni -= 1
		ni = N -1    
		if node2.next:
			node.next = node2.next
			node2.next = None
			node2 = None
		else:
			break
		print node.data,node.next.data
		if node.next:
			node = node.next
		else:
			break
 
l_list = prepare_llist()
lledit(l_list, 2, 1)
print_l_list(l_list) 
