import main as funcion
import os

print ("b")
while True:
    opcion=input("""----------------------------------------------    
Ingrese la opción a realizar:
a) Hallar la suma de los "n" primeros números.
b) dividir 2 números.
c) Salir del programa.
----------------------------------------------
""")
    if opcion.lower()=="a":
        try:
            n=int(input("""Ingrese el valor de "n": """))
            print(f"La suma de los {n} primeros numeros es: {funcion.suma(n)}")
        except:
            print("ERROR. Los datos ingresados no son números.")
        else:
            print(os.getcwd())
        finally:
            print ("Proceso terminado.")
    elif opcion.lower()=="b":
        try:
            print("Ingrese los valores de la división:")
            a=int(input())
            b=int(input())
            print (f"El resultado de la división es: {funcion.div(a,b)}")
        except:
            print("ERROR. Los datos ingresados no son números.")
        else:
            print(os.getcwd())
        finally:
            print ("Proceso terminado.")
    elif opcion.lower()=="c":
        break
    else :
        print("ERROR. Esa opción no es válida, profavor ingrese una opcion válida.")