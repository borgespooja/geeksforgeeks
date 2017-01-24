import sys
class TrieNode:
	def __init__(self, value):
		self.value = value
		self.arr = [None]*2
	
def insert(root, pre_xor):
	temp = root
	for j in range(31, -1, -1):
		val = int(bool(pre_xor & (1<<j)))
		if temp.arr[val] is None:
			temp.arr[val] = TrieNode(0)
		temp = temp.arr[val]
	temp.value = pre_xor

def query(root, pre_xor):
	temp = root
	for i in range(31, -1, -1):
		val = int(bool(pre_xor & (1<<i)))
		if temp.arr[1 - val] is not None:
			temp = temp.arr[1 - val]
		elif temp.arr[val] is not None:
			temp = temp.arr[val]
	return pre_xor ^ temp.value

def maxSubArray(a):
	root = TrieNode(0)
	insert(root, 0)
	result = -sys.maxint-1
	pre_xor = 0
	for i in range(len(a)):
		pre_xor ^= a[i] 
		insert(root, pre_xor)
		result = max(result, query(root, pre_xor))
	print result
		
maxSubArray([8,1,2,12])	