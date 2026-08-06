#Trafics
colors=["red", "green", "yellow"]
color=input("Enter a color: ")
color=color.lower()
if colors[0] == color:
    print("Stop")
if color in colors:
    print("The color is in the list")
elif colors[1] == color:
    print("Go")
elif colors[2] == color:
    print("Slow down") 
else:
    print("Invalid color")   

print("\n")

#Grades
marks=int(input("Enter your marks: "))
if marks>=80:
    print("Grade is A")
elif marks>=70:
    print("Grade is B")
elif marks>=60:
    print("Grade is C")
elif marks>=50:
    print("Grade is D")
else:
    print("Grade is F")