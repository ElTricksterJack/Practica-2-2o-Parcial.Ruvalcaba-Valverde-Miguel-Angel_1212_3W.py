print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("----------------Punto 3-----------------")
import math#Traemos la carpeta math
print("Bamos a sacar la facotiral de un numero entero")
N = int(input("Allade un numero entero:"))#capturamos el valor
if N < 1:#Abrimos un if con una variable que si el numero es inferior de 1 marca error
    print("Error el numero es 0 o 1:")
else:#Este es el descarte
    print(f"El factorial de {N} es")#Primero se dise cual es el valor a factorisar
    F = math.factorial(N)#con esto se declara que F es la factorial de N trallendo una funsion de la carpeta math
    print(F)#Con esto se ve el resultado.
#AAAAAA me duele explicarlo.
print("--------------------------------------")
print("Objetivo: Dar un entero positivo y resuelva su factorial.")
print("Resultado: se bio el factorial del numero si se sigieron los pasos previos\n")
