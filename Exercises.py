#Question 1: Student Profile (String)
Full_name="irera josue"
Email= "irerajosue07@gmail.com"
Phone_number= 123456
Country= "Rwanda"
print("Full name is: ", Full_name)
print("Email is: ", Email)
print("Phone number is: ", Phone_number)
print("Country is: ", Country)

print("\n")

#Question 2: Username Generator (String)
#first_name= input("Enter your first name: ")
#last_name= input("Enter your last name: ")
#sername= first_name+last_name
#print("Your username is: ", username.lower())

print("\n")

#Question 3: Shopping List (List)
shopping_list= ["milk", "bread", "eggs", "fruits", "vegetables"]
print("first on the list is: ", shopping_list[0])
print("last on the list is: ", shopping_list[-1])
shopping_list.append("meat")
shopping_list.remove("vegetables")
print("Updated shopping list is: ", shopping_list)

print("\n")

#Question 4: Student Scores (List)
marks= [85, 90, 78, 92, 88]
print("Highest score is: ", max(marks))
print("Lowest score is: ", min(marks))
print("the sum of all scores is: ", sum(marks))
print("the average score is: ", sum(marks)/len(marks))

print("\n")

#Question 5: Days of the Week (Tuple)
weeks= ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("First day of the week is: ", weeks[0])
print("fourth day of the week is: ", weeks[3])
print("last day of the week is: ", weeks[-1])

print("\n")

#Question 6: Employee Record (Dictionary)
employee={
    "employee_id": 12345,
    "Name": "irera josue",
    "Department": "IT",
    "Salary": 5000
}
print("Employee name is: ", employee["Name"])
employee["Salary"]= 6000
employee["email"]= "irerajosue07@gmail.com"
print("Updated employee record is: ", employee)

print("\n")

#Question 7: Library System (Dictionary)
book={
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year_published": 1925,
    "price": 15000
}
print("Book informations are: ", book)

print("\n")

#Question 8: Classroom Management (List + Dictionary)
students= [
    {
        "name": "Alice",
        "age": 20,
        "course": "Computer Science"
    },
    {
        "name": "Bob",
        "age": 22,
        "grade": 90
    },
    {
        "name": "Charlie",
        "age": 21,
        "course": "Mathematics"
    }
]
print("First Student's information is: ", students[0])
print("Second Student's information is: ", students[1])
print("Third Student's information is: ", students[2])

print("\n")

#Question 9: Personal Bio (All Data Types)
Name= "irera josue"
skills= ["Python", "Django", "JavaScript"]
date_of_birth= (2001, 3, 28)
contact_information= {
    "email": "irerajosue07@gmail.com",
    "phone": 1234567890
}
print("Name is: ", Name)
print("Skills are: ", skills)
print("Date of birth is: ", date_of_birth)
print("Contact information is: ", contact_information)

print("\n")

#Question 10: Student Marks Calculation (Arithmetic Operations)
contact_info={
    "irera": "7277443",
    "john": "9876543",
    "jane": "5555555"
}
search_name = input("Enter a name to search: ").strip()

# Search and display the result
if search_name in contact_info:
    print(f"{search_name}'s phone number is: {contact_info[search_name]['Phone_number']}")
else:
    print(f"Contact '{search_name}' was not found.")