# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#simple dictionary
person = {
    'first_name': 'john',
    'last_name': 'doe',
    'age': 30
}



#access a single value
print(person['first_name'])
print(person.get('last_name'))

#add item
person['phone'] = '555-555-5555'

#get keys
print(person.keys())

#get values
print(person.items())

#Make copy
person2 = person.copy()
person2['city'] = 'Boston'

print(person2)

#list of dict
people = [
    {'name': 'Martha', 'age': 40}, 
    {'name' : 'Bob', 'age': 20}
]

print(people)