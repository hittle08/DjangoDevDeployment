# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User: 
    #Constructor (Note: Have to have 2 underscores before and after init)
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0 
    
    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I a balance of {self.balance}'


# Init user object
Brian = User('Brian Hittle', 'hittle@hittle.com', 30)
Janet = User('Janet Williams', 'janet@janet.com', 20)

#edit property
Brian.age = 31
Janet.has_birthday()

#Call method

print(Janet.greeting())

print(Brian.name)

#init customer
john = Customer ('John Doe', 'john@john.com', 40)

john.set_balance(500)
print(john.greeting())