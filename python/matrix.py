class Matrix:
    def __init__(self,*terms):
        self.terms = []
        for i in terms:
            self.terms.append(str(Vector(i)))
    def __getitem__(self,index):
        if len(self.terms)>index:
            return eval(self.terms[index])
        return Vector()
    def __bool__(self):
        return len(self)>0
    def __eq__(self,other):
        return self.terms == Vector(other).terms
    def __nq__(self,other):
        return self.terms != Vector(other).terms
    def __setitem__(self,index,vec):
        self.terms[index] = str(Vector(vec))
    def __delitem__(self,key):
        del self.terms[index]
    def __missing__(self,key):
        return Vector()
    def __len__(self):
        return len(self.terms)
    def __contains__(self,num):
        return str(num) in self.terms
    def __repr__(self):
        return 'Matrix('+','.join(self.terms)+')'
    __str__ = __repr__
    def mult(self,other):
        res = []
        vec = []
        for i in range(len(self)):
            num = []
            for j in self:
                num+=[j[i]]
            vec += [sum(num)]
            vec = Vector(vec)
        for i in other:
            num = []
            for j in range(len(other)):
                num+= [i[j]]
            res+= [sum(num)*vec]
        return Matrix(res)
class Vector:
    def __init__(self,*terms):
        if len(terms)>0:
            if isinstance(terms[0],tuple) or isinstance(terms[0],list) or isinstance(terms[0],Vector):
                terms = terms[0]
            elif isinstance(terms[0],dict):
                terms = list(terms[0].values())
        self.terms = []
        self.nums = []
        for i in terms:
            self.terms.append(str(i))
            self.nums.append(i)
    def __bool__(self):
        return len(self)>0
    def __eq__(self,other):
        return self.terms == Vector(other).terms
    def __nq__(self,other):
        return self.terms != Vector(other).terms
    def __getitem__(self,index):
        if len(self.terms)>index:
            return eval(self.terms[index])
        return 0
    def __setitem__(self,index,num):
        self.terms[index] = str(num)
        self.nums[index] = num
    def __delitem__(self,key):
        del self.terms[index]
    def __missing__(self,key):
        return 0
    def __len__(self):
        return len(self.terms)
    def __contains__(self,num):
        return str(num) in self.terms
    def __repr__(self):
        return 'Vector('+','.join(self.terms)+')'
    __str__ = __repr__
    def __add__(self,other):
        return self.add(other)
    __radd__ = __add__
    def __mul__(self,other):
        return self.mult(other)
    __rmul__ = __mul__
    def add(self, other):
        if not isinstance(other,Vector):
            other = Vector(other)
        return Vector([self[i]+other[i] for i in range(max(len(self),len(other)))])
    def mult(self,other):
        if isinstance(other,Matrix):
            return other.mult(self)
        if isinstance(other,str):
            other = eval(other)
        if isinstance(other, Vector) or isinstance(other, list) or isinstance(other, dict) or isinstance(other, tuple):
            other = other[0]
        return Vector([self[i]*other for i in range(len(self))])
