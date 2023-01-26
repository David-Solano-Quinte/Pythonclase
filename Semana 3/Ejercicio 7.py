class PRODUCTO:
    def __init__(self,nombre:str,pais:str,lote:str,año:int):
        self.nombre= nombre
        self.codigo= f"{pais.upper()}-{lote}-{año}"
        self.identificacion = [f"{pais}",f"{lote}"]

    def __str__(self) -> str:
        return f"{self.nombre}: {self.codigo}"

    def identificar(self):
        print(f"País: {self.identificacion[0]} || Lote: {self.identificacion[1]}")

ejemplo=PRODUCTO("Sample_text","perú","0001",2023)

while True:
    opcion= input ("""--------------------------------------------
Ingrese la opcion a realizar: 
a) Mostrar el producto y código.
b) Mostrar país de orígen y número de lote.
c) Salir.
--------------------------------------------
""")
    if opcion.lower() == "a":
        print(PRODUCTO.__str__(ejemplo))
    elif opcion.lower() == "b":
        PRODUCTO.identificar(ejemplo)
    elif opcion.lower() == "c":
        break
    else:
        print("Esa opción no es válida.")