class Node:
	def __init__(self, value):
		self.value = value
		self.adj = []

def bfs(src):
	q = []
	q.append(src)
	visited = [src]
	while q:
		node = q.pop(0)
		print "value of node :",node.value
		print "address of node :",node
		for v in node.adj:
			if v not in visited:
				visited.append(v)
				q.append(v)
				
				
			
def cloneGraph(src):
	g_dict = {}
	q = []
	node = Node(src.value)
	#node.adj = src.adj
	g_dict[src] = node
	q.append(src)
	while q:
		n = q.pop(0)
		for v in n.adj:
			if v not in g_dict:
				new_node = Node(v.value)
				g_dict[v] = new_node
				q.append(v)
			g_dict[n].adj.append(g_dict[v])
	return g_dict[src]

#1 -- 2
#|    |
#|    |
#4 -- 3 
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.adj.append(n2)
n1.adj.append(n4)
n2.adj.append(n1)
n2.adj.append(n3)
n3.adj.append(n2)
n3.adj.append(n4)
n4.adj.append(n1)
n4.adj.append(n3)

print "graph before cloning"
bfs(n1)
new_src = cloneGraph(n1)
print "graph after cloning"
bfs(new_src)		