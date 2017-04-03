import math, random
p = 0
n = 0
k = math.sqrt(6)
try:
    while True:
        n+=1
        if math.gcd(random.randint(1,n),random.randint(1,n))==1:
            p+=1
        k = math.sqrt(6*n/p)
        print(n,k)
except KeyboardInterrupt:
    print('\n\r'+str(n),k,'FINAL')
    raise SystemExit()
