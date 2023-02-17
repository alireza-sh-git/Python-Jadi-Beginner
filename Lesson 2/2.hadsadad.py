# import random
# answer = random.randint(1,10000)
# a=int(input('Please guess the number: '))
# while(a!=answer):
#     if a>answer:
#        a= int(input("Please guess a smaller number: "))
#     else:
#        a= int(input("Please guess a larger number: "))
# print('You guessed the number correctly.')



import random
firstPossibleNumber = 1
lastPossibleNumber = 100
hint = ''

while hint!='c':
    guess = random.randint(firstPossibleNumber,lastPossibleNumber)
    hint = input('I guess '+ str(guess) + '. Is it Correct? ')
    if hint == 'c':
        print('I guessed correctly')
    elif hint == 'l':
        firstPossibleNumber = guess +1
    elif hint=='s':
        lastPossibleNumber = guess-1
    else:
        print('You did not give me a hint')
