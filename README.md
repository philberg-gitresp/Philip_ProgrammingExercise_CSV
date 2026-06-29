# Philip_ProgrammingExercise_CSV

There are two programs involved in this project, write_grades.py and read_grades.py.
In this program, an instructor grades a class they teach, depending on how many the user inputs, after they take three exams. The program wants to store the information, including their first and last names as strings and the three exam grades as integers, to put in a file named 'grades.csv' for later use.

Both functions in both programs will be put into one in this document.

## Function: write_grades
Creates the .csv file for grades while writing the information that it will give to and out of the user's input.

Parameters:
None

Variables:
num_students (Stores the number of students in the class that the user enters.)
csvfile (Creates the .csv file for the program.)
writer (Writes the information the user inputs in the .csv file that was created by the program.)
i (Loops the process for each student that is in the class entered by the user.)
first_name (Stores the first name of the student in the .csv file.)
last_name (Stores the last name of the student in the .csv file.)
exam_1 (Stores the grade of the first exam in the .csv file.)
exam_2 (Stores the grade of the second exam in the .csv file.)
exam_3 (Stores the grade of the third exam in the .csv file.)

Logic:
1. The program will ask the user how many students are in the classroom.
2. Once the number of students was answered, the program will start asking the user their information and what grades they had gotten.
3. The process will repeat itself until there are no more students left to give information on.

Returns:
None


## Function: read_grades
Allows the program to read and display grades from the .csv file.

Parameters:
None

Variables:
csvfile (If there is a .csv that was either put in or created in the first program, it will use it for the function to work.)
reader (Once the .csv file has been found, it will use the information from the file to display its results.)
row (Stores each road that is read from the .csv file.) 

Logic:
1. The program will find the .csv file from the other program to read the information.
2. Once the .csv file was found, the program will display the results from all the information that the user had inputted from the last program.

Returns:
None


## Function: main
The main program for everything to work.

Parameters:
None on either program.

Variables:
None on either program.

1st Logic (write_grades.py):
1. The program will ask the user to input the information for the .csv file.
2. Once everything is put in, the program will create the grades.csv file
3. The program will then ask the user to head for the other program (read_grades.py) to display the results.

2nd Logic (read_grades.py):
1. The program will locate the grades.csv file that the user has created for the program itself.
2. Once the .csv file is found, it will display the results on what the user had wrote from the last program to see if everything they wrote works.

Returns:
None on either program.
