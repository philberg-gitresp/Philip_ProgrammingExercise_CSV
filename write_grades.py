# In this program, an instructor grades a class they teach,
# depending on how many the user inputs, after they take three exams.
# The program wants to store the information, including their first and
# last names as strings and the three exam grades as integers, to put in
# a file named 'grades.csv' for later use.

# You are in part one where the program write the .csv file for the other
# program could read on.

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

# The main program for everything to work.
def main():
    print("================================================")
    print("       Student Grade List Program (SGL)")
    print("================================================")
    write_grades()
    print("================================================")
    print("Thanks for inputting the information for the program.")
    print("To read the results, run read_grades.py in Python.")

main()