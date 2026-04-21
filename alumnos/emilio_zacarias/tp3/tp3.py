def funcionSinParametro():
    print("prueba")

funcionSinParametro()



def funcionConParametro(nombre):  
    print(f"Hola {nombre}")

funcionConParametro("emilio")


def sumaConRetorno(a, b): 
    return a + b  

print(sumaConRetorno(1, 2))

#funcion ya creada en python
lista = [1, 2, 3]

print(len(lista))  

# variable global
varGlobal = "hola"  


def saludo():
    #variable local
    varLocal = "emilio"
    print(f"Hola {varLocal}")

saludo()
print(varGlobal)
