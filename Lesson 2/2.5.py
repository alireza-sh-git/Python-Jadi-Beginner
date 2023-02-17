import math
def numberOfDivs(n):
    i=1
    div = 0
    while i<= math.sqrt(n):
        if n%i == 0:
            if i==math.sqrt(n):
                div+=1
            else:
                div+=2
        i+=1
    return div


largestNumberOfDivs = answer = 0
for i in range(20):
    newNumber = int(input('Please enter a new number: '))
    newNumberDivs = numberOfDivs(newNumber)
    if (newNumberDivs>largestNumberOfDivs) or ((newNumberDivs==largestNumberOfDivs) and (newNumber>answer)):
        answer = newNumber
        largestNumberOfDivs = newNumberDivs

print (answer, largestNumberOfDivs)