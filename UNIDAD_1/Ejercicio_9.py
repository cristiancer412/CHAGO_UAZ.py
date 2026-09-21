x = float(input("Teclee argumento x? "))

while x <= -1 or x > 1:
    print("Error, valor de x inválido")
    x = float(input("Teclee argumento x? "))

n = int(input("Hasta cuantos términos de la serie? "))

suma_terminos = 0.0

for i in range(1, n + 1):
    termino = ((-1) ** (i - 1) * (x ** i)) / i
    suma_terminos += termino

print(f"ln(1+x) = {suma_terminos:.6f}")