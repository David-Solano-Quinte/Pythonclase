valor=(__name__ =="__main__")

def llamada ():
    from __main__ import abc
    print (abc())

def suma (n:int):
    if n>0:
        n= n + suma(n-1)
    return n

def div (a:int,b:int):
    n=a/b
    return n
