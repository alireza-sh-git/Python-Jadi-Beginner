import math 
number = int(input('Please enter a number: '))
div = 2
while div <= math.sqrt (number):
    if number % div == 0:
        print('Not prime')
        break
    else:
        div +=1
if div > math.sqrt(number):
    print('Prime')
