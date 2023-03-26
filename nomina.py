#s_b: salario base
#he: cantidad de horas extras
#b: bonificacion 1 si hay o 0 si no

#se ingresan los datos 
s_b,he,b=input().split()
s_b=float(s_b)
he=int(he)
b=int(b)

#se hacen las operaciones 
vh=s_b/192 #valor hora 
vhe=((vh*1.25)*he)#valor hora extra 
Bon=(s_b*0.05)*b# la bonificacion 
s_t=s_b+vhe+Bon
devengado=(s_t*0.035)+(s_t*0.04)+(s_t*0.01)
salario=s_t-devengado
print(round(salario,1))
