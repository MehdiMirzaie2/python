# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main

rect = shape_calculator.Rectangle(3, 6)
sq = shape_calculator.Square(5)

rect.set_width(7)
rect.set_height(8)
sq.set_side(2)
actual = str(rect)
print(actual)
expected = "Rectangle(width=7, height=8)"
print(expected)
print("\n")
# assertEqual(actual, expected, 'Expected string representation of rectangle after setting new values to be "Rectangle(width=7, height=8)"')
actual = str(sq)
print(actual)
expected = "Square(side=2)"
print(expected)
print("\n")
# assertEqual(actual, expected, 'Expected string representation of square after setting new values to be "Square(side=2)"')
sq.set_width(4)
actual = str(sq)
print(actual)
expected = "Square(side=4)"
print(expected)
print("\n")
# assertEqual(actual, expected, 'Expected string representation of square after setting width to be "Square(side=4)"')

# rect = shape_calculator.Rectangle(5, 10)
# print(rect.get_area())
# print(rect)
# rect.set_width(3)
# print(rect)
# print(rect.get_perimeter())
# print(rect)

# sq = shape_calculator.Square(9)
# print(sq.get_area())
# sq.set_side(2)
# print(sq.get_diagonal())
# string = str(sq)
# print(string)
# sq.set_side(4)
# string = str(sq)
# print(string)


# Run unit tests automatically
# main(module='test_module', exit=False)