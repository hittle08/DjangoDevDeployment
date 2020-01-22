# A List is a collection which is ordered and changeable. Allows duplicate members.

#create list
#numbers = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'Grapes', 'Pears', 12]

#using a constructor
numbers = list ((1,2,3,4,5))


print(type(numbers))

#Get value
print(fruits[1])

#get length
print(len(fruits))

#append list
fruits.append('Mangos')
print(fruits)

#remove from list
fruits.remove('Grapes')
print(fruits)

#Insert into specific postion
fruits.insert(2, 'Strawberries')
print(fruits)

#remove from position
fruits.pop(3)
print (fruits)

#Reverse list
fruits.reverse()
print (fruits)