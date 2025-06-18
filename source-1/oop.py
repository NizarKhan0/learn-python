# OOP Object-Oriented Programming

# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.0))
# print(type('Hello'))
# print(type([]))
# print(type(()))
# print(type({}))


# create class
class PlayerCharacters:
    # class object attribute
    membership = True
    def __init__(self, name='Anonymous', age=0):
        # if (PlayerCharacters.membership):
        if (age > 18):
         self.name = name  # attribute
         self.age = age
         

    def shout(self):
        print(f'{self.name} is shouting!')
    
    # def run(self, hello):
    #     print(f'{self.name} is running {hello}')
    
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Nizar', num1 + num2)
    
    @staticmethod
    def adding_things_static(num1, num2):
        return num1 + num2


# player1 = PlayerCharacters('Nizar', 24)
# player1.shout()

# classmethod
player3 = PlayerCharacters.adding_things(21, 3)
print(player3.age)  # Using class method to add numbers


# player2 = PlayerCharacters('John', 28)

# Corrected code snippet:
# print(player1.age)        # 24
# player1.run('in the park')  # Nizar is running in the park (no None)
# player2.shout()           # John is shouting! (no None)
# print(player2.membership) # True

# help(player1)  # help function to see the attributes and methods of the class
# help(list)  # help function to see the attributes and methods of the list class

# Example of a class with various methods and attributes
class NameOfClass():
    class_attribute = 'Value'
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        
    def method1(self):
        #code
        print(f'Method 1 called with {self.param1} and {self.param2}')
    
    @classmethod
    def class_method(cls, arg1):
        # code
        print(f'Class method called with {arg1}')
        
    @staticmethod
    def static_method(arg1):
        # code
        print(f'Static method called with {arg1}')


# Encapsulation
class EncapsulatedClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def run(self):
        print('run')
    
    def speak(self):
        print(f'my name is {self.name} and I am {self.age} years old')
        

player1 = EncapsulatedClass('Nizar', 24)
# player1.speak()  # my name is Nizar and I am 24 years old

# abstraction
player1.name = '!!!'
player1.speak = 'ILYSM'
print(player1.speak)  # ILYSM

player2 = {'name': 'John', 'age': 28}
print(f"My name is {player2['name']} and I am {player2['age']} years old")  # my name is John and I am 28 years old


# Private vs Public Attributes

# Private - attributes are not accessible outside the class and cannot be modified directly.
# class PrivateClass:
#     def __init__(self, name):
#         self._name = name  # private attribute
    
#     def get_name(self):
#         return self._name  # public method to access private attribute
    
#     def set_name(self, name):
#         self._name = name  # public method to modify private attribute
        
# # Public - attributes are accessible from outside the class and can be modified directly.
# class PublicClass:
#     def __init__(self, name):
#         self.name = name  # public attribute
    
#     def get_name(self):
#         return self.name  # public method to access public attribute
    
#     def set_name(self, name):
#         self.name = name  # public method to modify public attribute
        

# Inheritance

class User():
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
        
    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')
        
wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()