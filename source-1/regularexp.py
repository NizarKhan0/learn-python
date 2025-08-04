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