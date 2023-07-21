import copy
import random
# Consider using the modules imported above.

class Hat:
	def __init__(self, **args):
		self.hat = args
		self.contents = []
		for key, val in args.items():
			for _ in range(val):
				self.contents.append(key)

	def draw(self, num_to_draw):
		removed_balls = []
		if num_to_draw >= len(self.contents):
			return self.contents
		for _ in range(num_to_draw):
			random_postion = random.randint(0, (len(self.contents) - 1))
			removed_balls.append(self.contents[random_postion])
			self.contents.remove(self.contents[random_postion])
		return removed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	M = 0
	flag = 0
	expected_flag = len(expected_balls)
	for _ in range(num_experiments):
		old_list = copy.copy(hat.contents)
		recieved_list = hat.draw(num_balls_drawn)
		hat.contents = old_list
		# hat.contents = hat.contents + recieved_list
		for key, val in expected_balls.items():
			num_key = recieved_list.count(key)
			if num_key < val:
				break
			else:
				flag += 1
		if flag == expected_flag:
			M += 1
		flag = 0
	return (M / num_experiments)
