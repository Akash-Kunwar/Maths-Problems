def flame(a, b): 
    l, sc = 1, 0
    rc, fc = 0, 5
    f = "flames"
    f = [i for i in f] 
    q = "".join(a) 
    w = "".join(b) 
      
    # print(q, w) 
    n = len(a) 
    m = len(b) 
    tc = n + m 
    for i in range(n): 
        c = a[i] 
        for j in range(m): 
            if (c == b[j]): 
                a[i] = -1
                b[j] = -1
                sc = sc + 2
                break
  
    rc = tc - sc 
    i = 0
  
    while (i): 
        if (l == (rc)): 
            for k in range(i,len(f)): 
                f[k] = f[k + 1] 
            f[k + 1] = '\0'
            fc = fc - 1
            i = i - 1
            l = 0
        if (i == fc): 
            i = -1
        if (fc == 0): 
            break
        l += 1
        i += 1
  
    # Print the results 
    if (f[0] == 'e'): 
        print(q, "is ENEMY to", w) 
    elif (f[0] == 'f'): 
        print(q, "is FRIEND to", w) 
    elif (f[0] == 'm'): 
        print(q, "is going to MARRY", w) 
    elif (f[0] == 'l'): 
        print(q, "is in LOVE with", w) 
    elif (f[0] == 'a'): 
        print(q, "has more AFFECTION on", w) 
    else: 
        print(q, "and", w, "are SISTERS/BROTHERS ") 
  
# Driver code 
a = input()
b = input()
a = [i for i in a] 
b = [j for j in b] 
  
# print(a,b) 
flame(a, b) 