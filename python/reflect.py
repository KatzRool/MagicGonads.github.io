from math import *
import turtle
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
        return atan2(v[1],v[0])
    def abs(v):
        return sqrt(v[0]**2+v[1]**2)
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
def arg(v):
    return v.arg()
def reflect(v=100+100j,n=100j):
    v = vec(v)
    return vec.pol(abs(v),2*arg(vec(n))-arg(v))
def refract(v=100+100j,n=100j,i=1):
    v = vec(v)
    n = vec(n)
    t = arg(v)-arg(n)
    k = cos(t)*i+sin(t)*1j
    t = atan2(k.imag,k.real)+arg(n)
    return vec.pol(abs(v),t)/abs(i)
def draw(v):
    v = vec(v)
    turtle.showturtle()
    turtle.left(degrees(v.arg()))
    turtle.forward(v.abs())
    turtle.stamp()
    turtle.ht()
    turtle.setpos(0,0)
    turtle.setheading(0)
turtle.speed(-1)
c = vec(100+100j)
def ratio(n=1,i=1):
    return n/i
def index(v=c,c=c):
    return abs(vec(c))/abs(vec(v))
def move(v):
    v = vec(v)
    turtle.setpos(turtle.xcor()+v[0],turtle.ycor()+v[1])
