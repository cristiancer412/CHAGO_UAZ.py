n1 = float(input("Dame el número n1: "))
n2 = float(input("Dame el número n2: "))
n3 = float(input("Dame el número n3: "))

if n1 > 0 and n2 > 0 and n3 > 0:
    
    suma1 = int(n1) + int((n1 - int(n1)) * 10000 + 0.5)
    suma2 = int(n2) + int((n2 - int(n2)) * 10000 + 0.5)
    suma3 = int(n3) + int((n3 - int(n3)) * 10000 + 0.5)
    
    if suma1 >= suma2 and suma1 >= suma3:
        mayor = suma1
    elif suma2 >= suma3:
        mayor = suma2
    else:
        mayor = suma3
        
    print(f"La suma resultante de n1 = {suma1:.4f}")
    print(f"La suma resultante de n2 = {suma2:.4f}")
    print(f"La suma resultante de n3 = {suma3:.4f}")
    print(f"El valor mayor de las sumas es {mayor:.4f}")

else:
    print("Alguno o varios de los números no son positivos")