#
# Worksheet A
#
# This worksheet is also a Python program. Your task is to read the 
# task descriptions below and then write one or more Python statements to
# carry out the tasks. There's a Python "print" statement before each
# task that will display the expected output for that task; you can use
# this to ensure that your statements are correct.
#

print("------")
print("Task 1: Arithmetic expressions")
print("Expected output: 7")

# Task 1: Add parentheses to the Python statement below so that it prints
# out the number 7.

print(10 + 4 / 2)

#------------------------------------------------------------------------

print("\n------")
print("Task 2: Expressions of inequality")
print("Expected output: True")

# Task 2: Change the operator in the statement below so that it displays
# "True" instead of "False."

print(14 > 15)

#------------------------------------------------------------------------

print("\n------")
print("Task 3: Variable assignment")
print("Expected output: 32")

# Task 3: Change the variable assignment below so that the print statement
# displays "32." (Don't change the print statement!)

my_number = 17
print(my_number)

#------------------------------------------------------------------------

print("\n------")
print("Task 4: Types")
print("Expected output: <type 'str'>")

# Task 4: Three variables are assigned below, all with different types.
# Replace the word "None" inside the parentheses of type() in the print
# statement below so that it prints "<type 'str'>".

x = 14
y = 17.4
z = "mother said there'd be days like these"
print(type(None))

#------------------------------------------------------------------------

print("\n------")
print("Task 5: String literals")
print("Expected output: We aren't friends now.")

# Task 5: Modify the print statement below so that it displays the string
# "We aren't friends now." (i.e., change "are" to "aren't".) Use a
# single quoted string---don't change it to double quotes.

print('We are friends now.')

#------------------------------------------------------------------------

print("\n------")
print("Task 6: Questions about strings")
print("Expected output: 51")

# Task 6: Inside the call to "print" below, write an expression that evaluates
# to the sum of the lengths of the two string variables defined below
# (first_line and second_line). Use the len() function.

first_line = "It was the best of times."
second_line = "It was the worst of times."
print() # your code here!

#------------------------------------------------------------------------

print("\n------")
print("Task 7: Questions about strings, part 2")
print("Expected output: 37")

# Task 7: Inside the call to "print" below, write an expression that evaluates
# to the position of the word "window" in the string defined in the variable
# called "romeo." Use the .find() method.

romeo = "But, soft! what light through yonder window breaks?"
print() # your code here!

#------------------------------------------------------------------------

print("\n------")
print("Task 8: String transformations")
print("Expected output: and the horse you rode in on")

# Task 8: Modify the print statement below so that it prints out the contents
# of the variable "benediction", but with all white space removed from
# the beginning and end of the string. Use the .strip() method.

benediction = "     and the horse you rode in on    \n"
print(benediction)

#------------------------------------------------------------------------

print("\n------")
print("Task 9: String transformations, part 2")
print("Expected output: AND THE HORSE YOU RODE IN ON")

# Task 9: Using the previously defined "benediction" variable, write an
# expression inside the "print" function below that evaluates to the content of
# the string, with all whitespace removed, and with all letters converted to
# uppercase. Use the .upper() method.

print() # your code here!

#------------------------------------------------------------------------

print("\n------")
print("Task 10: String indexing")
print("Expected output: p")

# Task 10: Modify the value assigned to variable "offset" below so that
# the following "print" statement displays the letter "p".

offset = 0
print("apple"[offset])

#------------------------------------------------------------------------

print("\n------")
print("Task 11: String slices")
print("Expected output: yonder")

# Task 11: Modify the values assigned to variables "start" and "end"
# below so that the following "print" statement displays the word "yonder".

start = 0
end = 10
romeo = "But, soft! what light through yonder window breaks?"
print(romeo[start:end])

#------------------------------------------------------------------------

print("\n------")
print("Task 12: Integers and strings")
print("Expected output: 100")

# Task 12: Modify the statement below so that it displays the number 100.
# Do this using the int() function (hint: you need to use it twice).

print("19" + "81")

print("\n------")
print("Task 13: List indexes")
print("Expected output: alpha")

# Task 13: A variable "greek" is defined below. The value of this variable
# is of type list. Change the expression below the variable definition so
# that it prints "alpha" (instead of "beta").

greek = ["alpha", "beta", "gamma", "delta", "epsilon"]
print(greek[1])

#------------------------------------------------------------------------

print("\n------")
print("Task 14: List slices")
print("Expected output: ['beta', 'gamma', 'delta']")

# Task 14: Change the values of the variables "start" and "finish" below so that
# the print statement displays the second through fourth items in the list
# "greek" (defined above).

start = 0
finish = 6
print(greek[start:finish])

#------------------------------------------------------------------------

print("\n------")
print("Task 15: List slices, part 2")
print("Expected output: ['delta', 'epsilon']")

# Task 15: Change the value of the variable "foo" below so that the print
# statement displays the last two members of the list "greek" (defined above).
# Use a negative number for "foo".

foo = 0
print(greek[foo:])

#------------------------------------------------------------------------

print("\n------")
print("Task 16: List operations")
print("Expected output: True")

# Task 16: Change the value of the variable "letter_to_look_for' below so
# that the print statement displays "True."

letter_to_look_for = "aleph"
print(letter_to_look_for in greek)

#------------------------------------------------------------------------

print("\n------")
print("Task 17: List operations, part 2")
print("Expected output: ['alpha', 'beta', 'delta', 'epsilon', 'gamma']")

# Task 17: Change the expression below so that the print statement displays
# the list "greek" (defined above) in alphabetical order. (Use the "sorted"
# function.

print(greek)

#------------------------------------------------------------------------

print("\n------")
print("Task 18: Modifying lists")
print("Expected output: ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta']")

# Task 18: Write a Python statement that adds a new item, "zeta", to the
# list "greek" (defined above). The print statement should display the updated
# list.

# write your statement here
print(greek)

#------------------------------------------------------------------------

print("\n------")
print("Task 19: Loops")
print("Expected output:")
print("  alpha")
print("  beta")
print("  gamma")
print("  delta")
print("  epsilon")
print("  zeta")

# Task 19: Write a "for" loop below that prints out each item in the list
# "greek" (defined above). (The list should contain the item that you
# added to the list in task 18.)




#------------------------------------------------------------------------

print("\n------")
print("Task 20: Loops, part 2")
print("Expected output:")
print("  Alpha")
print("  Beta")
print("  Gamma")
print("  Delta")
print("  Epsilon")
print("  Zeta")

# Task 20: Write a "for" loop below that prints out each item in the list
# "greek" (defined above), but with the first letter of each item capitalized.
# (The list should contain the item that you added to the list in task 18.)




#------------------------------------------------------------------------

print("\n------")
print("Task 21: Split and join")
print("Expected output:")
print("  81")
print("  9-18-81")

# Task 21: Modify the variable "separator" below so that the first print
# statement displays "81". Modify the variable "glue" so that the second print
# statement displays "9-18-81".

separator = "?"
glue = "?"
parts = "9/18/81".split(separator)
print(parts[-1])
print(glue.join(parts))

#------------------------------------------------------------------------

print("\n------")
print("Task 22: All together now")
print("Expected output: alpha, beta, gamma, delta, epsilon, zeta, eta, theta")

# Task 22: Make three changes on the Python code below, as follows: (1) replace
# [] with an expression that evaluates to a list with two items, "eta" and
# "theta" (using the .split() method). (2) Replace the word "pass" with a
# Python statement, so that the "for" loop has the effect of adding two new
# items to the list "greek". (Use the .append() method.) (3) Change the value
# of the variable "glue" so that the desired output is displayed.

new_letters = "eta theta"
new_letters_list = [] # <-- replace this

for letter_name in new_letters_list:
	pass # <-- and replace this

glue = "?" # <-- and replace this

print(glue.join(greek))
