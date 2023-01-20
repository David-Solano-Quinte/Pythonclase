## David Josue Solano Quinte

a=int(input("""Ingrese el valor de dos numeros:
"""))
b=int(input())
def mayor(a,b):
    if a>b:
        return a
    elif a<b :
        return b
    else :
        return "Ambos numeros son iguales."
    
print (mayor(a,b))