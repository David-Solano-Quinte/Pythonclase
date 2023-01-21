## David Josue Solano Quinte

#DICCIONARIO
biblioteca={"libro1" : ["autor1","categoría1","disponible"],"libro2":["autor2","categoría2","prestado"],
"libro3":["autor1","categoría3","prestado"],"libro4":["autor3","categoría4","disponible"],"libro5":["autor1","categoría2","prestado"],
"libro6":["autor2","categoría4","disponible"],"libro7":["autor4","categoría2","disponible"],"libro8":["autor1","categoría4","prestado"]}

#CUERPO DEL MENU
opcion=int(1)
print("Bienvenido al menu de la biblioteca.")
while True:
#MENU
    opcion=input("""Eliga la opción que desea realizar:

1) Obtener una lista sobre las categorías de los libros.
2) Obtener nombre de los libros y autores.
3) Cambiar el estado de un libro.
4) Ver la lista de usuarios de la biblioteca.
0) Terminar programa.
""")
    if opcion=="1":
        #CUERPO DE LA OPCION 1:
        while opcion!="0":
            opcion=input("""Porfavor, eliga la categoría de libros que desea observar:

1) Categoría 1
2) Categoría 2
3) Categoría 3
4) Categoría 4
0) Regresar al menu principal.
""")
            if opcion=="1":
                for key,val in biblioteca.items():
                    key=f"{key}"
                    val = "categoría1"
                    listatemp=[biblioteca[key][1]]
                    if val in listatemp:
                        print (f"{key}, {val}")

            elif opcion =="2":
                for key,val in biblioteca.items():
                    key=f"{key}"
                    val = "categoría2"
                    listatemp=[biblioteca[key][1]]
                    if val in listatemp:
                        print (f"{key}, {val}")
            elif opcion=="3":
                for key,val in biblioteca.items():
                    key=f"{key}"
                    val = "categoría3"
                    listatemp=[biblioteca[key][1]]
                    if val in listatemp:
                        print (f"{key}, {val}")
            elif opcion=="4":
                for key,val in biblioteca.items():
                    key=f"{key}"
                    val = "categoría4"
                    listatemp=[biblioteca[key][1]]
                    if val in listatemp:
                        print (f"{key}, {val}")
            elif opcion!="0":
                print("ERROR. Esa opción no es válida, porfavor ingrese de nuevo una opción.")
    elif opcion=="2":
        #CUERPO DE LA OPCION 2:
        while opcion !="0":
            opcion = input("""Porfavor, eliga la categoría de libros que desea observar:

1) Autor 1
2) Autor 2
3) Autor 3
4) Autor 4
0) Regresar al menu principal.
""")
            if opcion=="1":
                for key,val in biblioteca.items():
                    key=f"{key}"
                    val = "autor1"
                    listatemp=[biblioteca[key][0]]
                    if val in listatemp:
                        print (f"{key}, {val}")

            elif opcion =="2":
                for key,val in biblioteca.items():
                    key=f"{key}"
                    val = "autor2"
                    listatemp=[biblioteca[key][0]]
                    if val in listatemp:
                        print (f"{key}, {val}")
            elif opcion=="3":
                for key,val in biblioteca.items():
                    key=f"{key}"
                    val = "autor3"
                    listatemp=[biblioteca[key][0]]
                    if val in listatemp:
                        print (f"{key}, {val}")
            elif opcion=="4":
                for key,val in biblioteca.items():
                    key=f"{key}"
                    val = "autor4"
                    listatemp=[biblioteca[key][0]]
                    if val in listatemp:
                        print (f"{key}, {val}")
            elif opcion!="0":
                print("ERROR. Esa opción no es válida, porfavor ingrese de nuevo una opción.")
    elif opcion=="3":
        while opcion!=0:
            a=int(1)
            for key,val in biblioteca.items():
                val=biblioteca[key][2]
                print (f"{a}){key}, {val}")
                a+=1
            print ("0) Volver al menu principal.")
            opcion= input(f"Ingrese la opcion de la que desea cambiar su disponibilidad: ")
            if opcion.isnumeric() and int(opcion)<a:
                if opcion =="0":
                    break
                state=biblioteca[f"libro{opcion}"][2]
                if state == "disponible":
                    state="prestado"
                else:
                    state="disponible"
                biblioteca[f"libro{opcion}"][2]=state
            else:
                print("ERROR. El dato ingresado no es válido, porfavor ingrese una opción válida.")
    elif opcion=="4":
        lista_usuarios=["Jorge", "Miguel", "María", "Pepe", "Henry", "Manuel", "Roxane"]
        for nombre in lista_usuarios:
            print (nombre)
    elif opcion!="5":
        print("ERROR. Esa opción no es válida, porfavor ingrese de nuevo una opción.")
        