class Const_op_DS:
	def __init__(self):
		self.l = []
		self.max_l = []

	def push(self, val):
		self.l.append(val)
		if (not self.max_l) or (self.max_l and self.max_l[-1] <= val):
			self.max_l.append(val)
		else:
			self.max_l.append(self.max_l[-1])
	
	def pop(self):
		if self.l and self.max_l:
			popped_val = self.l[-1]
			del self.l[-1]
			del self.max_l[-1]
			return popped_val		
		else:
			print "no element to pop, DS is empty"
	
	def max(self):
		if self.max_l:
			return self.max_l[-1]
		else:
			print "empty DS, no max element"
			
s = Const_op_DS()
s.pop()
s.max()
s.push(1)
s.push(3)
s.push(1)

print s.max()

print s.pop()
			