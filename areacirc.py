import numpy as np
import matplotlib.pyplot as plt
import math

n=input("Numeros de muestras: ")
 
def randux(r):
    print "randux"
    Ux=[]
    x=0
    x0=7
    while x<r:
        x0=((5*x0)+3)%607
        x=x+1
        """print "X"+str(x)+"="+str(x0)
        print "U"+str(x)+"="+str(float(x0)/16)"""
        Ux.append(float(x0)/607)
    return Ux
 
def randuy(r):
    print "randuy"
    Uy=[]
    x=0
    x0=17
    while x<r:
        x0=((5*x0)+2)%1279
        x=x+1
        """print "X"+str(x)+"="+str(x0)
        print "U"+str(x)+"="+str(float(x0)/31)"""
        Uy.append(float(x0)/1279)
    return Uy
 
Ux=randux(n)
Uy=randuy(n)
k=6
r=5
for i in range(n):
    Ux[i]=2*k*Ux[i]-k
 
for i in range(n):
    Uy[i]=2*k*Uy[i]-k

plt.ion()
ax=plt.gca()

arear=math.pi*(r**2)
N=1
d=0;
ax.plot([0]*13,range(-6,7))
ax.plot(range(-6,7),[0]*13)

for i in range(n):
	if (Ux[i]**2+Uy[i]**2)<=(r**2):
		ax.plot(Ux[i],Uy[i],"b*")
		N=N+1
		
	else:
		ax.plot(Ux[i],Uy[i],"r*")
	if i%10==0:
		plt.draw()
	title="Area Teorica: "+str(arear)+" Area Practica: "+str(N*(float(1)/(n*(2*r)**2)))+"\n"+"Error: "+str()
	plt.title(title)
