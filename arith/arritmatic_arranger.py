import pytest

def get_answer(numerator, operator, denominator):
	try:
		if operator == '+':
			answer = int(numerator) + int(denominator)
		else:
			answer = int(numerator) - int(denominator)
		return str(answer)
	except:
		print("Error: Numbers must only contain digits.")
		exit(1)
		

def arithmetic_arranger(problems, bool_ans=False):
	top = ""
	middle = ""
	dashes = ""
	answer = ""
	arranged_problems = ""

	len_problems = len(problems)
	if len_problems > 5:
		return ("Error: Too many problems.")

	for i in range(len_problems):
		numerator, operator, denominator = problems[i].split(' ')
		if not numerator.isdigit() or not denominator.isdigit():
			return "Error: Numbers must only contain digits."
		len_numerator = len(numerator)
		len_denominator = len(denominator)
		if len_numerator > 4 or len_denominator > 4:
			return ("Error: Numbers cannot be more than four digits.")
		if not operator in ['-', '+']:
			return ("Error: Operator must be '+' or '-'.")

		current_answer = ""
		current_answer += get_answer(numerator, operator, denominator)
		difference = abs(len_numerator - len_denominator)
		new_numerator = ""
		new_denominator = ""
		dash = ""
		larger = len_numerator

		if len_numerator >= len_denominator:
			new_numerator += f"  {numerator}"
			new_denominator += f"{' ' * (difference)} {denominator}"
			dash += f"{'-' * (len_numerator + 2)}"
			# answer += f"    {' ' * (abs(len_numerator - len(current_answer) + 2))}{current_answer}"
		else:
			new_numerator += f"{' ' * (difference + 1)} {numerator}"
			new_denominator += f" {denominator}"
			dash += f"{'-' * (len_denominator + 2)}"
			larger = len_denominator
			# answer += f"    {' ' * (abs(len_denominator - len(current_answer) + 2))}{current_answer}"
		if i == 0:
			top += f"{new_numerator}"
			middle += f"{operator}{new_denominator}"
			dashes += f"{dash}"
			answer += f"{' ' * (abs(larger - len(current_answer) + 2))}{current_answer}"
		else:
			top += f"    {new_numerator}"
			middle += f"    {operator}{new_denominator}"
			dashes += f"    {dash}"
			answer += f"    {' ' * (abs(larger - len(current_answer) + 2))}{current_answer}"
	if (bool_ans == True):
		arranged_problems += f"{top}\n{middle}\n{dashes}\n{answer}"
	else:
		arranged_problems += f"{top}\n{middle}\n{dashes}"
	return arranged_problems

# print(arithmetic_arranger(["2000 - 1", "11 + 5", "11 + 15", "11 + 5", "11 - 5"]))
print(arithmetic_arranger(['1 + 2', '1 - 9380'], True))