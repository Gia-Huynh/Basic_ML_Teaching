import numpy as np
import cv2
import math

import matplotlib.pyplot as plt
import matplotlib
plt.style.use('seaborn-whitegrid')

def calcu (xx):
    result2=w*xx*xx
    return (result2)

def loss (x1,x2):
    return (abs(x1-x2))

def true_ans (xx):
    result=3*xx*xx
    return (result)
    
w=7
learning_rate=0.00002
i=0
temp=np.linspace(0, 20, 2000)
i=0
while True:
    x=(i%10)+1
    print (w)
    plt.plot(temp, true_ans (temp), c='red')
    plt.plot(temp, calcu(temp), 'g', label='ham so')
    txt=plt.text(0.3,calcu(20)*0.9,'f(x)='+str(round(w,4))+'*x^2',fontsize=15)
    #plt.show()
    plt.savefig('fig/'+str(i)+'.png')
    txt.remove()
    w=w+learning_rate*2*x*x*(true_ans (x)-calcu(x))
    i=i+1
    if i==40: 
        break
print (w)
print (calcu(4),' ',true_ans(4))
