x0=input("Ingrese la semilla: ");
a=input("Ingrese el multiplicador: ");
b=input("Ingrese la constante aditiva: ");
m=input("Ingrese el modulo: ");
r=input("Ingrese cuantas datos quiere mostrar: ");
x=0;
while x<r:
    x0=((a*x0)+b)%m;
    x=x+1;
    print "X"+str(x)+"="+x0;
    print "U"+str(x)+"="+str(float(x0)/m);
