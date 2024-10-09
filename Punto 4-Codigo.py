print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("----------------Punto 4-----------------")
print("El IVA normal es del 16% pero como estamos en zona froterisa nos cobran el 8% de IVA, pero me dijieron que use un 21% hasi que usaremos eso.")
#lo de ariba son las reglas vasicas o una explicasion vasica
print("1.Estofado de Ijirak 20$\n2.Calabaza de Jack 15$\n3.Filete de Wikilate't 25$")
M1 = int(input("Que quieres comer del menu:"))#Primero hay que alladir un match para 3 veses para poder simular una factura
match M1:
    case 1:
        print("Se lladiran 20$ a la cuenta")
        C = 20
    case 2:
        print("Se lladiran 15$ a la cuenta")
        C = 15
    case 3:
        print("Se lladiran 25$ a la cuenta")
        C = 25
    case _:
        print("Okey nada")
        C = 0 #este es porque no pidieron nada

print("1.Troso de pastel de Chocolate 30$\n2.Troso de pastel de Chocolate con chispas de Choclate 40$\n3.Troso de pastel de Chocolate con chispas de Choclate y jarabe de chocolate 50$")
M2 = int(input("Que quieres comer del menu de postres:"))
match M2:
    case 1:
        print("Se lladiran 30$ a la cuenta")
        P = 30
    case 2:
        print("Se lladiran 40$ a la cuenta")
        P = 40
    case 3:
        print("Se lladiran 50$ a la cuenta")
        P = 50
    case _:
        print("Okey nada")
        P = 0 #este es porque no pidieron nada

print("1.Arisona 25$\n2.Soda Cherry Boom Chocolat 18$\n3.Agua de kiwi 20$")
M3 = int(input("Que quieres del menu de vevidas:"))
match M3:
    case 1:
        print("Se lladiran 25$ a la cuenta")
        B = 25
    case 2:
        print("Se lladiran 18$ a la cuenta")
        B = 18
    case 3:
        print("Se lladiran 20$ a la cuenta")
        B = 20
    case _:
        print("Okey nada")
        B = 0 #este es porque no pidieron nada

cue = C+B+P #ahora con los valores ya definidos se suman para la cuenta
iva = (cue/100)*21 #con esto se logra saver cual es el iva
print("\nLa cuenta llega")
print("Sin IVA /-/",cue)#con esto se ve el resultado sin iva
print("IVA del 8% /-/",iva)#con esto se ve el resultado del iva
print("Total de la Factura /-/",cue+iva)#con esto se ve el resultado de la cuenta con iva
print("--------------------------------------")
print("Objetivo: Calcular total de una factura luego del IVA. primero obtener la cantidad sin IVA luego el porcentaje de IVA a aplicar, por ultimo devolver el total de la factura. ")
print("Resultado: se puedo ver el resultado de la cuenta sin iva, con iva y el iva solo.\n")
