import matplotlib.pyplot as plt
import matplotlib
plt.style.use('seaborn-whitegrid')
import numpy as np

def hamso (x):
    temp=3*(x**2)+3*x
    return (temp)
def daoham (x):
    #2x+3
    temp=(hamso(x)-hamso(x+0.0000000001))/(-0.0000000001)
    return (temp)
def tieptuyen (x,y):
    plt.text(0.3,250, 'X='+str(round(y,1))+'  Y='+str(round(hamso(y),2)), fontsize=13)
    plt.text(0.3,275, 'tiep tuyen: '+str(int(daoham (y)))+'x-'+str(int((daoham (y)*y-hamso(y)))), fontsize=13)
    return (daoham (y)*x-(daoham (y)*y-hamso(y)))
    #return (daoham (y)*x)

def nigger (x):
    return (x-x)
#201
for j in np.linspace(-10,10,201):
    i=round(j,1)
    #fig = plt.figure()
    ax = plt.axes()
    ax.set_xlim(-13,13)
    ax.set_ylim(-50,300)
    plt.xticks(np.arange(-13, 13, 1.0))
    x = np.linspace(-13, 13, 1500)
    Oy = np.linspace (-50, 250, 2)

    plt.axhline(linewidth=2, color='k') #adds thick line @ y=0
    plt.axvline(linewidth=2, color='k') #adds thick line @ x=0

    #ax.plot(nigger(Oy),Oy,'k')
    #ax.plot(x,nigger(x),'k')
    plt.scatter(i, hamso(i), s=50, c='red')
    ax.plot(x, hamso(x), 'g', label='ham so')
    ax.plot(x, daoham(x), 'r', label='dao ham', linewidth=0.5)
    ax.plot(x, tieptuyen(x,i), 'b', label='tiep tuyen')
    plt.savefig('all_imagesv3/'+str(round(i+10,1))+'.png')
    plt.clf()

print (daoham(2))
