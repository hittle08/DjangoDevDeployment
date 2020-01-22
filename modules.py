# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#Core Modules
import datetime

#Insted of bringing in the entire module you can bring in just what you need. 
from datetime import date
import time
from time import time

#import pip module
import camelcase

#import custom module
import validator
from validator import validate_email



#useing dateTime core module
# today = datetime.date.today ()
today = date.today()

#useing timestamp core module
#timestamp = time.time()
timestamp = time()
print(timestamp)
print(today)

#useing camel case from pip module
camel = camelcase.CamelCase()
text = "hello there world"
print(camel.hump(text))


#using custom imported module
email = 'test@test.com'
if validate_email(email):
    print('email is valid')
else: 
    print('not and e-mail')
