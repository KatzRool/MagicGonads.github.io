plan = """
The main script (mandelbrot.pde) allows you to browse through different values, then press space to save that snapshot along with relevant information about it, so you can insert that info into image.pde in the image folder, then in the image folder you can set the resolution multipler, and generate higher resolution images that dont display in the window, but rather it runs once and then saves to a local folder.

You can set the complex transpose for both z and c, so for z it means a gradient between a Tricorn fractal and a Mandelbrot fractal, and for c it means a gradient between an updside down julia set and a regular julia set.

The newer, now lost, version allowed you to merge between julia and mandelbrot modes, it was really cool.
How I did it was I added a constant value to every pixel and then calculated using the mandelbrot method, so I'll be re-adding that soon.

Also I had added a 'ghost' feature that allowed you to see the n previous calulations for the main script, I wasn't able to introduce any transparency on the image script however, any ideas? I need to be able to give a PImage transparency and then add another PImage (with transparency) on top of the previous one, then save that image.﻿

Changing rendering to a trace of the argument and magnitude of the final z at each iteration.
Low magnitudes appear dark and high magnitudes are continuously brighter.
"""

#http://paulbourke.net/fractals/juliaset/
#http://pillow.readthedocs.io/en/latest/

from math import *

def colour(h=1,s=1,v=1):
    import colorsys
    c = '#'
    h,s,v = (h,0)[h==float('NaN')],(s,1)[s==float('NaN')],(v,255)[v==float('NaN')]    
    for i in colorsys.hsv_to_rgb(h,s,v):
        c+= '0'*(i<16)+hex(max(min(int(i),255),0)).replace('0x','')
    return c

def iterate(_exe,_col,_arg):
    global tra,jug,con,k,n,m,mit,mag,off,res,pix,mag
    f = lambda z=complex(0,0),c=complex(0,0): eval(_exe)
    pix = [0]*w*h
    sca = 2/mag
    inc = 2*sca/(min(w,h))
    x = -sca*max(w,h)/min(w,h)+off[0]
    y = -sca+off[1]
    for i in range(w):
        for j in range(h):
            z = con
            c = complex(x*jug[0],y*jug[1])
            z,c = (z,c)[jul],(c,z)[jul]
            its = 0
            while its<mit:
                try:
                    z = complex(z.real*tra[0],z.imag*tra[1])
                    z = f(z,c)
                    if abs(z)>out:
                        break
                except OverflowError:
                    its = mit
                    break
                its+=1
            pix[i+j*w] = (eval(_col),eval(_arg))
            if not trc and its==mit:
                pix[i+j*w] = (0,0)
            y+= inc
        x+= inc
        y = -sca+off[1]

def arg(z):
    return atan2(z.imag,z.real)

def save():
    from PIL import Image,ImageColor
    global pix
    pix = [0]*w*h
    iterate(compile(exe,"<string>","eval"),compile(col,"<string>","eval"),compile(ang,"<string>","eval"))
    Im = Image.new('RGB',[w,h])
    p = 0
    for _p in pix:
        if _p !=(0,0):
            y = p//w
            x = p%w
            #2-min(1,_p[0]),min(1,_p[0])*255)
            Im.putpixel([x,y],ImageColor.getrgb(colour(abs(pi+_p[1])/(2*pi),1,_p[0]*255)))
        p+=1
    Im.save(name+'.png','PNG')
h = 450
w = 800
trc = False
jul = False
tra = (1,1)
con = complex(0,0)
jug = (1,1)
mit = 500
out = 4
exe = 'z**2+c'
col = '(its/mit+(its==0))**0.5'#'abs(z)/5'
ang = '0.5'#'arg(z)'
mag = 1
off = (0,0)

name = str(con).replace('j','i').replace('(','').replace(')','')+' '+('Mandelbrot','Julia')[jul]+' '+('Set','Trace')[trc]+' f(z) = '+exe+' while abs(z) ≤ '+str(out)+' by v('+col+') h('+ang+')'+' @ '+str(mit)+' iters '+str(mag)+'x offset '+str(off)+str(tra)+str(jug)
name = name.replace('/','÷').replace('**','^').replace('*','×').replace('its','ί').replace('mit','μ')
save()
