# Define equation
def g(x):
    return 6*x**3 + 31*x**2 +3*x - 10

# Brute force the equation
def plug():
    x = -100
    while x < 100:
        if g(x) == 0:
            print("x =",x)
        x += 1
    print("Done.")
# There may be more answers than are found with cubic equations


# First degree equations format ax + b = cx + d
def equation(a,b,c,d):
    return (d-b)/(a-c)

# Quadratic equations format a*x**2 + b*x + c = 0
from math import sqrt

def quad(a,b,c):
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return x1,x2

# guess method for cubics
def f(x):
    return 6*x**3 + 31*x**2 + 3*x - 10

def average(a,b):
    return (a + b)/2.0

def guess():
    lower = -1
    upper = 0
    for i in range(40):
        midpt = average(lower,upper)
        if f(midpt) ==0:
            return midpt
        elif f(midpt) < 0:
            upper = midpt
        else:
            lower = midpt
    return midpt

x = guess()

print(x,f(x))
