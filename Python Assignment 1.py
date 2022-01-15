# PYTHON ASSIGNMENT 1 


#Q1. Average of three numbers 

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
num3=float(input("Enter the third number: "))

print("The average of the given numbers is ",(num1+num2+num3)/3)

#Q2. Calculation of income tax 

income=float(input("Enter your total income:"))
members=int(input("Enter your none earning family members:"))

taxable_income=float(income-10000-members*3000)

income_tax=taxable_income/5

if income_tax<0:
    print("You don't have to pay income tax.")

else:    
   print("Income tax to be paid is ", income_tax)


#Q3. Storing data in form of list 

SID=int(input("Enter your SID-"))
name=input("Enter your name-")
gender=input("Enter your Gender-(M,F,U) -  ")
course=input("Enter the course name-")
cgpa=float(input("Enter the CGPA-"))

Student=[SID,name,gender,course,cgpa]

print(Student)


#Q4. Sorting marks of 5 students 
 
A1=float(input("Enter your marks:"))                #A1 is marks of student 1
A2=float(input("Enter your marks:"))                #A2 is marks of student 2
A3=float(input("Enter your marks:"))                #A3 is marks of student 3
A4=float(input("Enter your marks:"))                #A4 is marks of student 4
A5=float(input("Enter your marks:"))                #A5 is marks of student 5

Marks=[A1,A2,A3,A4,A5]
Marks.sort()
print(Marks)


#Q5.1 Removing certain element from a list 


colour=['Red','Green','White','Black','Pink','Yellow']
colour.remove('Black')
print(colour)

#Q5.2 Overwriting elements of a list 

colour[3:5]=['Purple']
print(colour)
