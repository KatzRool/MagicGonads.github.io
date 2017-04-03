import math
def segment(y,x,num=6,rot=0,per=1):
    return (math.floor((math.atan2(y,x)+rot)*num/2/math.pi)%num*2+per)*math.pi/num-rot
def edge(i,n=6,r=1,p=0):
    t = 2*(i%n)*math.pi/n+p
    x = math.cos(t)*r
    y = math.sin(t)*r
    _x = '' if x == 0 or 'e' in str(x) else '-'*(x<0)+(str(abs(x))+'*')*(abs(x)!=1)+'x '
    _y = '' if y == 0 or 'e' in str(y) else (str(abs(y))+'*')*(abs(y)!=1)+'y '
    s = '0 ' if _x+_y == '' else _x+(('+ ','- ')[y<0],'-'*(y<0 and _y!=''))[_x=='' or _y=='']+_y
    return s+'= '+str(r)
def edges(n=6,r=1,p=0):
    return [edge(i,n,r,p) for i in range(n)]
def vertex(i,n=6,r=1,p=0):
    t = 2*(i%n+0.5)*math.pi/n+p+math.pi/2
    l = r/math.cos(math.pi/n)
    x = math.sin(t)*l
    y = math.cos(t)*l
    return ((x,0)['e' in str(x)],(y,0)['e' in str(y)])
def verticies(n=6,r=1,p=0):
    return [vertex(i,n,r,p) for i in range(n)]
def area(n=6,r=1):
    return math.pi*r*r if n==0 else math.tan(math.pi/n)*n*r*r
def angles(n=6):
    return (n-2)*180
def diagonals(n=6):
    return n*(n-3)/2
