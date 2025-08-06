import re

pattern = re.compile('this')
string = 'search inside this text please!'

print('search' in string)  # True
print(re.search('this', string))  # <re.Match object; span=(0, 6), match='search'>

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(a)
print(b)
print(c)  # None, because 'this' does not match the entire string
print(d)  # None, because 'this' does not match the beginning of the string


# a = re.search('this', string)
print(a.span())  # <re.Match object; span=(10, 14), match='
print(a.group())  # 'this'
print(a.start())  # 10
print(a.end())  # 14

# Regular expressions 2

# regex101dotcom

pattern = re.compile(r'\d{3}-\d{2}-\d{4}')
string = 'My phone number is 123-45-6789.'

print(re.search(pattern, string))


# Regular expressions 3

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'b@b.com'
# string = 'zar'

a = pattern.search(string)
print(a)  # <re.Match object; span=(0, 7), match='


# Password validation

pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
password = 'Password123!'
print(pattern.match(password))  # <re.Match object; span=(0, 14), match='Password123!'>

# we created the password checker, but we did not implement the last rule: password has to end with a number
# <re.Match object; span=(0, 12), match='Password123'>
# The password is valid, but it does not end with a number
# To fix this, we need to change the regex to require a digit at the end
pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{7,}\d$')
password = 'Password123'
print(pattern.match(password))  # <re.Match object; span=(0, 12), match='Password123'>
# The password is valid and ends with a number