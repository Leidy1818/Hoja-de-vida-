repetir="S"
while repetir=="S" or repetir=="s":
    print("Ingrese la temperatura en grados Celcius")
    C=float(input("Temperatura: "))
    print("Precione 1 si desea Grados Fahrenheit")
    print("Precione 2 si desea Grados Rankine")
    print("Precione 3 si desea Grados Kelvin")
    num=int(input("ingresa la opcion: "))
    if num ==1:
        F=(C*9/5)+32
        print(C,"Grados Celcius", "es equivalente a", F, "Grados Fahrenheit ")
    elif num ==2:
        Ra=(C*9/5)+491.67
        print(C,"Grados Celcius", "es equivalente a", Ra, "Grados Rankine ")
    elif num==3:
        K=C+273.15
        print(C,"Grados Celcius", "es equivalente a", K, "Grados Kelvin ")
    else:
        print("Ingrese opcion valida")
    repetir=input("¿Desea continuar S/N?")



F=(C*9/5)+32
K=C+273.15
Ra=(C*9/5)+491.67