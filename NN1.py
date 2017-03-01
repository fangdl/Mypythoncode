import random
import math

def rand(a, b):
    return (b - a) * random.random() + a

def make_matrix(m, n, fill=0.0):
    mat = []
    for i in range(m):
        mat.append([fill]*n)
    return mat

#print rand(10, 20)
#print make_matrix(4,5)

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

def sigmod_derivate(x):
    return x * (1 - x)

#print sigmoid(10)
#print sigmod_derivate(sigmoid(10))



