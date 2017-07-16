#
# Worksheet B
#
# This worksheet is also a Python program. Your task is to read the 
# task descriptions below and then write one or more Python statements to
# carry out the tasks. There's a Python "print" statement before each
# task that will display the expected output for that task; you can use
# this to ensure that your statements are correct.
#
# In this worksheet, some of the tasks will throw an error that causes
# the program to stop running, and skip the remaining tasks. Because of
# this, you'll have to complete the tasks in the given order!

print("\n------")
print("Task 1: Making a dictionary")
print("Expected output: helium")

# Task 1: A variable "element_names" is defined below, with a value of "None".
# Change the definition of "element_names" so that the variable contains a
# dictionary value, and the print statement below displays "helium" (instead
# of throwing a KeyError).

element_names = None
print(element_names['He'])

#------------------------------------------------------------------------

print("\n------")
print("Task 2: Adding a new key to a dictionary")
print("Expected output: lithium")

# Task 2: Modify the values of the variables "key" and "val" below so that
# the print statement displays 'lithium'.

key = "???"
val = "???"
element_names[key] = val
print(element_names['Li'])

#------------------------------------------------------------------------

print("\n------")
print("Task 3: Modifying an existing key")
print("Expected output: 19")

# Task 3: Modifying the values of the variables "key" and "value" below
# so that the print statement displays "19".

key = "???"
val = "???"
word_counts = {'cheese': 10, 'wine': 17, 'arachnids': 24}
word_counts[key] = val
print(word_counts['wine'])

#------------------------------------------------------------------------

print("\n------")
print("Task 4: Keys")
print("Expected output: 4")

# Task 4: Change the expression on the right-hand side of the assignment
# operator for the variable "student_names" below, so that the print
# statement displays "4". Use the `.keys()` method.

student_ages = {'Alfred': 17, 'Bryson': 18, 'Candace': 19, 'David': 20}
student_names = [] # <-- change this!
print(len(student_names))

#------------------------------------------------------------------------

print("\n------")
print("Task 5: Dictionary operations")
print("Expected output: Pluto is not a planet.")

# Task 5: Change the value of the variable "planet_name" below so that the
# expected output is printed.

planet_classifications = {'Mercury': 'terrestrial', 'Venus': 'terrestrial',
		'Earth': 'terrestrial', 'Mars': 'terrestrial', 'Jupiter': 'gas giant',
		'Saturn': 'gas giant', 'Uranus': 'ice giant', 'Neptune': 'ice giant'}
planet_name = 'Neptune'
if planet_name in planet_classifications:
	print(planet_name + " is a planet.")
else:
	print(planet_name + " is not a planet.")

#------------------------------------------------------------------------

print("\n------")
print("Task 6: Keys and loops")
print("Expected output: ")
print("  Earth")
print("  Mars")
print("  Mercury")
print("  Venus")

# Task 6: Modify the code below in the two following ways. First, change
# the right-hand side of the "planet_list" assignment. Then, add an "if"
# statement inside the "for" loop. Your goal is to produce the expected output
# above. Use the .keys() method and the sorted() function. You're
# checking to see which keys have the value "terrestrial".

planet_list = [] # <-- change this
for planet in planet_list:
	# add an if statement here, and tab over the line below
	print(planet)

#------------------------------------------------------------------------

print("\n------")
print("Task 7: Text analysis")
print("Expected output: 4")

# Task 7: Modify the code below in the two following ways. First, change
# the assignment of the variable "word_list" so that it contains a list
# of words in the string "words" (hint: use the ".split()" method). Second,
# replace the word "pass" in the "for" loop with a Python statement that
# adds a new key/value pair to the dictionary "word_dict", indicating the
# length of word. The result should be that the final print statement
# displays the output "4".

words = "Mother said there'd be days like these."
word_list = [] # <-- modify this
word_dict = {}
for word in word_list:
	pass # <-- replace this
print(word_dict['days'])


#------------------------------------------------------------------------

print("\n------")
print("Task 8: Text analysis, part 2")
print("Expected output:")
print("  Mother: 6")
print("  said: 4")
print("  there'd: 7")
print("  be: 2")
print("  days: 4")
print("  like: 4")
print("  these.: 6")

# Task 8: Using the "word_dict" variable you created in the previous task,
# write a loop that displays the expected output above. I've written a
# skeleton for you below. (You may need to use the "str()" function to
# append the two parts of the output string for each line together.)

for word in word_list:
	pass # <-- replace this!

#------------------------------------------------------------------------

print("\n------")
print("Task 9: Dictionaries with lists")
print("Expected output: ['foo', 'bar', 'baz']")

# Task 9: Modify the values of the variables "key" and "val" below so that
# the expected output is displayed.

key = "???"
val = "???"
widget_characteristics = {'scrumbulator': ['foo', 'bar']}
widget_characteristics[key].append(val)
print(widget_characteristics['scrumbulator'])

#------------------------------------------------------------------------

print("\n------")
print("Task 10: Lists of dictionaries")
print("Expected output: Mercutian, Venutian, Earthling, Martian")

# Task 10: Examine the data structure below: a list of dictionaries. Replace
# the word "pass" in the "for" loop below with a Python statement that takes
# the "demonym" key from each dictionary and appends it to the list "demonyms,"
# so that the expected output is produced.

planets = [
		{'name': 'Mercury', 'type': 'terrestrial', 'demonym': 'Mercutian'},
		{'name': 'Venus', 'type': 'terrestrial', 'demonym': 'Venutian'},
		{'name': 'Earth', 'type': 'terrestrial', 'demonym': 'Earthling'},
		{'name': 'Mars', 'type': 'terrestrial', 'demonym': 'Martian'}
]

demonyms = []
for planet in planets:
	pass # <-- replace this!
print(", ".join(demonyms))

#------------------------------------------------------------------------

print("\n------")
print("Task 11: Sets")
print("Expected output: apple, banana, cupcake")

# Task 11: The string below contains several duplications of the same strings.
# Insert an expression between the parentheses of the call to the set()
# function so that the desired output is produced. (Hint: You can initialize
# a new set by include an expression that evaluates to a string as the
# parameter to the set() function.)

items = "apple apple banana apple cupcake banana apple cupcake"
items_set = set() # <-- insert an expression between the parentheses
print(', '.join(sorted(items_set)))

#------------------------------------------------------------------------

print("\n------")
print("Task 12: List comprehensions (membership)")
print("Expected output: aardvark, anteater, alpaca")

# Task 12: The list comprehension below has no membership expression.
# Obviously, if left as-is, this list comprehension will evaluate to a copy
# of the original list. Add a membership expresison to the list comprehension
# so that the list comprehension evaluates to a new list that includes only
# those strings in the source list that start with the letter "a".

animals = ["aardvark", "camel", "anteater", "elephant", "alpaca", "jackal"]
animals_that_start_with_a = [x for x in animals] # <-- insert membership expr
print(', '.join(animals_that_start_with_a))

#------------------------------------------------------------------------

print("\n------")
print("Task 13: List comprehensions (predicate expression)")
print("Expected output: vark, amel, ater, hant, paca, ckal")

# Task 13: The list comprehension below has an expression "x" for its
# predicate expression. Modify the predicate expression so that the
# comprehension evaluates to a list containing the last four letters
# of each string in the source list.

animals = ["aardvark", "camel", "anteater", "elephant", "alpaca", "jackal"]
animal_parts = [x for x in animals] # <-- replace leftmost "x"
print(', '.join(animal_parts))

#------------------------------------------------------------------------

print("\n------")
print("Task 14: List comprehensions (putting it all together)")
print("Expected output: Camel, Elephant, Jackal")

# Task 14: Modify both the predicate expression and the membership expression
# of the list comprehension below so that the comprehension evaluates to a
# list containing only those strings that do NOT begin with the letter "a";
# the resulting strings should all have their first letters capitalized.
# (Hint: use the Python string object's .title() method.)

animals = ["aardvark", "camel", "anteater", "elephant", "alpaca", "jackal"]
animal_list = [x for x in animals] # <-- replace "x" and add membership expr
print(', '.join(animal_list))

#------------------------------------------------------------------------

print("\n------")
print("Task 15: List comprehensions with lists of dictionaries")
print("Expected output: Ceres, Pluto, Haumea, Makemake, Eris")

# Task 15: The "planets" variable below contains a list of dictionaries. Each
# dictionary in the list represents a planet, with a key/value pair for the
# planet's name and its type. Modify the predicate expression and membership
# expression of the list comprehension below so that the "dwarf_planet_names"
# variable contains a list of the names of each planet with a type of "dwarf."
# (Hint: the "planet name" expression in the list comprehension is just
# a placeholder! Replace it with an expression that evaluates to the value
# for the 'name' key in the dictionary.)

planets = [
		{'name': 'Mercury', 'type': 'terrestrial'},
		{'name': 'Venus', 'type': 'terrestrial'},
		{'name': 'Earth', 'type': 'terrestrial'},
		{'name': 'Mars', 'type': 'terrestrial'},
		{'name': 'Ceres', 'type': 'dwarf'},
		{'name': 'Jupiter', 'type': 'jovian'},
		{'name': 'Saturn', 'type': 'jovian'},
		{'name': 'Uranus', 'type': 'ice giant'},
		{'name': 'Neptune', 'type': 'ice giant'},
		{'name': 'Pluto', 'type': 'dwarf'},
		{'name': 'Haumea', 'type': 'dwarf'},
		{'name': 'Makemake', 'type': 'dwarf'},
		{'name': 'Eris', 'type': 'dwarf'},
]
dwarf_planet_names = ["planet name" for x in planets] # <-- make changes here!
print(", ".join(dwarf_planet_names))

