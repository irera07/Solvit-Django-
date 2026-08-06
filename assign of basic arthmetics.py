#Exercise 1: basic arithmetic
a = 20
b = 5
print("Addition of a and b is: ", a + b)
print("Subtraction of a and b is: ", a - b)
print("Multiplication of a and b is: ", a * b)
print("Division of a and b is: ", a / b)
print("Floor Division of a and b is: ", a // b)
print("Modulus of a and b is: ", a % b)
print("Exponent of a and b is: ", a ** b)

print("\n")

#Exercise 2: Calculate Student Marks 
math = 80 
english = 75 
science = 90 

Total_marks = math + english + science
Average_marks = Total_marks / 3
print("Total marks of student is: ", Total_marks)
print("Average marks of student is: ", Average_marks)

print("\n")

#Exercise 3:Rectangle 
length = 12 
width = 8 
print("Area of rectangle is: ", length * width)
print("Perimeter of rectangle is: ", 2 * (length + width))

print("\n")

#Exercise 4: Even or Odd
number = 27 
if number % 2 == 0:
    print(number, "is an Even number")
else:
    print(number, "is an Odd number")
    
print("\n")

#Exercise 5: Update Variables
score = 50 
score += 20
print("Updated score is: ", score)

score -= 10
print("Updated score after subtraction is: ", score)

score *= 2
print("Updated score after multiplication is: ", score)

score /= 4
print("Updated score after division is: ", score)

print("\n")

#Exercise 6: Comparison Operators
a = 15 
b = 10 
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

print("\n")

#Exercise 7: Logical Operators 
age = 22 
has_id = True 

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)

print("\n")

#Exercise 8: User Input 
number_1=int(input("Enter first number: "))
number_2=int(input("Enter second number: "))
sum=number_1+number_2
difference=number_1-number_2
product=number_1*number_2
quotient=number_1/number_2
print("Sum of two numbers is: ", sum)
print("Difference of two numbers is: ", difference)
print("Product of two numbers is: ", product)
print("Quotient of two numbers is: ", quotient)

print("\n")

#Exercise 9: Mini Calculator
num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number: "))
print("Addition = ", num_1 + num_2)
print("Subtraction = ", num_1 - num_2)
print("Multiplication = ", num_1 * num_2)
print("Division = ", num_1 / num_2)
print("Remainder = ", num_1 % num_2)
print("Power = ", num_1 ** num_2)

print("\n")

#Exercise 10
n1=int(input("Enter Math marks: "))
n2=int(input("Enter English marks: "))
n3=int(input("Enter Science marks: "))

Total_marks=n1+n2+n3
Average_marks=Total_marks/3
print("Total: ", Total_marks)
print("Average: ", Average_marks)

if Average_marks>=50:
    print("Passed: ", Average_marks>=50)
else:
    print("Passed: ", Average_marks>=50)