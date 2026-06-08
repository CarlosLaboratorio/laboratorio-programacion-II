#------------------------------------
# Funciones sin parametro ni retorno
#------------------------------------

def saludar():

    print ("Hola, estoy aprendiendo python!")

saludar()


#---------------------------
# Funciones con parametros 
#---------------------------

def saludar_persona(nombre):

    print (f"Hola {nombre}")

saludar_persona("Leandro")

#---------------------------------
# Funciones con varios parametros
#---------------------------------

def sumar(a, b):

    print ("La suma es:", a + b)

sumar(10, 5)


#------------------------
# Funciones con retorno
#------------------------

def multiplicar(a, b):
    
    return a * b

resultado = multiplicar(5, 3)
print ("Resultado:", resultado)


#-------------------------------
# Funciones dentro de funciones
#-------------------------------

def externa():

    print ("Funcion externa")

    def interna():
        
        print ("Funcion interna")

    interna()


externa()


#-------------------
# Funciones creadas
#-------------------

print ("Maximo:", max(10, 20, 30))
print ("Minimo:", min(10, 20, 30))
print ("Longitud:", len("Lab II 2026"))
print ("Suma lista:", sum([1, 2, 3, 4]))


#------------------------------
# Variables locales y globales
#------------------------------

x = 100 # Global

def ejemplo():

    x = 50 # Local
    print ("Esta variable se encuentra dentro de la funcion:", x)

ejemplo()

print ("Esta variable se encuentra fuera de la funcion:", x)




