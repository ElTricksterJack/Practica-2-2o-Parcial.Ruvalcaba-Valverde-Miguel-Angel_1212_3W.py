print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("----------------Punto 11-----------------")#aqui vamos de nuevo...
P1 = float(input("Allade un primer valor:"))#caputremos los valores
P2 = float(input("Allade un segundo valor:"))
if P1 == P2:#veamos si los valores son iguales
    print("La distansia es 0 porque son el mismo")#si lo son no vale y la disansia es 0
elif P1 > P2:#estos 2 elif son solo para que no salgan negativos si es que no se ingresan
    R = P1 - P2
    print(f"La distansia entre {P1} y {P2} es {R}")
elif P1 < P2:
    R = P2 - P1
    print(f"La distansia entre {P2} y {P1} es {R}")
else:#este este else marca error
    print("Error")
print("--------------------------------------")
print("Objetivo: Que saque la distancia dirigida entre dos puntos.")
print("Resultado: Se logra ver la distansia numerica entre ambos puntos.\n")
