"""
Module 11 Lab-11
Victor Rodriguez
5/2/25
Code writes a text file that allows for the user to enter grade info. The program then can reread the file 
and then calculate the total points earned, the number of students in the class, and the class average for the assignment
or class grade.
"""
def main():
    """
    even though the lab is written as two individual programs I decided to combine the two since the second part accesses the 
    first step. In the interest of learning how to write modular programming I decided to create a main function then have each 
    defined function in main be each part in the two steps.
    """
    #the first part out of the three problems assigned in the lab
    write_file()
    #the second part out of the three problems assigned in the lab
    read_file()

"""
This is the function that writes the text file.I added some minor validation attempting to use the new exception logic that I learned in
in the new chapter that we read. I also used the new try logic in order to use the new methods being learned in class. 
"""
def write_file():
    #this opens the file in writing mode
    with open('grades.txt','w') as file:
        while True:
            #lets the user know what the sentinel value for the function is
            grade_input = input("Enter the student's grade or a -1 to exit the program:")
            #established the sentinel value in the function
            if grade_input == '-1':
                print('All grades input. Exiting grade file.')
                break
            #writes the given input into the text file
            try:
                grade = float(grade_input)
                file.write(f"{grade}\n")
            
            #validation to prevent program from crashing if user enters a anything other 
            #a number it stops the program from crashing and just asks for new input
            except ValueError:
                print('Invalid Input. Enter a grade or -1 to exit.')

"""
This is the function that reads the text file and reinterprets it into python to display it. It also calculates the 
average using date found while translating.
"""
def read_file():
    #opens the file in read mode
    with open('grades.txt','r')as file:
        total = 0
        count = 0
        #reads the file line by line and groups the data together by line
        for line in file:
            #separates the lines by blank spaces
            print(line,end='')
            grade = float(line)
            total += grade
            count +=1
    print(f"The total is:{total}")
    print(f"The student count is:{count}")
    #this prevents a divide by zero condition if the user closes the program without entering data
    if count > 0:
        average = total/count
        print(f"The group average is:{average}")
    else:
        print('Since no grades were entered there is no average.') 
main()

"""
This program takes data including first and last name and three exam scores. Then it turns it into comma separated values.
"""
import csv
def csv_portion():
    #separates the csv by lines marked by blank spaces
    with open('grades.csv','w',newline='') as file:
        writer = csv.writer(file)

        while True:
            #tell the user the sentinel value
            first_name = input("Enter the student's first name or type finished to exit.\n")
            #establishes sentinel value in the loop
            if first_name == 'finished':
                print('All student info has been saved.')
                break
            last_name = input("Enter the student's last name:")

            try:
                #groups exams together under the same conditions
                exam_1 = int(input("Enter the student's Exam 1 grade:"))
                exam_2 = int(input("Enter the student's Exam 2 grade:"))
                exam_3 = int(input("Enter the student's Exam 3 grade:"))
                
                #creates the csv row with the data given
                writer.writerow([first_name,last_name,exam_1,exam_2,exam_3])
            #input validation to insure user inputs a integer
            except ValueError:
                print('Invalid input. Please enter a integer:')
csv_portion()
