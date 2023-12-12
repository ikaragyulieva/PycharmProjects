# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N.
# On the following N lines, you will be receiving a student's name and grade.
# For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point
# in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.

n = int(input())
students = {}
for _ in range(n):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student_name, grades in students.items():
    formated_grades = ' '.join([f"{grade:.2f}" for grade in grades])
    print(f"{student_name} -> {formated_grades} (avg: {sum(grades)/len(grades):.2f})")