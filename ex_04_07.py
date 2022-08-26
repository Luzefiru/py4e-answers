# function for calculating grades & returning string for result
def computegrade(ungraded):
    if ungraded > 0.0 and ungraded < 1.0:
        if ungraded >= 0.9:
            return 'A'
        elif ungraded >= 0.8:
            return 'B'
        elif ungraded >= 0.7:
            return 'C'
        elif ungraded >= 0.6:
            return 'D'
        elif ungraded < 0.6:
            return 'F'
    else:
        return 'Bad score'

score = input('Enter score: ')
try:
    score = float(score)
except:
    print('Bad score')
    exit()

print(computegrade(score))