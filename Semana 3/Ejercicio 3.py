def mul (a:int):
    n=a*2
    print(n)

def fact (a:int):
    n=int(1)
    for x in range(1,a+1):
        n=n*x
    print(n)

while True:
    opcion=input("""------------------------------------------
Eliga la opción que desea realizar:
a) Multiplicar por 2.
b) Hallar el factorial.
c) Finalizar programa.
------------------------------------------""")
    if opcion=="a":
        num=int(input("Ingrese el valor numérico deseado:"))
        mul(num)
    elif opcion=="b":
        num=int(input("Ingrese el valor numérico deseado:"))
        fact(num)
    elif opcion=="c":
        break
    else:
        print("Esa opción no es válida, porfavor ingrese otro valor.")