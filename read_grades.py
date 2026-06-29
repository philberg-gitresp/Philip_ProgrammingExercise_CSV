# In this program, an instructor grades a class they teach,
# depending on how many the user inputs, after they take three exams.
# The program wants to store the information, including their first and
# last names as strings and the three exam grades as integers, to put in
# a file named 'grades.csv' for later use.

# You are in part two where the program read the .csv file that was created
# by the writing program.

import csv

# Allows the program to read and display grades from the .csv file.
def read_grades():
    print("Student Grades\n")

    with open('grades.csv', 'r', newline="") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            print(f"{row[0]:<15}| {row[1]:<15}| {row[2]:<10}| {row[3]:<10}| {row[3]:<10}")

# The main program for everything to work.
def main():
    print("================================================")
    print("       Student Grade List Program (SGL)")
    print(" ")
    print("  - We will read the grades that was in the")
    print("    grades.csv file.")
    print("================================================")
    read_grades()
    print("================================================")
    print("Thanks for using the Student Grade List Program.")
    print("Have a nice day!")

main()