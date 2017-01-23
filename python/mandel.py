plan = """
The main script (mandelbrot.pde) allows you to browse through different values, then press space to save that snapshot along with relevant information about it, so you can insert that info into image.pde in the image folder, then in the image folder you can set the resolution multipler, and generate higher resolution images that dont display in the window, but rather it runs once and then saves to a local folder.

You can set the complex transpose for both z and c, so for z it means a gradient between a Tricorn fractal and a Mandelbrot fractal, and for c it means a gradient between an updside down julia set and a regular julia set.

The newer, now lost, version allowed you to merge between julia and mandelbrot modes, it was really cool.
How I did it was I added a constant value to every pixel and then calculated using the mandelbrot method, so I'll be re-adding that soon.

Also I had added a 'ghost' feature that allowed you to see the n previous calulations for the main script, I wasn't able to introduce any transparency on the image script however, any ideas? I need to be able to give a PImage transparency and then add another PImage (with transparency) on top of the previous one, then save that image.﻿
"""

#http://paulbourke.net/fractals/juliaset/
#http://pillow.readthedocs.io/en/latest/

from math import *

def colour(h=1,s=1,v=1):
    import colorsys
    c = '#'
    for i in colorsys.hls_to_rgb(h,s,v):
        c+= '0'*(i<16)+hex(min(int(i),255)).replace('0x','')
    return c

def iterate():
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
            its = 0
            while its<mit:
                try:
                    z = complex(z.real*tra[0],z.imag*tra[1])
                    z = f((z,c)[jul],(c,z)[jul])
                    if abs(z)>out:
                        break
                except OverflowError:
                    its = mit
                    break
                its+=1
            if its==mit:
                pix[i+j*w] = 0
            else:
                t = eval(_col)
                pix[i+j*w] = 1/(t+(t==0))-(t==0)
            y+= inc
        x+= inc
        y = -sca+off[1]
def reloc():
    global mag,off,mag
    off[0]+= (mouseX-w/2)/(w*mag)
    off[1]+= (mouseY-h/2)/(h*mag)

def save():
    from PIL import Image,ImageColor
    global pix,_exe,_col
    pix = [0]*w*h
    _exe = compile(exe,"<string>","eval")
    _col = compile(col,"<string>","eval")
    iterate()
    Im = Image.new('RGB',[w,h])
    p = 0
    for _p in pix:
        if _p !=0:
            y = p//w
            x = p%w
            c = (_p,1-_p,255*_p)
            Im.putpixel([x,y],ImageColor.getrgb(colour(hue/100,255-_p*255,_p)))
        p+=1
    Im.save(name+'.png','PNG')
hue = 50
h = 450
w = 800
jul = False
tra = (1,1)
con = complex(0,0)
jug = (1,1)
mit = 50
out = 4
exe = 'z**2+c'
col = '(1+its/mit)**(1/2)'
mag = 1
off = (0,0)

name = str(con).replace('j','i').replace('(','').replace(')','')+' '+('Mandelbrot','Julia')[jul]+' Set f(z) = '+exe+' while abs(z) ≤ '+str(out)+' by '+col+' @ '+str(mit)+' iters '+str(mag)+'x offset '+str(off)+str(tra)+str(jug)
name = name.replace('/','÷').replace('**','^').replace('*','×').replace('its','ι').replace('mit','μ')
save()
