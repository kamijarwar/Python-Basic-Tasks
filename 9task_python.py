


# ---------------- PYTHON BASIC TASKS ----------------

# Task 1: User se naam lo aur print karo
# Task 2: 2 numbers le kar sum, subtraction, multiplication, division
# Task 3: Age check (adult / not adult)
# Task 4: Even / Odd
# Task 5: Greatest of 3 numbers
# Task 6: Grade system (marks)
# Task 7: Positive / Negative / Zero
# Task 8: Simple Calculator
# Task 9: Salary Tax

# ---------------- MENU ----------------

print("----- Python Tasks Menu -----")
print("1. Welcome User")
print("2. Calculator Basic")
print("3. Age Check")
print("4. Even/Odd")
print("5. Greatest Number")
print("6. Grade System")
print("7. Number Type")
print("8. Calculator")
print("9. Salary Tax")

choice = int(input("Enter task number (1-9): "))

# ---------------- TASK LOGIC ----------------

if choice == 1:
    name = input("Enter your name: ")
    print("Welcome", name)

elif choice == 2:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print("Sum =", a+b)









# -------------------------------------------------------------------------------------
#1st Task: "User se naam lo aur print karo:"
name=input("ENter your name:")
print("Welcome",name)
#---------------------------------------------------------------------------------------

#2nd Task:User se 2 numbers lo aur:sum subtraction multiplication division print karo:
a=int(input("Enter 1st number:"))
b=int(input("Enter the 2nd number:"))
print("sum=",a+b)
print("subtraction=",a-b)
print("multiplication=",a*b)
print("division=",a/b)

#----------------------------------------------------------------------------------------------
#task:03: User se age lo aur check karo:agar age ≥ 18 → "You are an adult" warna → "You are not an adult"
age=int(input("Enter your age:"))
if age>=18:
   print("you are an adult:")
else:
   print("you are not an adult:")
#--------------------------------------------------------------------------------------------
#Task 04:write a program to check wehter a number is even or odd:
number=int(input("Enter any number:"))
if number %2==0:
   print("number is even:")
elif number %2!=0:
   print("Number is odd:")

#-----------------------------------------------------------------------------------------
#Task 05: write a programe: that takes input from user three numbers and print greter number from them:
a=int (input("Enter 1st number:"))
b=int (input("Enter 2nd number:"))
c=int (input("Enter 3rd number:"))
if a>=b and a>=c:
   print("Greater number is:",a) 
elif b>=a and b>=c:
   print("Greater number is:",b)
else:
   print("greter number is :",c)

#-----------------------------------------------------------------------------------------
#Task 06 write a program to ask user  enter a makrs 0-100 and assign them sutiable grade to them:
marks=int(input("ENter a marks of student:"))
if marks>=90 and marks<=100:
   print("A")
elif marks>=80 and marks<90:
   print("B")
elif marks>=70 and marks<80:
       print("C")
elif marks>=60 and marks<70:
           print("D")
else:
    print("fail:")

#-----------------------------------------------------------------------------------------------
#Task 07 write a program to check a number is negative postive or zero:
number=int(input("ENter any number:"))
if number>0:
   print("number positive:")
elif number<0:
   print("Nagative:")

elif number==0:
   print("number = zero:")
    
#-----------------------------------------------------------------------------------------
#Task 08:write a program of simple calculater:that takes two numbers and and operator form user and perform the operation:
a=int(input("ENter 1st number:"))
b=int(input("Enter 2nd number:"))
operator=input("enter any operator(+,-,*,/)")
if operator=="+":
   print("sum=",a+b)
elif operator=="-":
   print("subtractor=",a-b)
elif operator=="*":
   print("Multiplication=",a*b)
elif operator=="/":
   print("divison=",a/b)
else:
   print("Invalid operator:")


#----------------------------------------------------------------------------------------------------
#Task 09:write a program to User se salary lo:agar salary > 50,000 → tax = 10% warna → tax = 5% Final salary print karo after tax


salary=float(input("Enter your salary:"))
if salary>50000:
    tax=salary*0.10
    final_salary=salary-tax
    print("Final slary after tax is :",final_salary)
elif salary<=50000:
    tax=salary*0.05
    final_salary=salary-tax
    print("final salary after tax is :",final_salary)
