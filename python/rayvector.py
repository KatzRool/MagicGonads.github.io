from math import *
from cmath import *
import turtle as T

#Data

c=3*10**8
class vec():
    def __init__(self,v):
        if isinstance(v,vec):
            v = [v[0],v[1]]
        else:
            v = [v.real,v.imag] if isinstance(v,complex) else v
            v = list(v) if isinstance(v,list) or isinstance(v,tuple) else [v]
            v+= [0]*(len(v)==1)
        self.it = v
        self.c = complex(v[0],v[1])
    @classmethod
    def pol(cls,r,t):
        return vec([r*cos(t),r*sin(t)])
    def __iter__(self):
        return self.it.__iter__()
    def __getitem__(self,key):
        return self.it.__getitem__(key)
    def __setitem__(self,key,value):
        it = list(self.it)
        it[key] = value
        self.c = complex(it[0],it[1])
        self.it = (it[0],it[1])
    def __contains__(self,other):
        return self.it.__contains__(other)
    def arg(v):
        return atan2(v.c.imag,v.c.real)
    def abs(v):
        return abs(v.c)
    def __abs__(v):
        return v.abs()
    def __repr__(v):
        return v.c.__repr__()
    def __str__(v):
        return v.c.__str__()
    def __mul__(v,u):
        u = vec(u)
        return vec(u.c*v.c)
    __rmul__ = __mul__
    def __add__(v,u):
        u = vec(u)
        return vec(u.c+v.c)
    __radd__ = __add__
    def __pow__(v,u):
        u = vec(u)
        return vec(v.c**u.c)
    def __rpow__(v,u):
        u = vec(u)
        return vec(u.c**v.c)
    def __truediv__(v,u):
        u = vec(u)
        return vec(v.c/u.c)
    def __rtruediv__(v,u):
        u = vec(u)
        return vec(u.c/v.c)
    def __neg__(v):
        return -1*v
def arg(v):
    v = vec(v)
    return v.arg()
def reflect(v,N=1j):
    return vec.pol(abs(v),2*arg(N)-arg(v))
def refract(v,N=1j,n=1):
    if n == 0:
        return float(inf)
    A = vec.pol(1,arg(N)-asin(sin(arg(N)-arg(v))*c/abs(v)*n))
    return A/abs(A)*c/n
def refractA(v,N=1j,n=1):
    if n == 0:
        return float(inf)
    if abs(v) == 0:
        return 0
    return arg(N)-asin(sin(arg(N)-arg(v))*c/abs(v)/n)
def indicies(v,r):
    return (c/abs(v),c/abs(r))
def collide(v,N=1j,n=1):
    if refractA(v,N,n).imag:
        return reflect(v,N)
    return refract(v,N,n)

#Render

def setup():
    global writer
    T.bgcolor('black')
    T.tracer(False)
    T.mode("logo")
    plane('surface',NOR)
    surface = T.Turtle()
    surface.shape('surface')
    direct('norm',NOR)
    norm = T.Turtle()
    norm.shape('norm')
    inray('in',INV)
    inarrow = T.Turtle()
    inarrow.shape('in')
    OUT = refract(INV,NOR,REF)
    outray('out',OUT)
    outarrow = T.Turtle()
    outarrow.shape('out')
    for shp in surface,norm,inarrow,outarrow:
        shp.resizemode("user")
        shp.shapesize(1,1,SIZ)
        shp.speed(0)
        shp.color(colour)
    norm.shapesize(1,1,SIZ//2)
    T.ht() 
    writer = T.Turtle()
    writer.ht()
    writer.pu()
    writer.color(colour)
    writer.clear()
    writer.home()
    h = T.window_height()
    writer.forward(h/3+35)
    writer.write('SELECTED: '+('Vi','N','Rr','c')[OBJ],
                 align="center", font=("Courier", 14, "bold"))
    writer.back(35)
    writer.write('Rr = '+str(REF),
                 align="center", font=("Courier", 14, "bold"))
    writer.back(35)
    writer.write('c = '+str(VEL),
                 align="center", font=("Courier", 14, "bold"))
    writer.forward(85)
    writer.home()
    writer.backward(h/3+35)
    writer.write('Vr = '+str(OUT),
                 align="center", font=("Courier", 14, "bold"))
    writer.forward(35)
    writer.write('Ri = '+str(VEL/abs(INV)),
                 align="center", font=("Courier", 14, "bold"))
    writer.forward(35)
    writer.write('Vi = '+str(INV),
                 align="center", font=("Courier", 14, "bold"))
    T.tracer(True)

def direct(name,v):
    v = vec(v)
    d = v.abs()
    T.reset()
    T.penup()
    T.home()
    T.begin_poly()
    T.left(v.arg()*180/pi)
    T.right(90)
    T.forward(d)
    T.backward(2*d)
    T.end_poly()
    T.register_shape(name,T.get_poly())

def plane(name,v):
    v = vec(v)
    T.reset()
    d=abs(NOR)
    T.penup()
    T.setpos(0,0)
    T.pendown()
    T.begin_poly()
    T.left(v.arg()*180/pi)
    T.forward(d)
    T.backward(2*d)
    T.end_poly()
    T.register_shape(name,T.get_poly())

def inray(name,v):
    v=vec(v)
    T.reset()
    T.penup()
    T.setpos(-v[0],-v[1])
    T.pendown()
    r = v.abs()
    T.begin_poly()
    T.left(v.arg()*180/pi)
    T.right(90)
    T.forward(r/2)
    T.right(140)
    T.forward(10)
    T.backward(10)
    T.right(80)
    T.forward(10)
    T.backward(10)
    T.right(140)
    T.forward(r/2)
    T.end_poly()
    T.register_shape(name,T.get_poly())

def outray(name,v):
    v=vec(v)
    T.reset()
    r = v.abs()
    T.begin_poly()
    T.right(v.arg()*180/pi)
    T.forward(r/2)
    T.right(140)
    T.forward(10)
    T.backward(10)
    T.right(80)
    T.forward(10)
    T.backward(10)
    T.right(140)
    T.forward(r/2)
    T.end_poly()
    T.register_shape(name,T.get_poly())

def newOBJ(x=0,y=0):
    global OBJ
    OBJ+=1
    OBJ%=4
    recall()

def setOBJ(x,y):
    global INV, NOR, REF, VEL, OBJ
    k = complex(x,y)
    if OBJ==0:
        INV = -k
    elif OBJ==1:
        NOR = k
    elif OBJ==2:
        REF = k/100
    elif OBJ==3:
        VEL = k
    recall()

def recall():
    global c, VEL
    c = VEL
    setup()
    T.tracer(True)

def regen(x=0,y=0):
    tracer(False)
    T.reset()
    main()

def main():
    global INV, NOR, REF, VEL, SIZ, OBJ, colour
    INV = 100+100j
    NOR = 100j
    REF = 1
    VEL = 100
    SIZ = 2
    OBJ = 0
    colour = 'orange'
    T.onscreenclick(setOBJ,1)
    T.onscreenclick(regen,2)
    T.onscreenclick(newOBJ,3)
    recall()

if __name__ == "__main__":
    input()
    T.mode("logo")
    main()
    T.mainloop()
