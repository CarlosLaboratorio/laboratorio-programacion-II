# Rango de numeros configurable por el usuario
inicio = int(input("Inicio: "))
fin = int(input("Fin: "))

if inicio > fin:  # validacion de rango valido
    print("Error, el inicio debe ser menor al fin.")
else:
    resultado = []  # lista vacia donde se almacenan los datos
    for i in range(inicio, fin+1):
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            # append() añade cada elemento nuevo al final de la lista
            resultado.append(i)

    for i in resultado:
        print(i)
    if resultado:
        print(f"\n|--- Estadisticas ---|")
        # cuenta cuantos elementos hay en la lista
        print(f"|Total de numeros: {len(resultado)}")
        # suma todos los elementos
        print(f"|----- Suma -----: {sum(resultado)}")
        print(f"|--- Promedio ---: {sum(resultado)/len(resultado):.2f}")
        # busca el elemento mas chico
        print(f"|---- Minimo ----: {min(resultado)}")
        # busca el elemento mas grande
        print(f"|---- Maximo ----: {max(resultado)}")
