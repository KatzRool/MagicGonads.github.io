import math,turtle,colorsys
turtle.ht()
turtle.penup()
turtle.speed(-1)
scale = 10
rot = math.pi
hue = 100
sat = 80
pos = [0,0]
ref = [1,1]
lit = 1.5
cls = turtle.clear
_phi = (1+5**0.5)/2
def rotate(p=90):
    global rot
    rot += math.radians(p)
def reflect(x=-1,y=1):
    ref[0]*=x
    ref[1]*=y
def colour(h=1,s=1,v=1):
    c = '#'
    for i in colorsys.hsv_to_rgb(h,s,v):
        c+= '0'*(i<16)+hex(min(int(i),255)).replace('0x','')
    return c
def repo():
    turtle.setpos(pos[0],pos[1])
def goto(x,y):
    turtle.setpos(x*scale,y*scale)
def move(x,y):
    goto(turtle.xcor()/scale+x,turtle.ycor()/scale+y)
def axis(n,b=3,r=1):
    n = (abs(n) if n/abs(n) == 1 else abs(n)+b) if n != 0 else 0
    t = math.pi*(2*n+1)/(2*b) + rot
    return (r*math.cos(t)*ref[0],r*math.sin(t)*ref[1])
def seq(n,b):
    n = n%(2*b)
    n = -(n%b) if n>b else n
    return n
def para(i=(1,0),j=(0,1),k=None):
    x = turtle.xcor()/scale
    y = turtle.ycor()/scale
    turtle.begin_fill()
    goto(x+i[0],y+i[1])
    if k != None:
        goto(x+k[0],y+k[1])
    goto(x+j[0],y+j[1])
    turtle.end_fill()
    goto(x,y)
def struct(m,*ords):
    'm in [0:5]'
    x = turtle.xcor()
    y = turtle.ycor()
    b = len(ords)
    d = b-1
    exe = ['None','(i[0]+j[0],i[1]+j[1])','(i[0]/2+j[0]/2,i[1]/2+j[1]/2)','axis(seq(2+2*n,b),b,((ords[n]**2+ords[(n+1)%b]**2)/2)**0.5)','axis(seq(2+2*n,b),b,(ords[n]**2+ords[(n+1)%b]**2)**0.5/2)','axis(seq(2+2*n,b),b,(ords[n]**2+ords[(n+1)%b]**2)**0.5)'][m]
    for n in range(0,b):
        i = axis(seq(1+2*n,b),b,ords[n])
        j = axis(seq(3+2*n,b),b,ords[(n+1)%b])
        k = eval(exe)
        turtle.color(colour(hue/100,sat/100,abs(lit*n-b)*180/b+56))
        para(i,j,k)
def rose(rad=1,l=25,d=50,p=2,k=0,m=0):
    global rot
    _r = rad*60/d
    exe = 'struct('+str(m)+','+'*rad,'.join([str(i) for i in list(range(1,d//2+1))+list(range(2,d//2+k))[::-1]])+'*rad)'
    for i in range(l):
        rad = _r/_phi**(i//5)
        exec(exe)
        rot+=_phi**p
