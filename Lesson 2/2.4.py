oldest = secondOldest = newCandidateAge = 0
while (newCandidateAge!=-1):
    newCandidateAge = int(input("Please enter the age of the candidate: "))
    if newCandidateAge>=oldest:
        secondOldest = oldest
        oldest = newCandidateAge
    elif (newCandidateAge>secondOldest) and (newCandidateAge<oldest):
        secondOldest=newCandidateAge

print('The oldest candidate is', oldest)
print('The second oldest candidate is', secondOldest)