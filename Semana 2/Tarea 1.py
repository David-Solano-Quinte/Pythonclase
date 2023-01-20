## David Josue Solano Quinte

opcion = int(1)
while opcion != 4:
    opcion = int(input("""Escriba la opción a realizar:
1) Dibujar un cuadrado con *´s.
2) Mostrar una lista de numeros indicando los multiplos de 2.
3) Iterar una lista de nombres y edades imprimiendo los que son mayores de edad.
4) Terminar el programa.
"""))
    if opcion!=4:
        if opcion==3 :
            a=int(0)
            lista= []
            while True:
                
                nombre= input("""Ingrese el nombre:   (para finalizar la recopilación de datos escriba "0")
""")
                if nombre=="0":
                    break
                edad = int(input(f"""Ingrese la edad de {nombre}:
"""))
                if edad>=18:
                    listtemp=[nombre, edad]
                    lista.append(listtemp)
            print(f"Los mayores de edad son: {lista}")
        elif opcion==2 :
            a= int(input ("""Ingrese el rango:
Desde: """))
            b =int(input("Hasta: "))
            print(" ")
            for x in range(a,b+1,1):
                if x%2==0:
                    print(f"{x} es multiplo de 2.")
                else:
                    print(f"{x} no es multiplo de 2.")
            print(" ")
        elif opcion==1 :
            a=int(input("Ingrese el valor del lado del cuadrado: "))
            for x in range(1,a+1) :
                if x==1 or x==a:
                    print("* "*(a))
                else :
                    print("*"+" "*(a*2-3)+"*")

        else:
            print ("Esa opcion no es valida.")