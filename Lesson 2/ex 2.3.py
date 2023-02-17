
maxAge = newCandidateAge = 0
while newCandidateAge != -1:
    newCandidateAge = int(input("Please enter the candidate age: "))
    if newCandidateAge > maxAge:
        maxAge = newCandidateAge
print ('The maximum age is', maxAge)