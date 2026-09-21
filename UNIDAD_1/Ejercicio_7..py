n = int(input("Dame un número: "))

if n > 0:
    f = 0
    print("Según la función, la serie es:")
    print(f)  
    
    for x in range(1, n + 1):
        f = 2 * f + (x ** 2)
        print(f)
else:
    print("El número debe ser un entero positivo")