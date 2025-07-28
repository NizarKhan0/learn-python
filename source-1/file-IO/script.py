my_file = open('test.txt')

# print(my_file)
# print(my_file.read())
# my_file.seek(0)  # Reset file pointer to the beginning
# print(my_file.read())
# my_file.seek(0)  # Reset file pointer to the beginning
# print(my_file.read())
# print(my_file.readline(2))  # Read the first line
print(my_file.readlines())  # Regular example to read all lines
my_file.close()  # Close the file after reading