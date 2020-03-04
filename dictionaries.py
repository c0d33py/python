# # A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# # Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}
# print(person)

# # Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')
# print(person2)
# # Get value
# print(person['first_name'])
# print(person.get('last_name'))

# # Add key/value
person['phone'] = '555-555-5555'
# print(person)
# # Get dict keys
# print(person.keys())

# # Get dict items
# print(person.items())
# # Copy dict
person2 = person.copy()
person2['city'] = 'Boston'
# print(person2)
# # Remove item
del(person['age'])
# print(person)
person.pop('phone')
# print(person)
# # Clear
# person.clear()
# print(person)
# # Get length
# print(len(person))

# # List of dict
people = [
    {'name': 'adeel', 'age': 27},
    {'name': 'najam', 'age': 25}
]
print(people)


print(people[0]['name'])
