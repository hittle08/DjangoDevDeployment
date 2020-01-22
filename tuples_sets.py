# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
fruit_tuple = ('Apple', 'Orange', 'Mango')
#using constructor
#fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

#gets specific value
print(fruit_tuple[1])
print(fruit_tuple)

# A Set is a collection which is unordered and unindexed. No duplicate members.

fruit_set = {'Apple', 'Orange', 'Mango'}
print('Apple' in fruit_set)

fruit_set.add('Grape')  
print(fruit_set)
