class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height
	
	def __str__(self):
		return f"Rectangle(width={str(self.width)}, height={str(self.height)})"

	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height

	def get_area(self):
		return (self.width * self.height)

	def get_perimeter(self):
		return (2 * self.width + 2 * self.height)
	
	def get_diagonal(self):
		return ((self.width ** 2 + self.height ** 2) ** .5)

	def get_picture(self):
		picture = ""
		if self.width > 50 or self.height > 50:
			return "Too big for picture."
		for _ in range(self.height):
			picture += f"{'*' * self.width}\n"
		return picture
	
	def get_amount_inside(self, other_width, other_height=None):
		if other_height == None:
			other_height = other_width.height
			other_width = other_width.width
		num_width = self.width / other_width
		num_height = self.height / other_height

		if num_height < 0 or num_width < 0:
			return 0
		return int(num_width * num_height)
	
# class Square(Rectangle):
# 	def __init__(self, side_lenght):
# 		self.side = side_lenght
# 		self.set_width(side_lenght)
# 		self.set_height(side_lenght)

# 	def set_side(self, new_side):
# 		self.side = new_side
# 		self.set_width(new_side)
# 		self.set_height(new_side)

class Square(Rectangle):
	def __init__(self, side_length):
		super().__init__(side_length, side_length)
		self.side = side_length

	def set_side(self, new_side):
		self.side = new_side
		self.set_width(new_side)
		self.set_height(new_side)

	def __str__(self):
		return f"Square(side={str(self.width)})"
