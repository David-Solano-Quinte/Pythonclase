valor=(__name__ =="__main__")
print (valor)

def suma (n:int):
    if n>0:
        n= n + suma(n-1)
    return n

def div (a:int,b:int):
    n=a/b
    return n
