from datetime import date
import time
# Math Libraries
import cmath
from cxroots import Circle

# Python code for Julia Fractal 
from PIL import Image, ImageDraw
#Latex
import sympy as sym

start_time = time.time()

# Setting the width and height of the image to be created 
w, h = 1920, 1080
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
maxIter = 100
# Diverging condition
R = 1000
# Colouring mode
mode = 2

c = complex(0,0)
# Defining the function
def f(z):
    num = z**3 - 2*z**2 + 0.5*z + 1
    den = 1
    return num / den

#function = lambda z: func(z)

# Symbolic equation
F = ( Z**3 - 2*Z**2 + 0.5*Z + 1 ) / ( 1 )

# Taking the derivative
FP = sym.diff( F,Z )
def fp(z):
    return complex(FP.evalf(subs={Z: z, C: c}))
print(FP)
#print(complex(FP.evalf(subs={Z: 4+1j, C: 1})))

# Finding the roots
roots = []
cont = Circle(0,3)
zeroes = cont.roots(f)
zeroes.show()
print(zeroes)
numroots = len(zeroes[0])
for j in range(numroots):
    roots.append(complex(zeroes[0][j].real, zeroes[0][j].imag))
print(roots)
    
# Assign hues for each root
colours = [(90,190,155), (0,190,155), (150,255,255), (90,190,155), (90,190,155), (90,190,155)]

# Converting to latex
# Write the latex expression to file
exp = sym.Eq(FZ, F)
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
        #print(y)
        # Compute Julia Iteration at pixel (x,y)
        zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX 
        zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY
        z = complex(zx, zy)
        k = maxIter
        tol = 0.00001
        while k > 1: 
            z = z - f(z) / fp(z)
            for j in range(numroots):
                diff = z - roots[j]
                if( abs(diff.real) < tol and abs(diff.imag) < tol):
                    pix[x,y] = colours[j]
            k -= 1
        

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
