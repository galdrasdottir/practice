def add(a, b):
	print("ADDING %d + %d" % (a, b))
	return a + b

def subtract(a, b):
	print("SUBTRACTING %d - %d" % (a, b))
	return a - b

def multiply(a, b):
	print("MULTIPLYING %d * %d" % (a, b))
	return a * b

def divide(a, b):
	print("DIVIDING %d / %d" % (a, b))
	return a / b

print("Let's do some math with just functions!")

height_in = int(input("How tall are you in inches?"))
weight_lb = int(input("What is your weight in lbs?"))

height_cm = multiply(height_in, 2.54)
weight_kg = divide(weight_lb, 2.205)


print("That's roughly %d cm and %d kg." % (height_cm, weight_kg))

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

division = divide(iq, 2)
multiplication = multiply(weight, division)
subtraction = subtract(height, multiplication)
addition = add(age, subtraction)

formula = 30 + 5 + ((78 - 4) - ((90 * 2) * (50 / 2)))

print(what, addition, formula)

new_formula = subtract(add(24, divide(34, 100)), 1023)
print(new_formula)