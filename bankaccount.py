class User:
	def __init__(self, username, email_address):
		self.name = username
		self.email = email_address
		self.account = [BankAccount(int_rate = 2, balance = 0)]
	def make_deposit(self, amount, whichOne):
		print(self.name + " deposited $" + str(amount))
		self.account[whichOne].account_balance+=amount
		return self
	def make_withdrawal(self, amount, whichOne):
		if amount > self.account[whichOne].account_balance:
			print("Not enough money")
		else:
			self.account[whichOne].account_balance-=amount
			print(self.name + " withdrew $" + str(amount))
		return self
	def display_user_balance(self, whichOne):
		print("User: " + self.name + ", Balance: $" + str(self.account[whichOne].account_balance))
		return self
class BankAccount:
	def __init__(self, int_rate, balance):
		self.interest_rate = int_rate
		self.account_balance = balance
	def deposit(self, amount):
		self.account_balance+=amount
		print("Balance: $" + str(self.account_balance))
		return self
	def withdraw(self, amount):
		if self.account_balance < amount:
			print("Insufficient funds: Charging a $5 fee")
			self.account_balance-=5
		else:
			self.account_balance-=amount
		print("Balance: $" + str(self.account_balance))
		return self
	def display_account_info(self):
		print("Balance: $" + str(self.account_balance))
		return self
	def yield_interest(self):
		if self.account_balance > 0:
			self.account_balance*=(1 + self.interest_rate/100)
			print(1 + self.interest_rate/100)
		return self

maiya = User("Maiya T", "m@yahoo.com")
maiya.account.append(BankAccount(5,120))
maiya.account[0].display_account_info()
maiya.display_user_balance(0)
maiya.account[1].display_account_info()
maiya.display_user_balance(1)


first_account = BankAccount(10, 100)
second_account = BankAccount(15, 5000)

first_account.deposit(200).deposit(100).deposit(250.25).withdraw(700).yield_interest().display_account_info()
second_account.deposit(129).deposit(342).withdraw(100).withdraw(200).withdraw(140).withdraw(380).yield_interest().display_account_info()


























