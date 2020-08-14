from math import *
def cAdd(a,b):
    return [a[0] + b[0], a[1] + b[1]]


def cMult(a,b):
    return [a[0] * b[0] - a[1]*b[1] , a[0]*b[1] + a[1]*b[0]] 

def cMag(a):
    return sqrt(a[0]**2 + a[1]**2)



u = [3,4]
c = [0,1]
print(cMag(u))
