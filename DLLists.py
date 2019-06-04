class DLNode:
	def __init__(self,value):
		self.value = value
		self.next = None
		self.previous = None
class DLList:
	def __init__(self):
		self.head = None
		self.tail = None
	def length_of_list(self):
		length = 0
		runner = self.head
		while (runner!= None):
			length+=1
			runner = runner.next
		return length
	def print_values(self):
		print(" ")
		print("printing values")
		runner = self.head
		while (runner!= None):
			print(runner.value)
			runner = runner.next
		print(" ")
		return self
	def first_item(self, val):
		if self.head == None:
			new_node = DLNode(val)
			self.head = new_node
	def add_to_front(self,val):
		new_node = DLNode(val)
		if (self.head == None):
			self.first_item(val)
			return self
		new_node.next = self.head
		self.head.previous = new_node
		self.head = new_node
		return self
	def add_to_back(self, val):
		if self.head == None:
			self.first_item(val)
			return self
		runner = self.head
		while runner.next != None:
			runner = runner.next
		new_node = DLNode(val)
		runner.next = new_node
		new_node.previous = runner
		return self
	def remove_from_front(self):
		if self.head == None:
			print("Nothing to remove")
		if self.head.next == None:
			self.head = None
			return self
		tmp = self.head.value
		self.head = self.head.next
		print("removing values")
		return tmp
	def remove_from_back(self):
		if self.head == None:
			print("Nothing to remove")
			return self
		if self.head.next == None:
			self.head = None
			return self
		runner = self.head
		while (runner.next != None):
			runner = runner.next
		runner.previous.next = None
		print("removing values")
	def remove_val(self, val):
		if self.head == None:
			print("Nothing to remove")
			return self
		if self.head.next == None:
			if self.head.value == x:
				self.head = None
			else:
				print("Not found")
			return self
		if self.head.value == val:
			self.head = self.head.next
			self.head.previous = None
			return self
		runner = self.head
		while runner.next != None:
			if runner.value == val:
				break;
			runner = runner.next
		if runner.next != None:
			runner.previous.next = runner.next
			runner.next.previous = runner.previous
		else:
			if runner.value == val:
				runner.previous.next = None
			else:
				print("Not found")
		print("removing values")
		return self
	def insert_at(self, val, n):
		if n == 0:
			self.add_to_front(val)
			return self
		if n == self.length_of_list() - 1:
			self.add_to_back(val)
			return self
		location = 0
		runner = self.head
		while (location != n-1):
			runner = runner.next
			location+=1
		if location == n-1:
			new_node = DLNode(val)
			new_node.previous = runner
			new_node.next = runner.next
			if runner.previous != None:
				runner.previous.next = new_node
			runner.next = new_node
			return self
		
my_list = DLList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!")

# my_list.print_values()
# print(my_list.length_of_list()) #3
print(my_list.remove_from_front())

# my_list.print_values()
my_list.add_to_front("Stuff1").add_to_front("stuff2").print_values()
my_list.remove_from_back()

# my_list.print_values() #Stuff2, Stuff1, are

my_list.add_to_front("Stuff3").add_to_front("Stuff4")

# my_list.print_values() #Stuff4, Stuff3, Stuff2, Stuff1, are

my_list.remove_val("are")
# print(my_list.length_of_list()) #4

# my_list.print_values() #Stuff4, Stuff3, Stuff2, Stuff1
my_list.remove_val("stuff2")
# my_list.print_values() #Stuff4, Stuff3, Stuff1
my_list.remove_val("Stuff4")
# my_list.print_values() #Stuff3, Stuff1
# print(my_list.length_of_list()) #2

my_list.insert_at(5,0)
# my_list.print_values() #5, Stuff3, Stuff1

my_list.insert_at(3,1)
my_list.print_values() #5, 3, Stuff3, Stuff1

my_list.insert_at(99,4)
my_list.print_values() #5, 3, Stuff3, Stuff1, 99