# Assignment 1: Create a dictionary representing a student with keys like 'name', 'roll_number', 'grades' (a list of subjects and marks).
# Perform various operations like adding, removing, and modifying elements.

student_info = {
    "name": "Jimmy",
    "roll_number": "C193034",
    "semester": "1st",
    "grades": {
        "Math-1": 95,
        "EEE-1": 90,
        "PHY-1": 92,
        "Computer Programming 1": 84
    }
}

print("Student information:")
print(student_info)

student_info["grades"]["Advanced English"] = 85

print("Updated Student Information:")
print(student_info)

student_info["grades"]["Math-1"] = 90
print("After Modifying Student Information:")
print(student_info)

del student_info["grades"]["PHY-1"]
print("After Deleting Student Information:")
print(student_info)





# Assignment 2: Create a dictionary where keys are student names and values are lists of grades. Calculate the average grade for each student.

student_grades = {
    "Jimmy": [95, 80, 92],
    "Shamshed": [92, 88, 65],
    "Mukim": [70, 85, 80],
    "Samad": [98, 90, 92]
}

average_grades = {}

for student, grades in student_grades.items():
    total_grades = sum(grades)
    num_grades = len(grades)
    average_grade = total_grades / num_grades
    average_grades[student] = average_grade

print("Average grades for each student:")
for student, average_grade in average_grades.items():
    print(f"{student}: {average_grade:.2f}")


