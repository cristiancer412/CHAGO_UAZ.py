num = int(input("Dame un número entero positivo: "))

if num > 0:
    suma = 0
    print("La suma de todos sus divisores menores o iguales a él es:")
    
    for i in range(1, num + 1):
        if num % i == 0:
            suma += i
            print(i)  
            
    print(f"Suma total = {suma}")

else:
    print("El número ingresado debe ser un entero positivo.")