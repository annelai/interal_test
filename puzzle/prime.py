q = 600851475143
ans = 0
for p in range(q,0,-1):
    if ans!=0:
        break
    for i in range(2,p):
        if p%i==0: # not a prime
            continue
    ans = p
print (ans)
