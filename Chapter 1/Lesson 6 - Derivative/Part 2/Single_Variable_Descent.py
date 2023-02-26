import numpy as np
import cv2
import math

def calcu (xx):
    result2=w*xx*xx
    return (result2)

def true_ans (xx):
    result=3*xx*xx
    return (result)
    
w=-7
learning_rate=0.0001
i=0
while True:
    x=(i%10)+1
    print (w)
    w=w+learning_rate*2*x*x*(true_ans (x)-calcu(x))
    i=i+1
    if i==15:
        break
print (w)
print (calcu(4),' ',true_ans(4))
