# In this program, an instructor that teaches a class in which each
# student, for what how many the user inputs, takes three exams.
# The program wants to store the information, including their first and
# last names as strings and the three exam grades as integers, to put in
# a file named 'grades.csv' for later use.

import csv

# Creates the .csv file for grades while writing the information that it will
# give to and out of the user's input.
def write_grades():
    num_students = int(input("Enter number of students that are in the class: "))

    with open('grades.csv', 'w', newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        for i in range (num_students):
            print(f"\n- Student {i+1} -")

            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            exam_1 = input("Enter grade for exam 1: ")
            exam_2 = input("Enter grade for exam 2: ")
            exam_3 = input("Enter grade for exam 3: ")

            writer.writerow([first_name, last_name, exam_1, exam_2, exam_3])

    print("\ngrades.csv has been created successfully!\n")
    print("Thanks for inputting the information.")
    print("We will now show the results of what you typed.")
    print("================================================")

# Allows the program to read and display grades from the .csv file.
def read_grades():
    print("\nStudent Grades\n")

    with open('grades.csv', 'r', newline="") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            print(f"{row[0]:<15}| {row[1]:<15}| {row[2]:<10}| {row[3]:<10}| {row[3]:<10}")

# The Main Program
def main():
    write_grades()
    read_grades()

main()