costo = float(input("Dame el costo del artículo deportivo: "))
pago = float(input("Dame el pago del cliente: "))

if pago >= costo:
    cambio = pago - costo
    print(f"El cambio es: {cambio}")
else:
    print("Con esa cantidad no se alcanza a pagar")