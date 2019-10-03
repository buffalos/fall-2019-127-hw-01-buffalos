def mysqrt(number, guess):
    if number == 0:
        return 0
    newguess = guess +1
    while guess != newguess:
        x = number/guess
        newguess = guess
        guess = (guess + x/guess)/2
    return guess
print("this is the square root: ", mysqrt(4, 3))