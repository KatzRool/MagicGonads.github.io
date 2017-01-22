def pattern(s,o,n):
    'List Parsing Pattern'
    return [j for j in [n] for i in s for j in [eval(o)]]
def product(n,m=1,o='i'):
    'Product'
    return pattern(range(m,n+1),'j*'+o,1)[-1] if n>m else 1
def sigma(n,m=1,o='i'):
    'Sigma, Summation'
    return pattern(range(m,n+1),'j+'+o,0)[-1] if n>m else 0
def integral(o,m=-1,n=1,d=1):
    'Definite Integral'
    return sigma(n*d,m*d,'(lambda i: eval(str('+o+')))(i/'+str(d)+')/'+str(d))
def power(b,n=1):
    'Integer Exponentiation'
    return pattern([b]*abs(n)+[1]*(n==0),'j'+'*i'*(n>0)+'/i'*(n<0),1)[-1]
def factorial(n):
    'Factorial'
    return product(n+(n==0))
def e(d=40):
    'Euler Constant'
    return sigma(d,0,'1/factorial(i)')
e_ = e()
def ln(x,d=500):
    'Natural Logarithm'
    return sigma(d,1,'power(-'+str((1/x)-1)+',i)/i') if x != 0 else float('inf')
def log(x,b=e_,d=500):
    'Arbitrary Base Logarithm'
    return ln(x,d)/ln(b,d)
def exp(n=1, d=40):
    'Exponential'
    return power(e_,round(n))*power(sigma(d,0,'pow('+str(n-round(n))+',i)/factorial(i)'))
def index(b,n=1,d=250):
    'Real Exponentiation'
    return (power(b,n) if n == int(n) else exp(n*ln(b,d))) if b != 0 else (n==0)*1
def zeta(s=3,d=30):
    'Reinmann Zeta Function'
    return sigma(d,1,'1/index(i,'+str(s)+')')
def mascheroni(d=20):
    'Euler-Mascheroni Constant'
    return sigma(d,2,'index(-1,i)*zeta(i)/i')
mascheroni_ = mascheroni()
def gamma(t=0,d=40):
    'Gamma Function'
    return factorial(t-1) if t>0 and t == int(t) else (float('inf') if t/(abs(t)+(t==0)) == int(t) and t == int(t) else exp(-t*mascheroni_)/t*product(d,1,'power(1+'+str(t)+'/i,-1)*exp('+str(t)+'/i)'))
def fall(x,n):
    'Falling Factorial'
    return gamma(x+1)/gamma(x-n+1)
def rise(x,n):
    'Rising Factorial'
    return gamma(x+n+1)/gamma(x+1)
def choose(n=1,k=0):
    'Choose Function, Binomial Coefficient'
    return fall(n,k)/gamma(k+1)
def floor(x):
    'Floor, Round Down'
    return int(x)
def ceiling(x):
    'Ceiling, Round Up'
    return int(x)+(x!=int(x))
def modulo(x,n=2):
    'Modulo, Remainder'
    return x-n*floor(x/n)
def mediant(a,b,c=1,d=1):
    'Mediant, Farey Sum'
    return (a+b)/(c+d)
def sign(x):
    'Sign, Polarity'
    return x/abs(x+(x==0))
def pi(d=50):
    'Approximation of pi'
    return sigma(d,0,'(power(factorial(i),2)*power(2,i+1))/factorial(2*i+1)')
pi_ = pi()
def radians(x):
    'Radians'
    return pi_*x/180
def degrees(x):
    'Degrees'
    return 180*x/pi_
def sin(x,d=20):
    'Sine, Opposite/Hypotenuse'
    return sigma(d,0,'power(-1,i)*power('+str(x)+',2*i+1)/factorial(2*i+1)')
def cos(x,d=20):
    'Cosine, Adjacent/Hypotenuse'
    return sigma(d,0,'power(-1,i)*power('+str(x)+',2*i)/factorial(2*i)')
def tan(x,d=20):
    'Tangent, Opposite/Adjacent'
    return sin(x,d)/cos(x,d)
def csc(x,d=20):
    'Cosecant, Hypotenuse/Opposite'
    return 1/sin(x,d)
def sec(x,d=20):
    'Secant, Hypotenuse/Adjacent'
    return 1/cos(x,d)
def cot(x,d=20):
    'Cotangent, Adjacent/Opposite'
    return 1/tan(x,d)
def asin(x,d=20):
    'Inverse Sine'
    return sigma(d,1,'product(i,1,"2*i-1")/product(i,1,"2*i")*power('+str(x)+',2*i+1)/(2*i+1)')
def acos(x,d=20):
    'Inverse Cosine'
    return pi_/2-asin(x,d)
def atan(x,d=125):
    '#Inverse Tangent'
    return sigma(d,0,'index(2,2*i)*index(factorial(i),2)/factorial(2*i+1)*index('+str(x)+',2*i+1)/index(1+index('+str(x)+',2),i+1)')
def acsc(x,d=20):
    'Inverse Cosecant'
    return asin(1/x,d)
def asec(x,d=20):
    'Inverse Secant'
    return acos(1/x,d)
def acot(x,d=125):
    'Inverse Cotangent'
    return pi_/2-atan(x,d)
def binomial(n=2):
    'Binomial Theorem'
    return '1/('*(n<0)+'1'*(n==0)+' + '.join(pattern(range(0,abs(n)+1),'str(int(choose('+str(abs(n))+',i)))*(choose('+str(abs(n))+',i)!=1)+"y"*(i>0)+(("^"+str(i))*(i>1)+"*"*('+str(abs(n))+'-i>0 and i>0)+"x"*('+str(abs(n))+'-i>0)+("^"+str('+str(abs(n))+'-i))*(('+str(abs(n))+'-i)>1))*(choose('+str(abs(n))+',i)!=0)',0))+')'*(n<0)
def argument(x,y):
    'Argument, Angle'
    return atan(y/x)+pi_*sign(y)*(x<0) if x!=0 else sign(y)*pi_/2*(y!=0)
def absolute(x,y):
    'Absolute Value, Magnitude'
    return index(index(x,2)+index(y,2),0.5)
def phi(d=250):
    'Phi, Golden Ratio'
    return (1+index(5,0.5,d))/2
phi_ = phi()
def prime(p):
    'Wilson Primality'
    if p != int(abs(p)) or p < 2:
        return False
    return not (factorial(p-1)+1)%p
def primes(m,n=1):
    'List of Primes in [n,m]'
    return [p for p in range(n,m+1) if prime(p)]
def divisors(n):
    return [d for d in list(range(1,n//2+1))+[n] if n%d == 0]
def antiprime(c):
    return len(divisors(c))>max([len(divisors(n+(n==0))) for n in range(1,c)]+[0])
def antiprimes(m,n=1):
    return [c for c in range(n,m+1) if antiprime(c)]
class lateral:
    'Complex Number'
    def exp(l,d=40):
        'Exponential'
        if 1-(isinstance(l,int) + isinstance(l,float)):
              l = lateral(l,0)
        return lateral.polar(exp(l.re,d),l.arg())
    def prime(l):
        return prime(power(l.re,2)+power(l.im,2))
    def __init__(self,real=0,imaginary=0):
        if isinstance(real,int) or isinstance(real,float):
            self.re = real
        else:
            raise TypeError("lateral argument 'real' must be a number, not '"+real.__class__.__name__+"'")
        if isinstance(imaginary,int) or isinstance(imaginary,float):
            self.im = imaginary
        else:
            raise TypeError("lateral argument 'imaginary' must be a number, not '"+imaginary.__class__.__name__+"'")
        self.it = (self.re,self.im)
    @classmethod
    def polar(cls,radius=0,angle=0):
        if 1-(isinstance(radius,int) + isinstance(radius,float)):
            raise TypeError("lateral.polar argument 'radius' must be a number, not '"+radius.__class__.__name__+"'")
        if 1-(isinstance(angle,int) + isinstance(angle,float)):
            raise TypeError("lateral.polar argument 'angle' must be a number, not '"+angle.__class__.__name__+"'")
        return cls(radius*cos(angle),radius*sin(angle))
    def abs(self):
        return absolute(self.re,self.im)
    __abs__ = abs
    def arg(self):
        return argument(self.re,self.im)
    def __iter__(self):
        return self.it.__iter__()
    def __getitem__(self,key):
        return self.it.__getitem__(key)
    def __setitem__(self,key,value):
        it = list(self.it)
        it[key] = value
        self.re = it[0]
        self.im = it[1]
        self.it = (it[0],it[1])
    def __contains__(self,other):
        return self.it.__contains__(other)
    def __repr__(self):
        return str(self.re)*(self.re!=0)+('+'+str(self.im)+'i')*(self.im!=0)+'0'*((abs(self.re)+abs(self.im)==0))
    def __str__(self):
        return 'lateral('+str(self.re)+','+str(self.im)+')'
    def __neg__(self):
        return lateral(-self[0],-self[1])
    def __add__(self,other):
        if not isinstance(other,lateral):
            if isinstance(other,int) or isinstance(other,float):
                other = lateral(other)
            else:
                raise TypeError('unsupported operand type(s) for +: \'lateral\' and \''+other.__class__.__name__+"'")
        return lateral(self.re+other.re,self.im+other.im)
    __radd__ = __add__
    def __sub__(self,other):
        if not isinstance(other,lateral):
            if isinstance(other,int) or isinstance(other,float):
                other = lateral(other)
            else:
                raise TypeError('unsupported operand type(s) for -: \'lateral\' and \''+other.__class__.__name__+"'")
        return lateral(self.re-other.re,self.im-other.im)
    def __rsub__(self,other):
        if not isinstance(other,lateral):
            if isinstance(other,int) or isinstance(other,float):
                other = lateral(other)
            else:
                raise TypeError('unsupported operand type(s) for -: \''+other.__class__.__name__+"' and 'lateral'")
        return lateral(other.re-self.re,other.im-self.im)
    def __mul__(self,other):
        if not isinstance(other,lateral):
            if isinstance(other,int) or isinstance(other,float):
                other = lateral(other)
            else:
                raise TypeError('unsupported operand type(s) for *: \'lateral\' and \''+other.__class__.__name__+"'")
        return lateral(self.re*other.re-self.im*other.im,self.re*other.im+self.im*other.re)
    __rmul__ = __mul__
    def __truediv__(self,other):
        if not isinstance(other,lateral):
            if isinstance(other,int) or isinstance(other,float):
                other = lateral(other)
            else:
                raise TypeError('unsupported operand type(s) for /: \'lateral\' and \''+other.__class__.__name__+"'")
        return lateral.polar(self.abs()/other.abs(),self.arg()-other.arg())
    def __rtruediv__(self,other):
        if not isinstance(other,lateral):
            if isinstance(other,int) or isinstance(other,float):
                other = lateral(other)
            else:
                raise TypeError('unsupported operand type(s) for /: '+other.__class__.__name__+"' and 'lateral'")
        return lateral.polar(other.abs()/self.abs(),other.arg()-self.arg())
    def __pow__(self,other):
        if not isinstance(other,lateral):
            if isinstance(other,int) or isinstance(other,float):
                other = lateral(other)
            else:
                raise TypeError('unsupported operand type(s) for **: \'lateral\' and \''+other.__class__.__name__+"'")
        return index(self,abs(other))
    def __rpow__(self,other):
        if not isinstance(other,lateral):
            if isinstance(other,int) or isinstance(other,float):
                other = lateral(other)
            else:
                raise TypeError('unsupported operand type(s) for **: '+other.__class__.__name__+"' and 'lateral'")
        return index(other,abs(self))
class continued:
    'Continued Fraction Representation'
    def float(c):
        'Continued fraction to float'
        it = c.it[::-1]
        l = len(it)
        n = it[0]
        for i in range(l-1):
            n = it[i+1]+1/n
        return n
    def __init__(self,n,l=0):
        l = len(repr(n)) if l==0 else l
        it = []
        for i in range(l):
            it+=[int(n)]
            k = n-it[-1]
            if k==0:
                break
            n = 1/k
        self.it = it
    def __iter__(self):
        return self.it.__iter__()
    def __getitem__(self,key):
        return self.it.__getitem__(key)
    def __setitem__(self,key,value):
        it = list(self.it)
        it[key] = value
        self.re = it[0]
        self.im = it[1]
        self.it = (it[0],it[1])
    def __len__(self):
        return len(self.it)
    def __repr__(self):
        return ';'.join(str(self.it).split(',',1)).replace(' ','')
    __str__ = __repr__
    def __add__(self,other):
        return self.float()+other
    __radd__=__add__
    def __sub__(self,other):
        return self.float()-other
    def __rsub__(self,other):
        return other-self.float()
    def __mul__(self,other):
        return self.float()*other
    __rmul__=__mul__
    def __truediv__(self,other):
        return self.float()/other
    def __rtruediv__(self,other):
        return other/self.float()
    def __pow__(self,other):
        return self.float()**other
    def __rpow__(self,other):
        return other**self.float()
    def __mod__(self,other):
        return self.float()%other
    def __rmod__(self,other):
        return other%self.float()
cont = continued
def minowski(r):
    c = continued(r)
    return c[0] + sigma(len(c),1,'index(-1,i+1)/index(2,sum('+str(c.it)+'[1:i]))')
def keith(x,d=20):
    'Keith Number'
    if x>9:
        l = list(map(int,str(int(x))))
        n = len(l)
        i = 0
        while l[-1] != x and i < d:
            i+=1
            l += [sum(l)]
            l = l[::-1][0:n][::-1]
        return l[-1]*(l[-1]==x)
    else:
        return 0
def keiths(n=14,m=197,d=20):
    l = []
    for i in range(n,m+1):
        k = keith(i)
        if k:
            l+=[k]
    return l
def reg_poly_area(sides=5,radius=1,d=1):
    'Test Polar Integral'
    return integral(str(radius)+'*cos(i)*cos(360*(modulo(floor(i/(360/'+str(sides)+')),'+str(sides)+')+0.5)/'+str(sides)+')+'+str(radius)+'*sin(i)*sin(360*(modulo(floor(i/(360/'+str(sides)+')),'+str(sides)+')+0.5)/'+str(sides)+')',0,360,d)
def mplot(exp='x',start=0,end=200,scale=1):
    import matplotlib.pyplot as plt
    func = lambda x: eval(exp)
    plt.plot([x*scale for x in range(start,end+1)],[func(x*scale) for x in range(start,end+1)])
    plt.show()
