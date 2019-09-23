# Sohail and Bahtija

def piglatinify(sentence):
    result = " "
    for word in sentence.split():
        if word[0] in ["a", "e", "i", "o", "u"]:
            result += word + "ay "
        else:
            result += word[1:]+word[0] + "ay "
    return result
print(piglatinify("I am late to my computer science class"))
