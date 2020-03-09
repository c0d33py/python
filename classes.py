# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object


class User:
  def __init__(self, fname, lname, age):
    self.fname = fname    
    self.lname = lname    
    self.age = age   

  def fullname(self):
    return f'{self.fname} {self.lname}'
  
  def email(self):
    return f'{self.fname}.{self.lname}@gmail.com'

  
  def has_birthday(self):
    self.age += 1


user1 = User('Adeel', 'Ashraf', 25)
user2 = User('farhan', 'sundeela', 25)

# print(user1.has_birthday(age))

print(user2.email())

print(user1.fullname())




# Create class
# class User:
#   # Constructor
#   def __init__(self, name, email, age):
#     self.name = name
#     self.email = email
#     self.age = age

#   def fullname(self):
#     return f'{self.name} {self.email}'

#   def has_birthday(self):
#     self.age += 1

# print(user1.age)


# # Extend class
# class Customer(User):
#   # Constructor
#   def __init__(self, name, email, age):
#     self.name = name
#     self.email = email
#     self.age = age
#     self.balance = 0

#   def set_balance(self, balance):
#     self.balance = balance

#   def greeting(self):
#     return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# #  Init user object
# brad = User('Brad Traversy', 'brad@gmail.com', 37)
# # Init customer object
# janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

# janet.set_balance(500)

# brad.has_birthday()

