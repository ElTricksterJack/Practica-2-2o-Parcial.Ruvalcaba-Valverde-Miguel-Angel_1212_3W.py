print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("----------------Punto 10-----------------")
def sivo(c):#primero definamos la funsion, con todo y argumento
    c = c.lower()#esto es lo que permite ver y detectar las letras de un texto completo.
    if c in 'aeiou' or c in 'AEIOU':
        print("Es vocal")
        return True#esto le da el valor true
    else:#este es el descarte y dicho descarte le da el valor falso si la condision anterior no se cumple
        print("No es vocal o no es carapter")
        return False
vo = str(input("Allade una letra: "))
tf = sivo(vo)#con esto se demuestra el valor ture o false, y a su vez se ve el resultado de la funsion despues de capturar el numero, 2 pajaros de un tiro
print("True o Flase?:", tf)#listo solo de muestra el resultado.
#Hay lo tiene niños nos vemos la sigiente semana. o eso me gustaria desir
print("--------------------------------------")
print("Objetivo: Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.")
print("Resultado: se logro ver si es la vocal o no teneidno un valor true\n")
