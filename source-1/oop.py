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


player1 = PlayerCharacters('Nizar', 24)
player1.shout()

# player2 = PlayerCharacters('John', 28)

# Corrected code snippet:
# print(player1.age)        # 24
# player1.run('in the park')  # Nizar is running in the park (no None)
# player2.shout()           # John is shouting! (no None)
# print(player2.membership) # True

# help(player1)  # help function to see the attributes and methods of the class
# help(list)  # help function to see the attributes and methods of the list class



