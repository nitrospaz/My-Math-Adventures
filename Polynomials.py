print('Use "quad(a,b,c)" for quadratic equations.')
print('Use "equation(a,b,c,d)" for first order polynomials.')
from math import sqrt

def quad(a,b,c):
    # a*x**2 + b*x + c = 0 format
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return x1, x2

def plug():
    x = -100 #start at -100
    while x < 100: # go up to +100
        if 2*x+5 == 13: #if it makes the eq true
            print("x =",x) # print it out
        x += 1 # otherwise make x go up by 1 to test the next number

def equation(a,b,c,d):
    return (d-b)/(a-c)
# using return gives a number we can assign
#to a variable and use again
# ax+b=cx+d format
