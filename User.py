class User:
	def __init__(self, username, email_address):
		self.name = username
		self.email = email_address
		self.account_balance = 0
	def make_deposit(self, amount):
		print(self.name + " deposited $" + str(amount))
		self.account_balance+=amount
	def make_withdrawal(self, amount):
		if amount > self.account_balance:
			print("Not enough money")
		else:
			self.account_balance-=amount
			print(self.name + " withdrew $" + str(amount))
	def display_user_balance(self):
		print("User: " + self.name + ", Balance: $" + str(self.account_balance))
	def transfer_money(self, other_user, amount):
		if amount > self.account_balance:
			print("Not enough money")
		else:
			self.account_balance-=amount
			other_user.account_balance+=amount
			print(self.name + " transferred $" + str(amount) + " to " + other_user.name)

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
User.display_user_balance(maiya)
User.make_deposit(maiya, 200)
User.make_deposit(maiya, 500)
User.make_deposit(maiya, 300)
User.make_withdrawal(maiya, 300)
display_balances()
User.make_deposit(bob, 400)
User.make_deposit(bob, 700)
User.make_withdrawal(bob, 300)
User.make_withdrawal(bob, 400)
display_balances()
User.transfer_money(bob,maiya,100)
display_balances()
User.make_deposit(billy, 200)
User.make_withdrawal(billy, 300)
display_balances()
User.make_deposit(joe, 600)
User.make_withdrawal(joe, 100)
User.make_withdrawal(joe, 200)
User.make_withdrawal(joe, 150.30)
display_balances()
User.transfer_money(billy,joe,320)
display_balances()


