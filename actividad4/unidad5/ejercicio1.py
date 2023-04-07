class Calculadora:
    def __init__(self):
        self.v1=float(input(" Ingrese numero a:  "))
        self.v2=float(input(" Ingrese numero b:  "))
        
    def suma(self):
        suma=self.v1+self.v2
        print("La suma de v1 y v2 es:  ", suma)
        
    def resta(self):
        resta=self.v1 - self.v2
        print("La resta de v1 y v2 es:  ", resta)
        
    def mul(self):
        mul=self.v1*self.v2
        print("La multiplicacion de v1 y v2 es:  ", mul)
        
    def div(self):
        if self.v2==0:
            print("ERROR MATH")
        else:
            div=self.vl/self.v2
            print("La division de v1 y v2 es: ", div)
            
    def pot(self):
        pot=pow(self.v1,self.v2)
        print("La potencia de v1 y v2 es:  ", pot)
        
    def imprimir(self):
        print("Los numeros son: ")
        print("Numero 1", self.v1)
        print("Numero 2", self.v2 )
Calculadora()

        