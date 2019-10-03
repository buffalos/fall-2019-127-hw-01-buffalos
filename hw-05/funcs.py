def findmin(l):
    print(min(l))
findmin([1, 2, -3])



def findmini(l):
    index = l.index(min(l))
    print(index)
findmini([1, -2, -3])



def isGoodPassword(w):
    val = True
    w = "Pizza123!"
    capitals = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lowers = ["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['!','@','#','$','%','^','&','*','?']
    while val:
        if len(w) < 8:
            break
        elif not any(char in capitals for char in w):
            break
        elif not any(char in lowers for char in w):
            break
        elif not any(char in numbers for char in w):
            break
        elif not any(char in symbols for char in w):
            break
        else:
            print('good password')
            val = False
            break
    if val:
        print("not good password")
  
isGoodPassword("Pizza123!")
