from datetime import date
import time
# numpy interp
import numpy as npy

# Python code for Julia Fractal 
from PIL import Image, ImageDraw
#Latex
import sympy as sym

start_time = time.time()

# Setting the width and height of the image to be created 
w, h = 3840, 2160
# creating the new image in HSV mode 
bitmap = Image.new("HSV", (w, h), (0,0,0))
draw = ImageDraw.Draw(bitmap)
# Allocating the storage for the image and loading the pixel data
pix = bitmap.load() 

# Get Latex expression ready 
Z = sym.Symbol("z")
C = sym.Symbol("c")
FZ = sym.Symbol("f(z)")

# Setting up the variables according to the equation to create the fractal 
moveX, moveY, zoom = 0, 0, 1
maxIter = 360
# Diverging condition
R = 1000
# Colouring mode
mode = 6

c = complex(-0.7, 0.27015)
def f(z,c):
    try:
        num = 1
        den = 1 - npy.cos(0.1*z)**2
        f = num / den + c
    except (OverflowError, ZeroDivisionError):
        f = 100 + c
    return f

# Converting to latex
exp = sym.Eq(FZ, ( 1 ) / ( 1 - sym.cos(Z)**2 ) + C)

# Write the latex expression to file
sym.preview(exp, viewer='file', filename='latex.png')

perdone = 0
# Draw the set
for x in range(w):
    # Progress
    if((x / w)*100) > perdone:
        print( perdone, '% completed')
        if (perdone % 10 == 0):
            print('Elapsed time: ', round(time.time() - start_time), 'seconds')
        bitmap.convert("RGB").save('C:/Users/qntmn/OneDrive/Python/Fractals/Progress/CurrentProgress' + str(perdone) + '.png')
        perdone += 1
    for y in range(h):
        # Compute Julia Iteration at pixel (x,y)
        zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX 
        zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY
        z = complex(zx, zy)
        k = maxIter
        size = abs(z)
        while size < R and k > 1: 
            z = f(z,c)
            try:
                size = abs(z)
            except OverflowError:
                size = R + 1
            k -= 1
        # print(k)
        # print(z)
        
        
        i = round( npy.interp(k, [0, maxIter], [0, 255]) )
        # Test
        if(mode == 6):
            pix[x,y] = (i << 17) + (i << 11) + i*12
        # White & Blue
        if(mode == 5):
            pix[x,y] = (i << 16) + (i << 8) + i*8
        # Default
        if(mode == 4):
            pix[x,y] = (i << 21) + (i << 10) + i*8
        # Colourful
        if(mode == 3):
            pix[x,y] = (i << 15) + (i << 9) + i*8
        # Black & White
        if(mode == 2):
            pix[x,y] = (i << 17) + (i << 16) + i*4
        # Purple -> Red
        if(mode == 1):
            hue = round( (255)*(1 - abs(npy.sin((npy.pi/255)*(i)))) )
            pix[x,y] = (hue,255,255)
        
if(mode == 2):
    value = 0
else:
    value = 255
# Draw Axis after set is drawn
for x in range(0,w,100):
    zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX
    # Draw x ticks
    draw.line( ( (x,h),(x,h-10) ), fill=(0,0,value))
    # Draw x labels
    draw.text((x,h-20), str(round(zx,3)), fill=(0,0,value))
for y in range(0,h,100):
    zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY
    # Draw y ticks
    draw.line( ( (0,y),(10,y) ), fill=(0,0,value))
    # Draw y labels
    draw.text((0,y), str(round(zy,3)), fill=(0,0,value))

# Save fractal without latex
bitmap.show()
bitmap.convert("RGB").save('julia - ' + str(date.today()) + str(round(start_time)) + '.png')
# Open latex image
latim = Image.open("latex.png")
# Paste latex onto fractal
draw.text((w-400,200), str("c = " + str(c.real) + " + " + str(c.imag) + "i"), fill=(0,0,value))
draw.text((w-400,250), str("Max iterations = " + str(maxIter) + " , Runoff = " + str(R)), fill=(0,0,value))
bitmap.paste(latim, (w-400,400))
# Display the created fractal 
bitmap.convert("RGB").save('julialatex - ' + str(date.today()) + str(round(start_time)) + '.png')



print("Time to compute: ", round(time.time() - start_time))
