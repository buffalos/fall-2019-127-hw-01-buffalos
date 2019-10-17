def happyladybugs(b): 
    for i in range(len(b)):
        if b[i] != '_':
            if i>0:
                if b[i]==b[i-1]:
                    continue
            if i<len(b)-1:
                if b[i]==b[i+1]:
                    continue
            return False
    return True    
g = int(input().strip())
for num in range(g):
    n = input().strip()
    b = input().strip()
    if '_' in b:
        b=sorted(b)
    if happyladybugs(b):
        print("YES")
    else:
        print("NO")
        