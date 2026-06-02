"""
Ejemplo de Funciones básicas en Python
"""

def saludo():
    print("Hola, Python!")
    
saludo()

def return_saludo():
    return "Hola, Python!"

print(return_saludo())

def arg_saludo(name):
    print(f"Hola {name}")
    
    
arg_saludo("Carlos Aguirre")


def args_saludo(saludo,name):
    print(f"{saludo} {name}")
    
args_saludo("Hi","Aníbal")

def arg_pred_saludo(name="San Jose"):
    print(f"Hola {name}")
    
arg_pred_saludo()


def argument_return(saludo,name):
    return f"{saludo} {name}"

print(argument_return("Bienvenidos","Programadores"))

def multiples_retornos():
    return "Hola", "San Jose"

greet, name = multiples_retornos()
print(greet)
print(name)


def argumentos_vrbles(*names):
    for name in names:
        print(f"Hola {name}!")

argumentos_vrbles("Carlos","Aníbal","Aguirre","San Jose","Manso")

def argumentos_vrbles_key(**names):
    for key, value in names.items():
        print(f"{key} {value}")

argumentos_vrbles_key(
    name="Carlos",
    name2="Aníbal",
    lastname="Aguirre",
    Lugar1="San Jose",
    Lugar2="Manso")

"""
FUNCIONES DENTRO DE FUNCIONES
"""

def funcion_externa():
    def funcion_interna():
        print("Funcion interna: Hola Funcion oculta")
    funcion_interna()

funcion_externa()


print(len("Instituto Superior San Jose i27"))
print(type(39))
print("Instituto Superior San Jose i-27".upper())

"""
Variables globales y locales
"""
global_var="Python y Github"

def hi_python():
    local_var = "Hola"
    print(f"{local_var} {global_var}")
    
    
print(global_var)
#print(local_var)esto solamente se imprime localmente dentro de la función

hi_python()


"""
EXTRA
"""

def print_numbers(text1,text2)->int:
    count = 0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(text1 + text2)
        elif number % 5 == 0:
            print(text2)
        elif number % 3 == 0:
            print(text1)
        else:
            print(number)
            count += 1
    return count
    
print(print_numbers("Te esperamos","Django"))


