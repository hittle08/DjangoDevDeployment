# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

#Create function
def sayHello(name): 
    '''
    Prints Hello and then name. 
    '''
    print('Hello ' + name)

sayHello('sam')

#return value
def getSum(num1, num2): 
    total = num1 + num2
    return total

numSum = getSum(2, 3)

def addOnetoNum(num):
    num += + 1
    return num

num = 5

new_num = addOnetoNum(num)

print(new_num)
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2

print(getSum(9,2))

addOnetoNum = lambda num : num + 1

print(addOnetoNum(5))