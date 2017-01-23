import re
def code(c):
    n = ord(c.upper())-64
    g = 'bee'*int(n/13)
    n%= 13
    g+= 'be'*int(n/4)
    n%= 4
    g+= 'b'*n
    return g.upper() if c.isupper() else g
def write(s):
    k = re.split('[A-Za-z]+',s)
    s = re.split('[^A-Za-z]+',s)
    m = ''
    for i in s:
        l = ''
        n = 0
        for j in i:
            l+= '~'*(n!=0)+code(j)
            n+=1
        m+=l
        try:
            m+=k[1]
            del k[1]
        except IndexError:
            pass
    return k[0]+m
def letter(c):
    try:
        n = (96,64)[c[0].isupper()]
        c = c.lower()
        n+= c.count('bee')*13
        c = c.replace('bee','')
        n+= c.count('be')*4
        c = c.replace('be','')
        n+= c.count('b')
        return chr(n)
    except IndexError:
        return ''
def read(s):
    k = re.split('[A-Za-z~]+',s)
    s = re.split('[^A-Za-z~]+',s)
    m = ''
    for i in s:
        l = ''
        h = re.split('~+',i)
        for j in h:
            l+= letter(j)
        m+=l
        try:
            m+=k[1]
            del k[1]
        except IndexError:
            pass
    return k[0]+m
def bet():
    d = {0:('','~')}
    for i in range(1,27):
        c = chr(i+96)
        d[i] = (c,code(c))
    return d
def alpha():
    k = []
    for i in bet().values():
        k+=[i[0]+':'+i[1]]
    return ' \r\n '.join(k)
