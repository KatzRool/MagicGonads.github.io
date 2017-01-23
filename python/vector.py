from math import cos, sin, radians, degrees, acos, atan, atan2
class vec:
    #Instance Methods
    def __init__(self,x=0,y=0,z=0):
        self.car = (x,y,z)
        self.update()
    def update(self):
        x,y,z = self.car[0],self.car[1],self.car[2]
        r = (x**2+y**2+z**2)**0.5
        d = 1.0/(z+vec.per_w) if z+vec.per_w > 0 else vec.per_m
        d = d if d < vec.per_m else vec.per_m
        self.iso = (vec.iso_x*(x-y),vec.iso_y*(x+y+z*vec.iso_z))
        self.pol = (r,degrees(atan2(y,x)),degrees(acos(z/(r+(r==0)))))
        self.per = (x*d,y*d)
        self.com = complex(x,y)
    @classmethod
    def polar(cls,r=0,t=0,p=0):
        p,t = radians(p),radians(t)
        return cls(r*sin(p)*cos(t),r*sin(p)*sin(t),r*cos(p))
    #Class Variables
    mat = {'x':['x','y*cos(t)-z*sin(t)','y*sin(t)+z*cos(t)'],
           'y':['x*cos(t)+z*sin(t)','y','-x*sin(t)+z*cos(t)'],
           'z':['x*cos(t)-y*sin(t)','x*sin(t)+y*cos(t)','z']}
    iso_x = 3**0.5
    iso_y = 1
    iso_z = 2
    per_w = 1
    per_m = 562949953421312
    #Class Methods
    def rotate(self,angle=90,axis='z'):
        t = radians(angle)
        x,y,z = self.car[0],self.car[1],self.car[2]
        vector = vec(eval(vec.mat[axis][0]),eval(vec.mat[axis][1]),eval(vec.mat[axis][2]))
        vector.update()
        return vector
    def __repr__(self):
        return str(self.car)
    def __add__(self,other):
        if type(other) in (int,float,bool):
            other = vec(other/3,other/3,other/3)
        return vec(self.car[0]+other.car[0],self.car[1]+other.car[1],self.car[2]+other.car[2])
    def __radd__(self,other):
        return other - self
    def __sub__(self,other):
        if type(other) in (int,float,bool):
            other = vec(other/3,other/3,other/3)
        return vec(self.car[0]-other.car[0],self.car[1]-other.car[1],self.car[2]-other.car[2])
    def __rsub__(self,other):
        return self + other
    def __mul__(self,other):
        if type(other) in (int,float,bool):
            other = vec(other,other,other)
        return vec(self.car[0]*other.car[0],self.car[1]*other.car[1],self.car[2]*other.car[2])
    def __rmul__(self,other):
        return self * other
    def __truediv__(self,other):
        if type(other) in (int,float,bool):
            other = vec(other,other,other)
        return vec(self.car[0]/other.car[0],self.car[1]/other.car[1],self.car[2]/other.car[2])
    def __rtruediv__(self,other):
        return other/self.pol[0]
    def __floordiv__(self,other):
        if type(other) in (int,float,bool):
            other = vec(other,other,other)
        return vec(self.car[0]//other.car[0],self.car[1]//other.car[1],self.car[2]//other.car[2])
    def __rfloordiv__(self,other):
        return other//self.pol[0]
    def __mod__(self,other):
        if type(other) in (int,float,bool):
            other = vec(other,other,other)
        return vec(self.car[0]%other.car[0],self.car[1]%other.car[1],self.car[2]%other.car[2])
    def __rmod__(self,other):
        return other%self.pol[0]
    def __pow__(self,other):
        if type(other) in (int,float,bool):
            other = vec(other,0,0)
        return vec(self.car[0]**other.pol[0],self.car[1]**other.pol[1],self.car[2]**other.pol[0])
    def __rpow__(self,other):
        return other**self.pol[0]
    def __lt__(self,other):
        if type(other) in (int,float,bool):
            other = vec(other,0,0)
        return self.pol[0]<other.pol[0]
    def __le__(self,other):
        if type(other) in (int,float,bool):
            other = vec(other,0,0)
        return self.pol[0]<other.pol[0]
    def __gt__(self,other):
        if type(other) in (int,float,bool):
            other = vec(other,0,0)
        return self.pol[0]>other.pol[0]
    def __ge__(self,other):
        if type(other) in (int,float,bool):
            other = vec(other,0,0)
        return self.pol[0]>=other.pol[0]
    def __eq__(self,other):
        if type(other) in (int,float,bool):
            return self.pol[0]==other
        return (self.car[0]==other.car[0])&(self.car[1]==other.car[1])&(self.car[2]==other.car[2])
    def __ne__(self,other):
        return ~(self==other)
    def __and__(self,other):
        return bool(self)&bool(other)
    def __rand__(self,other):
        return self&other
    def __xor__(self,other):
        return bool(self)^bool(other)
    def __rxor__(self,other):
        return self^other
    def __or__(self,other):
        return bool(self)|bool(other)
    def __ror__(self,other):
        return self|other
    def __neg__(self):
        return self*-1
    def __invert__(self):
        return vec(self.car[0],-self.car[1],-self.car[2])
    def __abs__(self):
        return self.pol[0]
    def __nonzero__(self):
        return self.pol[0] != 0
    def __str__(self):
        return '('+','.join(self.car)+')'
    def __int__(self):
        return int(self.pol[0])
    def __complex__(self):
        return self.com
