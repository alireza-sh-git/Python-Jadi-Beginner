
totalPoints = 0
totalWins = 0
for i in range(5):
    thisGame = int(input("Please enter the number of points for this game: "))
    totalPoints += thisGame
    if thisGame==3:
        totalWins += 1
print("Number of wins:", totalWins)
print("Total Points:", totalPoints)