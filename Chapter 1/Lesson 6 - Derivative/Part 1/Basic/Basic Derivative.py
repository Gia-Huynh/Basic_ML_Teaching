import matplotlib.pyplot as plt
import matplotlib
plt.style.use('seaborn-whitegrid')
import numpy as np

def hamso (x):
    temp=3*(x**2)+3*x
    return (temp)
def daoham (x):
    #6x+3
    temp=(hamso(x)-hamso(x+0.0000000001))/(-0.0000000001)
    return (temp)
def tieptuyen (x,y):
    #plt.text(0.3,250, 'X='+str(round(y,1))+'  Y='+str(round(hamso(y),2)), fontsize=13)
    #plt.text(0.3,275, 'tiep tuyen: '+str(int(daoham (y)))+'x-'+str(int((daoham (y)*y-hamso(y)))), fontsize=13)
    return (daoham (y)*x-(daoham (y)*y-hamso(y)))
    #return (daoham (y)*x)

def daoham_coban (x,xo):
    global a
    global b
    a=(hamso(x)-hamso(xo))/(x-xo)
    b=hamso(x)-a*x
    
def nigger(x):
    return (a*x+b)

a=1
b=1

for j in np.linspace(5,2.001,300):
    i=round(j,3)
    ax = plt.axes()
    ax.set_xlim(-1,8)
    ax.set_ylim(-25,100)
    plt.xticks(np.arange(-1, 8, 1.0))
    x = np.linspace(-13, 13, 1500)
    Oy = np.linspace (-50, 250, 2)

    plt.axhline(linewidth=2, color='k') #adds thick line @ y=0
    plt.axvline(linewidth=2, color='k') #adds thick line @ x=0

    plt.scatter(i, hamso(i), s=15, c='green')
    ax.plot(x, hamso(x), 'red', label='ham so')
    daoham_coban(2,i)
    ax.plot(x, nigger(x), 'b', label='tiep tuyen')
    
    plt.text(4.1,40,'X=2   X0='+str(i), fontsize=13)
    plt.text(4.1,32,'(f(2)-f(x0))/(2-x0) = '+str(round(a,4)), fontsize=13)
    plt.text(4.1,23,'True dao ham = 15', fontsize=13)
    
    
    plt.scatter(2, hamso(2), s=15, c='blue')
    ax.plot(x, tieptuyen(x,2), 'b', linestyle='-.', label='tiep tuyen true')
    plt.savefig('all_imagesv0/'+str(int(round(i,3)*1000))+'.png')
    plt.clf()

print (daoham(2))
