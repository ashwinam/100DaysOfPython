import random
import pandas

# List and Dictionary Comprehensions.
# traditional way
numbers = [1, 2, 3]
new_list = []
for num in numbers:
    new_list.append(num + 1)

# same example using list comprehensions

new_numbers = [each + 1 for each in numbers]
# next example

name = "Ashwin"
# print([letter for letter in name])
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

# Dictionary Comprehension shortend for creating dictionaries
# 1. new_dict = {new_key:new_value for item in list }
# 2. new_dict = {new_key:new_value for (key, value) in dict.items() }

# Conditional Dictionary comprehension
# 3. new_dict = {new_key:new_value for (key, value) in dict.items() if test }


student_scores = {student: random.randint(40, 100) for student in names}


passed_students = {student: score for student, score in student_scores.items() if score > 60}

# iterate the pandas Data Frame
student_dict = {
    "students": ["Ashwin", "Pratik", "Tazin"],
    "scores": [56, 70, 90]
}

student_data_frame = pandas.DataFrame(student_dict)

# iterate data frame

for key, value in student_data_frame.items():
    pass

# loop through each rows using inbuilt data frame method

for index, row in student_data_frame.iterrows():
    if row.students == "Ashwin":
        print(row)