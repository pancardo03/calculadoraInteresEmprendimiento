#Programa para calcular interés simple

#Declaramos las variables para la formula (monto, tasa anual, periodo)
p=float(input("Ingresa monto: "))
i=float(input("Ingresa tasa anual: "))
r=float(input("Ingresa periodo en años: "))

#Calcular monto total
monto_total=p+(i*r)

#Imprimir monto total
print(monto_total)