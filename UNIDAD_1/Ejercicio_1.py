import math

H = float(input("Ingrese la altura: "))
W = float(input("Ingrese el ancho: "))

X = H / W

S = 2 * W * (math.sqrt(X**2 + 1/16) + (1/(16*X)) * (math.log(X + math.sqrt(X**2 + 1/16)) + math.log(4)))

print("La longitud de arco de la parábola es:", round(S, 4))