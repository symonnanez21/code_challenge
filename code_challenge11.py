for s in range(1, 5):   
    for y in range(4, s, -1):     
        print(" ",end=" ")   
    for m in range(0, s -1):     
        print("*",end=" ")   
    for o in range(0, s):     
        print("*",end=" ")   
    print()     
    
for n in range(1, 4):   
    for a in range(1, n +1):     
        print(" ",end=" ")   
    for i in range(4, n, -1):     
        print("*",end=" ")   
    for e in range(3, n, -1):     
        print("*",end=" ")   
    print()