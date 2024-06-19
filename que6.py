#Write a program that reads the content of a text file and prints it to the console.

read_file = 'readfile.txt'

file = open(read_file,'r')

filecontent = file.read()

print("Content of the file :",filecontent)

file.close()