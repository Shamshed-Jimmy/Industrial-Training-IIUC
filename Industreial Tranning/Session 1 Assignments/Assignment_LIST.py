# Assignment 1: Create a 2D list representing a 3x3 matrix and perform operations like accessing, modifying, and iterating through it.

#3x3 matrix using a 2D list crated below

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in the matrix


print("Value at row 1, column 2:", matrix[1][2])

# Modifying an element in the matrix


matrix[0][0] = 10  # here, changing the value at row 0, column 0 to 10
print("Updated matrix:", matrix)



# Iterating through the matrix


print("Iterating through the matrix:")
for row in matrix:
    for element in row:
        print(element, end=" ")  # Print each element separated by a space
    print()  # Move to the next row
    


# Assignment 2: Create a tuple with mixed data types and demonstrate its potential use cases in data structures like dictionaries.


person_info = ("Jimmy", 26, "Chittagong", "Power Bi")

# Creating  a dictionary to store the person's details


person_dict = {
    "name": person_info[0],
    "age": person_info[1],
    "location": person_info[2],
    "skills": person_info[3]
}

# Displaying the person's details


print("Name:", person_dict["name"])
print("Age:", person_dict["age"])
print("Location:", person_dict["location"])
print("Skills:", person_dict["skills"])




# Assignment 3: Create a list of tuples, where each tuple contains a student's name and their grade. Sort this list by grades.

# List of student names and grades
student_grades = [
    ("Jimmy", 85),
    ("Ismile", 72),
    ("Atif", 90),
    ("Ikramul", 78),
    ("Minhaz", 95)
]

# Sorting the list by grades (from lowest to highest)

sorted_grades = sorted(student_grades, key=lambda x: x[1])

# Displaying the sorted list of grades


print("Sorted Grades:")
for name, grade in sorted_grades:
    print(name + ":", grade)

