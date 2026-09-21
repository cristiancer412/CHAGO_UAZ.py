monto = float(input("Monto total de la compra $: "))

if monto < 500:
    descuento = 0
elif monto < 1000:
    descuento = 0.05
elif monto < 7000:
    descuento = 0.10
elif monto < 15000:
    descuento = 0.15
else:
    descuento = 0.25

totalPagar = monto - (monto * descuento)

print(f"El total a pagar incluyendo el descuento es $: {totalPagar:.2f}")