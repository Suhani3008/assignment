#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines


lines = []

while True:
    line = input("Enter a line (empty line to stop): ")
    if line == "":
        break
    lines.append(line)

print("Lines entered:")
for line in lines:
    print(line)
