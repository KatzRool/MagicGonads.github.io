def sigma(n,m=1,f=lambda x:x):
    return [j for j in [0] for x in range(m,n+1) for j in [j+f(x)]] if n>m else 0
def integral(f,m=-1,n=1,d=1):
    return sigma(n*d,m*d,lambda i: f(i/d)/d)
def contsum(f,m=0,n=1,d=1):
    return [j for j in [0] for x in list(range(int(min(m,n)*d+0.5),int(max(m,n)*d+1.5)))[::(1,-1)[m>n]] for j in [j+f(x/d)]]
def invsum(f,m=0,n=1,d=1):
    return [j for j in [0] for x in list(range(int(min(m,n)/d+0.5),int(max(m,n)*d+1.5)))[::(1,-1)[m>n]] for j in [j+f(x*d)]]
class arrow:
    depth = 10
    def crop(self,l=0):
        it = arrow(self.it)
        if l:
            while len(it)>l:
                del it[-1]
        else:
            while it[-1]==0 and len(it)>1:
                del it[-1]
        return arrow(list(it),self.s)
    def adv(self,s):
        it = arrow(self.it)
        l = len(it)
        for i in range(l):
            if abs(s)==s:
                it[i] += s*it[i+1]
            else:
                it[l-i-1] += s*it[l-i]
        return arrow(it,self.s).crop()
    def sum(self,x):
        arrow = self
        sgn = x/abs(x+(x==0))*self.s/abs(self.s+(self.s==0))
        for i in range(int(abs(x/self.s))):
            arrow = arrow.adv(sgn)
        return arrow
    def order(self):
        s = self.crop()
        l = len(s)
        it = arrow(s.it)
        pol = []
        for i in range(l):
            a = arrow.func(lambda x: x**(l-1-i),s.s).crop()
            n = (it[l-i-1]/a[-1])
            pol+=[n]
            k = []
            for i in range(len(a)):
                it[i] -= n*a[i]
        pol = pol[::-1]
        return pol
    def poly(self):
        pol = arrow.order(self)
        s = ''
        l = len(pol)
        for i in range(l):
            if i>0 and pol[i]==abs(pol[i]):
                s+='+'
            s+= str(pol[i])
            if i>0:
                s+='*x'
                if i>1:
                    s+='**'+str(i)
        return lambda x: eval(s)
    @classmethod
    def func(cls,f,s=1):
        def _c(f,*a):
            a = [str(x) for x in a]
            try:
                return eval('f('+','.join(a)+')')
            except ZeroDivisionError:
                return 0
        d = [f]
        it = [_c(f,0)]
        for i in range(arrow.depth):
            if i:
                d += [lambda x,j: _c(d[j-1],x+s,j-1)-_c(d[j-1],x,j-1)]
            else:
                d += [lambda x,j: _c(d[0],x+s)-_c(d[0],x)]
            it+=[_c(d[i+1],0,len(d)-1)]
        return cls(it,s)
    def __call__(self,x):
        return self.sum(x)[0]
    def __init__(self,it,s=1):
        self.s = it.s if isinstance(it,arrow) else s
        try:
            it.__iter__
            self.it = list(it)
        except AttributeError:
            self.it = [it]
    def __iter__(self):
        return self.it.__iter__()
    def __str__(self):
        return 'arrow('+str(self.it)+(','+str(self.s))*(self.s!=1)+')'
    __repr__ = __str__
    def __len__(self):
        return len(self.it)
    def __getitem__(self,key):
        try:
            return self.it[key]
        except IndexError:
            return 0
    def __setitem__(self,key,value):
        if key>=len(self):
            self.it+=[0]*(key-len(self)-1)
            self.it+=[value]
        else:
            self.it[key]=value
    def __delitem__(self,key):
        del self.it[key]
    def __missing__(key):
        return 0
    def __neg__(self):
        return -1*self
    def __add__(self,other):
        it = arrow(other)
        for i in range(max(len(it),len(self))):
            it[i]+= self[i]
        return arrow(it,self.s)
    __radd__ = __add__
    def __sub__(self,other):
        it = -arrow(other)
        for i in range(max(len(it),len(self))):
            it[i]+= self[i]
        return arrow(it,self.s)
    def __rsub__(self,other):
        it = (arrow(other)).it
        se = -arrow(self)
        for i in range(max(len(it),len(self))):
            it[i]+= self[i]
        return arrow(it,self.s)
    def __mul__(self,other):
        s = self.poly()
        o = arrow(other).poly()
        return arrow.func(lambda x: s(x)*o(x)).crop()
    __rmul__ = __mul__
    def __truediv__(self,other):
        s = self.poly()
        o = arrow(other).poly()
        return arrow.func(lambda x: s(x)/o(x)).crop()
    def __rtruediv__(self,other):
        s = self.poly()
        o = arrow(other).poly()
        return arrow.func(lambda x: o(x)/s(x)).crop()
    def __mod__(self,other):
        s = self.poly()
        o = arrow(other).poly()
        return arrow.func(lambda x: s(x)%o(x)).crop()
    def __rmod__(self,other):
        s = self.poly()
        o = arrow(other).poly()
        return arrow.func(lambda x: s(x)%o(x)).crop()
    def __pow__(self,other):
        s = self.poly()
        o = arrow(other).poly()
        return arrow.func(lambda x: s(x)**o(x)).crop()
    def __rpow__(self,other):
        s = self.poly()
        o = arrow(other).poly()
        return arrow.func(lambda x: o(x)**s(x)).crop()
    def op(self,func):
        s = self.poly()
        def fun(other):
            o = arrow(other).poly()
            return arrow.func(lambda x: func(s(x),o(x))).crop()
        return fun
