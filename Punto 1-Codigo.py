print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("----------------Punto 1-----------------")
#primero definimos la funsion a usar
def HB():#Hola Bro
    print("Hola Bro!!! como te trata la vida?")
    print("\n")#esto es el codigo de la funsion
c = 1#ahora hay que haser una variable.
while c > 0:#con este while se podra repetir el saludo, cada vez que se le pida
    a = str(input('Quieres aludar a tu amigo si o no: '))#con este input solo asepta strings
    if a==("si") or a==("Si") or a==("SI") or a==("sI") or a==("SI?") or a==("si?") or a==("Si?") or a==("sI?") or a==("yes") or a==("Yes") or a==("YEs")or a==("YES")or a==("yeS")or a==("yES")or a==("yes?")or a==("okey") or a==("") or a==(" "):
        HB()#al aseptar algunas de estas opsiones se saluda, pero tambien ise una trapa ya que vale poner un espasio o usar el espasio
    else:#este es el descarte para cerrar
        print("Okey adios")
        c = 0
print("--------------------------------------")
print("Objetivo:Funcion que muestre el saludo Hey amigos! cada vez que se le pida.")
print("Resultado:puedes salurdar a tu amigo cuants veses quieras. \n")
#me siento como dora la exploradora =(
