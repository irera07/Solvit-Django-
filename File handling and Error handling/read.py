file = open("D:\ACADEMICS\Another Skills\Solvit(Django)\Learning\File handling and Error handling\data.txt", "w")
print(file.write("i am also a web developer"))
file.close()

with open("D:\ACADEMICS\Another Skills\Solvit(Django)\Learning\File handling and Error handling\data.txt", "a") as file:
    print(file.write("let's get together"))
    file.close