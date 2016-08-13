#Box in a Box
import math
def sgn(x):
  return x/(abs(x)+(x==0))
ent = abs(int(input("Enter size: ")))
ran = range(-math.floor(ent/2),math.floor(ent/2)+ent%2)
for y in ran:
  box = []
  y+= (y>=0)*((1-ent%2))
  for x in ran:
    x+= (x>=0)*((1-ent%2))
    i = complex(x,y)*complex(0,1)**0.5
    if (int(ent/2)-(sgn(i.real)+sgn(i.imag))/2*x-(sgn(i.real)-sgn(i.imag))/2*y)%2 == 0:
      box += 'x'
    else:
      box += ' '
  print(' '.join(box))
input()
