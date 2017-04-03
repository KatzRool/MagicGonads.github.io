def red(x):
    while x!=2:
        if x%2:
            x=3*x+1
        else:
            x//=2
        print(x)
    return 1
def con(d=10):
    k=[0]
    x=1
    while len(k)<d:
        i=(x-1)//3
        try:
            if (x-1)%3==0 and i not in k and k[-2]/k[-3]==2:
                x=i
            else:
                x*=2
        except:
            x*=2
        k+=[x]
    return k
def dep(l):
    k = [l]
    i=-1
    while len(k)>0:
        i+=1
        if isinstance(k[0],list):
            k=k[0]
        else:
            break
    return i
def nex(x):
    if isinstance(x,list):
        for i in range(len(x)):
            x[i]=nex(x[i])
    else:
        x = [2*x,(x-1)/2]
    return x
def hek(d=10):
    x=1
    i=0
    while i<d:
        x=nex(x)
        i+=1
    return x
def les(l):
    return eval('['+str(l).replace('[','').replace(']','')+']')
def eve(n):
    return int(str(n)[-1])%2
def gen(d=10):
    import random
    s=[]
    for i in range(d):
        s+=[eve(random.random())]
    return s
def hur(s):
    x=[1]
    for i in s:
        if i:
            x+=[(x[-1]-1)/3]
        else:
            x+=[x[-1]*2]
    return x
def tek(k,w=400,h=300):
    import turtle as t
    t.screensize(w,h)
    t.speed(-1)
    t.ht()
    t.pu()
    m=max(max(k),abs(min(k)))
    n=len(k)
    for i in range(n):
        p = ((i-n/2+1/2)*2*w/n,k[i]/m*h)
        t.setpos(p[0],p[1])
        t.dot()
def col(h=1,s=1,v=1):
    import colorsys
    c = '#'
    for i in colorsys.hls_to_rgb(h,s,v):
        c+= '0'*(i<16)+hex(min(int(i),255)).replace('0x','')
    return c

def nek(k,w=400,h=300):
    import turtle as t
    t.screensize(w,h)
    t.speed(-1)
    t.ht()
    m=max(max(k),abs(min(k)))
    n=len(k)
    for i in range(n):
        t.setheading(i%2*90)
        t.circle(k[i]/m*(h,w)[i%2]/2,None,(n-i)+3)

def kek(k,w=400,h=300):
    import turtle as t
    t.pu()
    t.setpos(-w,0)
    t.pd()
    t.speed(-1)
    t.ht()
    m=max(max(k),abs(min(k)))
    n=len(k)
    for i in range(n):
        p = ((i-n/2+1/2)*2*w/n,k[i]/m*h)
        t.setpos(p[0],p[1])

def iek(k,w=400,h=300):
    import turtle as t
    t.screensize(w,h)
    t.speed(-1)
    t.ht()
    m=max(max(k),abs(min(k)))
    n=len(k)
    for i in range(n):
        t.setheading(i*360/n)
        t.pu()
        t.forward(k[i]/m)
        x,y=t.pos()
        x*=w
        y*=h
        t.setpos(x,y)
        t.pd()
        t.setpos(0,0)

def dek(k,w=400,h=300):
    import turtle as t
    t.screensize(w,h)
    t.speed(-1)
    t.ht()
    m=max(max(k),abs(min(k)))
    n=len(k)
    for i in range(n):
        t.circle(h*k[i]/m,w*k[i]/m)

def lek(k,w=400,h=300):
    import turtle as t
    t.screensize(w,h)
    t.speed(-1)
    t.ht()
    m=max(max(k),abs(min(k)))
    n=len(k)
    for i in range(n):
        p = h*k[i]/m/2
        t.pu()
        t.setpos(0,-p)
        t.pd()
        t.circle(p,None,(None,5)[p<0])#,w*k[i]/m)
        t.pu()
        t.setpos(0,0)
        t.setheading(0)

def test1():
    hue=0
    import turtle as t
    t.bgcolor('black')
    t.pd()
    while True:
        t.color(col(hue,255,1))
        tek(hur(gen(int((1-hue)*100)+1)),900,300)
        hue = hue+1/100 if hue<1 else 0
def test2():
    hue=0
    import turtle as t
    t.bgcolor('black')
    while True:
        t.color(col(hue,255,1))
        nek(hur(gen(int(hue*100)+1)),900,300)
        hue = hue+1/100 if hue<1 else 0
def test3():
    hue=0
    import turtle as t
    t.bgcolor('black')
    while True:
        t.color(col(hue,255,1))
        kek(hur(gen(int((1-hue)*100)+1)),900,300)
        hue = hue+1/100 if hue<1 else 0
def test4():
    hue=0
    import turtle as t
    t.bgcolor('black')
    while True:
        t.color(col(hue,255,1))
        dek(hur(gen(int(hue*100)+1)),180,30)
        hue = hue+1/100 if hue<1 else 0
def test5():
    hue=0
    import turtle as t
    t.bgcolor('black')
    while True:
        t.color(col(hue,255,1))
        lek(hur(gen(int(hue*100)+1)),900,300)
        hue = hue+1/100 if hue<1 else 0
