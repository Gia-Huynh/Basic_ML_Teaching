import numpy as np
import cv2
import math

import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D, art3d
from matplotlib import cm
from matplotlib.patches import Circle
from matplotlib.ticker import LinearLocator, FormatStrFormatter
#plt.style.use('seaborn-whitegrid')

def calcu (xx):
    result=w1*xx+w2*math.sin(xx)
    return (result)

def loss (x1,x2):
    return (abs(x1-x2))

def true_ans (xx):
    result=2*xx+2*math.sin(xx)
    return (result)
def grad_loss (xx,yy):
    result=0
    for i in nigger:
        result=result+(true_ans(i)-xx*i-yy*math.sin(i))**2
    result=math.sqrt(result)
    return (result)   
w1=4
w2=5
learning_rate=0.025
i=0
#Plot gradient
nigger = np.linspace(0,10,11) 
temp1 = np.linspace(0, 8, 130)
temp2 = np.linspace(0, 8, 130)
xx, yy = np.meshgrid(temp1, temp2)
zz=np.copy(xx)
print ('ghey')
for ii in range(0, len(temp1)):
    for jj in range(0, len(temp2)):
        zz[jj,ii]= grad_loss(temp1[ii], temp2[jj])
print ('ghey')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx,yy,zz, cmap=cm.coolwarm,linewidth=0,antialiased=True)
ax.set_xlim(0,8)
ax.set_ylim(0,8)
ax.set_zlim(0,120)
ax.view_init(elev=60, azim=-91)
print (w1,w2,grad_loss(w1,w2))
#current=ax.scatter(w1,w2,grad_loss(w1,w2)+5,s=50, c='green')
#plt.show()
#current.remove()
while True:
    current=ax.scatter(w1,w2,grad_loss(w1,w2),s=50, c='green')
    #plt.show()
    x=(i%10)+1
    Y= true_ans (x)
    print (w1,' ',w2)
    w1=w1+learning_rate*2*x*(Y-calcu(x))
    w2=w2+learning_rate*2*math.sin(x)*(Y-calcu(x))
    i=i+1
    plt.savefig('Mul_Fig/'+str(i)+'.png', dpi=300)
    current.remove()
    if i==150:
        break
print (w1,' ',w2)
print (calcu(4),' ',true_ans(4))
