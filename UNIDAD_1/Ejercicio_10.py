n1 = int(input("Dame el primer número entero positivo: "))
n2 = int(input("Dame el segundo número entero positivo: "))

if n1 > 0 and n2 > 0:
    suma = 0
    
    if n1 < n2:
        inicio = n1
        fin = n2
    else:
        inicio = n2
        fin = n1
        
    for i in range(inicio, fin + 1):
        if i % 2 != 0:
            suma += i
            
    print(f"La suma de los números impares entre los números que me diste es: {suma}")

else:
    print("Ambos números deben ser mayores que cero")