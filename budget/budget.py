class Category:
	def __init__(self, name):
		self.name = name
		self.ledger = []

	def deposit(self, amount, description=""):
		deposit_dict = {"amount":amount, "description":description}
		self.ledger.append(deposit_dict)

	def check_funds(self, amount):
		if amount > self.ledger[0]["amount"]:
			return False
		return True
	
	def withdraw(self, amount, description=""):
		if self.check_funds(amount) == True:
			withdraw_dict = {"amount":-1*amount, "description":description}
			self.ledger.append(withdraw_dict)
			return True
		return False
	
	def get_balance(self):
		if not self.ledger:
			return 0
		return_val = self.ledger[0]["amount"]
		i = 1
		while i < len(self.ledger):
			val = self.ledger[i]["amount"]
			return_val += val
			i += 1
		return return_val

	def transfer(self, amount, other_category):
		if self.check_funds(amount) == True:
			self.withdraw(amount, f"Transfer to {other_category.name}")
			other_category.deposit(amount, f"Transfer from {self.name}")
			return True
		return False
	
	def __str__(self):
		return_string = ""
		def get_len_half(len_name):
			half_len_stars = round((30 - len_name) / 2)
			if not (2 * half_len_stars + len_name) == 30:
				half_len_stars += 1
			return half_len_stars
		
		half_len_stars = get_len_half(len(self.name))
		return_string += f"{half_len_stars * '*'}{self.name}{(half_len_stars) * '*'}\n"
		for entry in self.ledger:
			new_amount = f"{entry['amount']:.2f}"
			max_len = 29 - len(str(new_amount))
			if len(entry['description']) < max_len:
				entry['description'] += f"{(max_len - len(entry['description'])) * ' '}"
			limited_des = entry['description'][:max_len]
			return_string += f"{limited_des} {new_amount}\n"
		return_string += f"Total: {self.get_balance():.2f}"
		return return_string

def create_spend_chart(categories):
	spend = []
	longest_name = 0
	# string = "Percentage spent by category\n"
	s = "Percentage spent by category"		

	for category in categories:
		temp = 0
		for item in category.ledger:
			if item['amount'] < 0:
				temp += abs(item['amount'])
		spend.append(temp)
		if longest_name < len(category.name):
			longest_name = len(category.name)

	total = sum(spend)
	percentage = [i/total * 100 for i in spend]
	
	for i in range(100, -1, -10):
		s += "\n" + str(i).rjust(3) + "|"
		for j in percentage:
			if j > i:
				s += " o "
			else:
				s += "   "
		# Spaces
		s += " "
	s += "\n    ----------"
	
	cat_length = []
	for category in categories:
		cat_length.append(len(category.category))
	max_length = max(cat_length)
		
	for i in range(max_length):
		s += "\n    "
		for j in range(len(categories)):
			if i < cat_length[j]:
				s += " " + categories[j].category[i] + " "
			else:
				s += "   "
		# Spaces
		s += " "
	return s


	# start = 100
	# while start >= 0:
	# 	string += f"{' ' * (3 - len(str(start)))}{start}|"
	# 	for value in percentage:
	# 		if start <= value:
	# 			string += " o "
	# 		else:
	# 			string += "   "
	# 	string += "\n"
	# 	start -= 10
	# string += f"{4 * ' '}{'-' * ((len(categories) * 3) + 1)}"
	# for i in range(longest_name):
	# 	string += f"\n{4 * ' '}"
	# 	for catefory in categories:
	# 		if i >= len(catefory.name):
	# 			string += f"{3 * ' '}"
	# 		else:
	# 			string += f" {catefory.name[i]} "
	# 	string += ' '
	# return string