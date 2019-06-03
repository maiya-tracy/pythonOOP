class User:
	def __init__(self, username, email_address):
		self.name = username
		self.email = email_address
		self.account_balance = 0
	def make_deposit(self, amount):
		print(self.name + " deposited $" + str(amount))
		self.account_balance+=amount
		return self
	def make_withdrawal(self, amount):
		if amount > self.account_balance:
			print("Not enough money")
		else:
			self.account_balance-=amount
			print(self.name + " withdrew $" + str(amount))
		return self
	def display_user_balance(self):
		print("User: " + self.name + ", Balance: $" + str(self.account_balance))
		return self
	def transfer_money(self, other_user, amount):
		if amount > self.account_balance:
			print("Not enough money")
		else:
			self.account_balance-=amount
			other_user.account_balance+=amount
			print(self.name + " transferred $" + str(amount) + " to " + other_user.name)
		return self

def display_balances ():
	print("*********printing balances*********")
	User.display_user_balance(maiya)
	User.display_user_balance(joe)
	User.display_user_balance(billy)
	User.display_user_balance(bob)
	print("********finished printing**********")

maiya = User("Maiya T", "maiya.tracy93@gmail.com")
joe = User("Joe Schmoe", "joeschmoe@gmail.com")
billy = User("Billy Bob Joe Bob", "billy@bob.com")
bob = User("Bob theBuilder", "bob@building.com")

print(maiya.name)
maiya.display_user_balance().make_deposit(200).make_deposit(500).make_deposit(300).make_withdrawal(300)
display_balances()
bob.make_deposit(400).make_deposit(700).make_withdrawal(300).make_withdrawal(400)
display_balances()
User.transfer_money(bob,maiya,100)
display_balances()
billy.make_deposit(200).make_withdrawal(300)
display_balances()
joe.make_deposit(600).make_withdrawal(100).make_withdrawal(200).make_withdrawal(150.30)
display_balances()
User.transfer_money(billy,joe,320)
display_balances()


