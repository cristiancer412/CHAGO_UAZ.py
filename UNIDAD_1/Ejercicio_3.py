largo = float(input("Ingresa largo del terreno: "))
ancho = float(input("Ingresa ancho del terreno: "))
precio = float(input("Ingresa precio por metro cuadrado de terreno $: "))

area = largo * ancho
precio_subtotal = area * precio

if area > 1000:
    total = precio_subtotal * 0.75
elif area > 500:
    total = precio_subtotal * 0.83
else:
    total = precio_subtotal



print("Precio del terreno es: $", total)