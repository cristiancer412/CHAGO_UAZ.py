num = int(input("Dame un número para verificar si es perfecto: "))

while num != 0:
    if num < 0:
        print(f"El {num} no es positivo")
    else:
        suma = 0
        for i in range(1, num):
            if num % i == 0:
                suma += i
        
        if suma == num:
            print(f"El {num} sí es perfecto")
        else:
            print(f"El {num} no es perfecto")
            
    num = int(input("Dame un número para verificar si es perfecto: "))

print("Fin de algoritmo")