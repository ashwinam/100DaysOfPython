# List and Dictionary Comprehensions.
# traditional way
numbers = [1, 2, 3]
new_list = []
for num in numbers:
    new_list.append(num+1)

# same example using list comprehensions

new_numbers = [each+1 for each in numbers]
# next example

name = "Ashwin"
print([letter for letter in name])
# python sequences
'''
1. range
2. list
3. string
4. tuple
'''

# range(1, 5) double the numbers
double_numbers = [num * 2 for num in range(1, 5)]

# print(double_numbers)

# Conditional List Comprehensions
# [new_item for item in list if test]

names = ["Alex", 'Beth', "Caroline", "Dave", "Eleanor", "Freddie"]

name_list = [name for name in names if len(name) < 5]
# print(name_list)

# get the name that length is more than 5 and make it uppercase

new_name_list = [name.upper() for name in names if len(name) > 5]
print(new_name_list)