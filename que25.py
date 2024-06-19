#5. Write a program that copies the contents of one text file to another

input = 'C:/Users/Home/Desktop/ASSIGNMENT1internship/input.txt'
output = 'C:/Users/Home/Desktop/ASSIGNMENT1internship/output.txt'


with open(input, 'r') as file_input:
    with open(output, 'w') as file_output:
       
        content = file_input.read()
        
        file_output.write(content)

print(f"Contents of '{input}' copied to '{output}' successfully.")
