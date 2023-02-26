import numpy as np
import cv2
import math

def calcu (xx):
    result=w1*xx+w2*math.sin(xx)
    return (result)

def loss (x1,x2):
    return (abs(x1-x2))

def true_ans (xx):
    result=2*xx+2*math.sin(xx)
    return (result)
    
#2x+2sin(x)
true=2*4+2*math.sin(4)
#4x+3sin(x)
w1=4
w2=-3
learning_rate=0.02
i=0
while True:
    x=(i%10)+1
    Y= true_ans (x)
    print (w1,' ',w2)
    w1=w1+learning_rate*2*x*(Y-calcu(x))
    w2=w2+learning_rate*2*math.sin(x)*(Y-calcu(x))
    i=i+1
    if i==500:
        break
print (w1,' ',w2)
print (calcu(4),' ',true_ans(4))
