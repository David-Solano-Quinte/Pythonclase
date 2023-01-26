##Solano Quinte David Josue
print ("Pregunta 8")
cont=input("Registre una contraseña: ")
cont1 = cont.casefold()
cadena = input("Ingrese la contraseña: ")
cadena1 =cadena.casefold()
if cadena1 == cont1 :
    print ("La contraseña introducida coincide con la contraseña guardada.")
else :
    print("La contraseña introducida, no coincide con la contraseña guardada")