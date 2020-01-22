# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

#Simple list
people=['John', 'Will', 'Janet', 'Karen']

#Simple for loop
for person in people:
    print('Current person: ', person)

#Break out of loop

for person in people:
    print('Current person: ', person)
    if person == 'Janet':
        break

#Position of print statement matters
'''
If janet is called before the print Janet will not be called
It will stop once it see's her name in the list. 
'''
for person in people:
    if person == 'Janet':
        break
    print('Current person: ', person)
    

#Continue/Skip a part in the list
for person in people:
    if person == 'Janet':
        continue
    print('Current person: ', person)

#Range
for i in range (len(people)):
    print('Current Perons: ', people[i])

for i in range(0, 10):
    print('Number ', i)

# While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 10: 
    print ('Count ', count)
    count += 1