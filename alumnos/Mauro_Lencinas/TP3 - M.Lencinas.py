""" Funciones básicas en Python """ 
def saludo():
    print("Hola, Python!")

saludo()
def return_saludo():
    return "Hola, Python!"
print(return_saludo())

def arg_saludo(name):
    print(f"Hola {name}")
arg_saludo("Mauro Lencinas")

def args_saludo(saludo,name):
    print(f"{saludo} {name}")
args_saludo("Hi","Mauro Lencinas")

def arg_pred_saludo(name="San Jose"):
    print(f"Hola {name}")
arg_pred_saludo()

def argument_return(saludo,name):
    return f"{saludo} {name}"
print(argument_return("Bienvenido", "Mauro Lencinas"))

def multiples_retornos():
    return "Hola", "San Jose"
greet, name = multiples_retornos()
print(greet)
print(name)

def argumentos_vrbles(*names):
    for name in names:
        print(f"Hola {name}!")
argumentos_vrbles("Mauro Lencinas", "San Jose", "Programadores")