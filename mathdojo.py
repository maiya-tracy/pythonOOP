class MathDojo:
	def __init__(self):
		self.result = 0
	def add(self, num, *nums):
		self.result += num
		for number in nums:
			self.result += number
		return self
	def subtract(self, num, *nums):
		self.result -= num
		for number in nums:
			self.result -= number
		return self
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5

md1 = MathDojo()

y = md1.add(2,3).subtract(4,5).add(9).subtract(2,3,7).result
print(y)
