x0 = input("Ingrese la semilla: ")
y0 = input("Ingrese la semilla: ")
z0 = input("Ingrese la semilla: ")
r = input("Ingrese cuantas datos quiere mostrar: ")
xi = x0
yi = y0
zi = z0

for i in range(r):
    xi = (171 * xi) % 30269
    yi = (171 * yi) % 30307
    zi = (171 * zi) % 30323
    ui = ((float(xi) / 30269) + (float(yi) / 30307) + (float(zi) / 30323)) % 1
    print "x" + str(i) + "=" + str(xi)
    print "y" + str(i) + "=" + str(yi)
    print "z" + str(i) + "=" + str(zi)
    print "u" + str(i) + "=" + str(ui)
    print ""
