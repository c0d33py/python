# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules


# user3 = User('starup', 'digicom', 2008)



# Core modules
# import datetime


# from datetime import date
# import time
# from time import time

# Pip module

# Import custom module
# import validator
from validator import validate_email

# today = datetime.date.today()
# today = date.today()
# print(today)
# timestamp = time()


email = input('type user email: ')



if validate_email(email):
  print('Email is valid')
else:
  print('Email is bad')
