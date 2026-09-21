n = int(input("Número de términos? "))

while n <= 0:
    print("Error, el número debe ser mayor que cero")
    n = int(input("Número de términos? "))

producto = 1.0

for i in range(1, n + 1):
    if i % 2 != 0:
        producto *= (i + 1) / i
    else:
        producto *= i / (i + 1)

valorPi = 2.0 * producto
print(f"Valor aproximado de pi = {valorPi:.4f}")