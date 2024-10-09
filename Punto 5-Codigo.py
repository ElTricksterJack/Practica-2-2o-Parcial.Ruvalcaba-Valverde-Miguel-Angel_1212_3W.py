print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("----------------Punto 5-----------------")
print("1.Area de un círculo \n2.Volumen de un cilindro")
G = int(input("Cual elijes:"))#Primero daremos la opcion de desidir
match G:#abrimos un match
    case 1:#con los case sabremos las opciones que tendra el codigo
        print("Formula de Area de ciruclo")
        print("A=pi*R^2")
        def AC(ra):#primero hay que haser funciones segun las reglas
            A = 3.14*(ra*ra)#esta es la formua del ciruclo
            print(A)
        
        X = int(input("Allade valor de radio o R:"))#con esto se desidira cual real el valor del radio
        print("El area del circulo es",AC(X))#y con esto se muestra el resultado
    case 2:#resta es la misma pero con el vlumen del cilindro
        print("Formula de Volumen de un cilindro")
        print("A=pi*R^2*h")
        def ACI(ra,h):#se repite el mismo proseso de haser funciones, desidir y mostrarlas es algo obio y prefier ahorar tiempo.
           A = 3.14*(ra*ra)*(h)
           print(A)

        X = int(input("Allade valor de radio o R:"))
        H = int(input("Allade valor de haltura o H:"))
        print("El area del circulo es",ACI(X,H))
    case _:#opcion de error
        print("Error")

print("--------------------------------------")
print("Objetivo:Calcular el área de un círculo  y el volumen otra que calcule el volumen de un cilindro y utilice  primera función.")
print("Resultado: Se lograron ver los resultados que elegiste.\n")
