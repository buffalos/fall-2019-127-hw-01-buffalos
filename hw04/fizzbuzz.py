for n in range(100):
    if n%3==0 and n%5==0:
        result = "fizzbuzz"
    elif n%3==0 and n%5 != 0:
        result = "fizz"
    elif n%3 != 0 and n%5==0:
        result = "buzz"
    else:
        result = n
    print(result)
    n = n+1
