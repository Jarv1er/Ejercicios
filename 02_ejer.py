# Software que permita sumar y restar (ambas opciones por ejecución) números enteros.

n1 = int(input("Ingresa el primer numero: "))

n2 = int(input("Ingresa el segundo numero: "))

op = input("¿Que operacion quieres realizar sumar o restar?: ")

if op == "sumar":
    print(n1 + n2)

elif op == "restar":
    print(n1 - n2)