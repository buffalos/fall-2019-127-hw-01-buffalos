s,t= map(int, input().split())
a,b= map(int, input().split())
m,n=map(int, input().split())
appledistances=map(int, input().split())
orangedistances=map(int, input().split())

numofapples=0
numoforanges=0
for x in appledistances:
    if s <= a + x <= t:
        numofapples += 1

for x in orangedistances:
    if s <= b + x <= t:
        numoforanges += 1
print("Inputs")
print(s, t)
print(a, b)
print(m, n)
print("Number of Apples and Oranges")
print(numofapples)
print(numoforanges)
