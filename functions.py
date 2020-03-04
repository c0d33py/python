# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces

def Index():
    print('hello world')

# Index()
# Index()
# Index()

# local variables globle variables
# def Index2():
#     """ local"""
#     print('hello django.')

""" globle"""
# print('hello django!')
# print('hello django!')
# print('hello django!')
# print('hello django!')
# Index2()

# return method
# def new_func():
#     return 'hello function.'

# print(new_func().upper())

def say_hi(name, version):
    # print('hello ' + name + ' the version is ' + version)
    return f'hello {name}  the version is {version}'

# say_hi('django', '3.2')
print(say_hi('Djano', '3.8'))

# return method 2
def new_func2(name):
    return f'hello {name}'
print(new_func2('django'))



# Create function
def sayHello(name='Sam'):
    print(f'Hello {name}')

sayHello()



