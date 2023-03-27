repetir="S"
count=0
d={}
while repetir=="S" or repetir=="s":
    l=[]
    Nom=input("Ingrese el nombre: ")
    l.append(Nom)
    edad=int(input("Ingrese la edad: "))
    l.append(edad)
    dir=input("Ingrese la direccion: ")
    l.append(dir)
    tel=int(input("Ingrese el telefono: "))
    l.append(tel)
    Sexo=input("Ingrese Sexo: ")
    l.append(Sexo)
    d[count]=l
    count+=1
    repetir=input("¿Desea continuar S/N?")
    
print(d)


