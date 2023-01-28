valor=(__name__ =="__main__")

def suma (n:int):
    if n>0:
        n= n + suma(n-1)
    return n

def div (a:int,b:int):
    n=a/b
    return n

##MENU
if __name__ =="__main__":
    while True:
        opc=str(input("""--------------------------------------
Elija el ejercício que desee iniciar.
2) Ejercicio 2.
3) Ejercicio 3.
4) Ejercicio 4.
5) Ejercicio 5.
6) Ejercicio 6.
7) Ejercicio 7.
0) Salir.
---------------------------------------
"""))
        if opc == "2":
            import Ejercicio_2
        elif opc == "3":
            import Ejercicio_3
        elif opc == "4":
            import Ejercicio_4
        elif opc == "5":
            import Ejercicio_5
        elif opc == "6":
            import Ejercicio_6
        elif opc == "7":
            import Ejercicio_7
        elif opc == "0":
            break
        else:
            print ("ERROR.Esa opción no es valida.")