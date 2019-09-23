def piglatin(word):
 
    if word[0] in ("a", "e", "i", "o", "u"):
        return word + "ay"
    else:
        return word[1:] + word[:1] + "ay"

print(piglatin("car"))
