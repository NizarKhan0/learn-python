from translate  import Translator

translator = Translator(to_lang="ja")

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
# with open('new_file.txt', mode='w') as my_file:
#     text = my_file.write('Nihaoo, Xiao!\n')  # Write to the file
#     print(text)

# read file with different file path

# relative path
with open('app/sad.txt', mode='r') as my_file:
    print(my_file.read())  # Read the entire file content

# absolute path
with open(r'C:\laragon\www\learn-python\source-1\file-IO\app\sad.txt', mode='r') as my_file:
    print(my_file.read())  # Read the entire file content

# ./ - Current directory
# .. - Parent directory
with open('./app/sad.txt', mode='r') as my_file:
    print(my_file.read())  # Read the entire file content


# File IO - Errors
# Handling file not found error
try:
    with open('non_existent_file.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    # print(f"Error: {e}")
    print("File not found. Please check the file path and try again.")
    raise err
except IOError as err:
    print("An IOError occurred. Please check the file permissions or disk space.")
    raise err


# Exercise

try:
    with open('./name.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as err:
    print("File not found. Please check the file path and try again.")
    raise err