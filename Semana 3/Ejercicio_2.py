##SPLIT
def split(texto:str):
    print (texto.split(sep=" "))

##JOIN
def join(texto:str):
    a=texto.split()
    texto="".join(a)
    print(texto)

##COUNT == len()
def count(texto:str):
    print("El texto tiene en total:")
    for a in range(1,len(texto)):
        if a!=len(texto):
            print (f"{a}...")
        else:
            print(f"{a} carácteres.")

##FIND
def find (char:str,texto:str):
    a=texto.find(char)
    if a != -1:
        print (f"Se encuentre en la posición: {texto.find(char)+1}")
    else :
        print("No se encontró este carácter.")
    
##UPPERCASE
def uppercase (texto:str):
    print (texto.upper())

##LOWERCASE
def lowercase (texto:str):
    print (texto.lower())


while True:
    ##MENU
    opcion=str(input ("""-----------------------------------------------
Eliga una opción a realizar:
a) Split
b) Join
C) Count
d) Find
e) Uppercase
f) Lowercase
g) Finalizar
-----------------------------------------------"""))

    texto=str("Lorem Ipsum")
    if opcion.lower()=="a":
        split(texto)
    elif opcion.lower() =="b":
        join (texto)
    elif opcion.lower() =="c":
        count(texto)
    elif opcion.lower() =="d":
        caracter=str(input("Ingrese el caracter a buscar:"))
        find (caracter,texto)
    elif opcion.lower() =="e":
        uppercase(texto)
    elif opcion.lower() =="f":
        lowercase(texto)
    elif opcion.lower()=="g":
        break
    else:
        print ("Esa opción no es válida.")