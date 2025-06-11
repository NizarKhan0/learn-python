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
    def __init__(self, name, age):
        self.name = name  #attribute
        self.age = age
    def run(self):
        # print(f'{self.name} is running')
        print('run')
        return 'done'

player1 = PlayerCharacters('Nizar', 24)
player2 = PlayerCharacters('John', 28)

print(player1.age)
print(player2.run())
