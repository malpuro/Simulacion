x0=input("Ingrese la semilla: ");
r=input("Ingrese cuantas datos quiere mostrar: ");
l=len(str(x0));
x=1;
x0=x0*x0;


while x<r+1:
    x0=str(x0);
    #print x0;
    if len(x0)%2==0 and len(x0)==(2*l):
        x1=x0[((2*l)/4):((2*3*l)/4)];
        print "X"+str(x)+"="+x1;
        print "U"+str(x)+"=0."+x1;
        print "";
        x=x+1;
        x1=int(x1);
        x0=x1*x1;
    else:
        aux="";
        for i in range((2*l)-len(str(x0))):
            aux=aux+"0";
        x0=str(x0);
        x0=aux+x0;
