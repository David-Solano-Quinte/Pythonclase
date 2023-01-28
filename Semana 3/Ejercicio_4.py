class CATALOGO:
    def __init__ (self,cuerpo:list):
        self.cuerpo=cuerpo

    def agregar (self,lista:list,producto:str):
        self.cuerpo = lista.append(producto)

class PRODUCTO:
    def __init__ (self,nombre:str):
        self.nombre = nombre
producto_a = PRODUCTO ("Llanta")
producto_b = PRODUCTO ("Timón")
producto_c = PRODUCTO ("Faro")
producto_d = PRODUCTO ("Puerta")
lista=[producto_a.nombre,producto_b.nombre,producto_c.nombre,producto_d.nombre]
catalogo = CATALOGO (lista)

while True:
    opc=input("""-----------------------------
Ingrese la opción a realizar:
a) Revisar el catálogo.
b) Agregar productos al catálogo.
c) Finalizar.
-----------------------------
""")
    opcion=opc.lower()
    if opcion=="a":
        print(lista)

    elif opcion=="b":
        prd=str(input("Ingrese el nombre del producto a ingresar: "))
        lista=catalogo.cuerpo
        catalogo.agregar(lista,prd)
        catalogo.cuerpo=lista
    elif opcion=="c":
        break
    else:
        print ("ERROR. La opción ingresada no es valida, porfavor vuelva a ingresar una opción.")