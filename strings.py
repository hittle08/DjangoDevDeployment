# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Brad"
age = 30

#Concatenate
print('Hello ' + name)
print('Hello I am ' + name + 'my age is ' + str(age))

# String Formatting

# Arguments by position
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

#Arguments by name
print('My name is  {name} and I am {age}'.format(name='Brad', age = '37'))

#F-Strings only in 3.6+
print(f'My name is {name} and I am {age}')

# String Methods

s = 'Hello There World'

# Capitalize first letter
print(s.capitalize())