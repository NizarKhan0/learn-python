# my_file = open('test.txt')

# print(my_file)
# print(my_file.read())
# my_file.seek(0)  # Reset file pointer to the beginning
# print(my_file.read())
# my_file.seek(0)  # Reset file pointer to the beginning
# print(my_file.read())
# print(my_file.readline(2))  # Read the first line
# print(my_file.readlines())  # Regular example to read all lines
# my_file.close()  # Close the file after reading

# Read, Write, and Append to a File

# r+ mode allows reading and writing
# w+ mode allows writing and reading, truncating the file first
# a+ mode allows appending and reading, creating the file if it doesn't exist
# with open('test.txt', mode='w') as my_file:
#     text = my_file.write('Huyy, Chiao!\n')  # Write to the file
#     print(text)
    # print(my_file.readlines())  # Read all lines

# create a new file and write to it
with open('new_file.txt', mode='w') as my_file:
    text = my_file.write('Nihaoo, Xiao!\n')  # Write to the file
    print(text)