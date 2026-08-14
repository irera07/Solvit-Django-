#try:
#    a=5
#    b=a/0
#    print(b)
#except:
 #   print("Error Occured")
 
#Calculator
try:
    x = int(input("enter first number: "))
    y = input("enter second number ")
    while True:
        print("selet your choice: ")
        print("1. Addition")
        print("2. substraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = int(input("select your choice 1/2/3/4/5: "))
        if choice == 1:
            print(x + y)
        elif choice == 2:
            print(x - y)
        elif choice == 3:
            print(x * y)
        elif choice == 4:
            print(x // y)
        elif choice == 5:
            break
        else:
            print("Invalid choice")
            
except Exception as e:
    print("Error happened", e)