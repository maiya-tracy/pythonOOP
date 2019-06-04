class Zoo:
	def __init__(self, zoo_name):
		self.animals = []
		self.name = zoo_name
	def print_all_info(self):
		print("-"*30, self.name, "-"*30)
		for animal in self.animals:
			animal.display_info()
	def feed_animal(self):
		for animal in self.animals:
			animal.feed_animal()
	def time_passes(self):
		for animal in self.animals:
			animal.time_passes()
class Animal(Zoo):
	def __init__(self, name, age, weight=0):
		self.name = name
		self.age = age
		self.health = 100
		self.happiness = 100
		self.claws = 20
		self.weight = weight
	def time_passes(self):
		self.health-=10
		self.happiness-=10
	def feed_animal(self):
		self.health+=10
		self.happiness+=10
	def display_info(self):
		print(self.__dict__)
class Lion(Animal):
	def __init__(self, name, age, weight, length):
		super().__init__(name, age, weight)
		self.mane_length = length
	def roar(self):
		print("ROAR!!!")
class Tiger(Animal):
	def __init__(self, name, age, weight, number_of_stripes = 0):
		super().__init__(name, age, weight)
		self.number_of_stripes = number_of_stripes
class Bear(Animal):
	def __init__(self, name, age, weight, girth = 0):
		super().__init__(name, age, weight)
		self.girth = girth
		self.hibernating = False

zoo1 = Zoo("Maiya's Zoo")
tiger1 = Tiger("Bob", 10, 200, 30)
tiger2 = Tiger("Fred", 10, 300, 30)
lion1 = Lion("Nala", 2, 150, 100)
lion2 = Lion("Simba", 2, 150, 100)
bear1 = Bear("Bubba", 2, 400, 100)
bear2 = Bear("Billy", 2, 400)
zoo1.animals.append(tiger1)
zoo1.animals.append(lion1)
zoo1.animals.append(bear1)
zoo1.animals.append(tiger2)
zoo1.animals.append(lion1)
zoo1.animals.append(bear2)

zoo1.print_all_info()

lion1.roar()

bear1.hibernating = True

bear2.feed_animal()

zoo1.feed_animal()

zoo1.print_all_info()

zoo1.time_passes()

zoo1.print_all_info()
