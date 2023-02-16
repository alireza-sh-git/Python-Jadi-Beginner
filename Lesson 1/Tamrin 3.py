number = int(input('Please enter a number: '))
newNumber =2 * ((number % 10 * 100)+(number // 10 % 10 *10 )+(number // 100))
print(newNumber)