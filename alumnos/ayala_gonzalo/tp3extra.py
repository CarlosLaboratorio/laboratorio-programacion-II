

def mensaje(texto1, texto2):
    
    count = 0

    for i in range(1, 100):

        if i % 5 == 0 and i % 3 == 0:
            
            print(f"{texto1}{texto2}")
        elif i % 5 == 0:
            print(texto2)
        elif i % 3 == 0:
            print(texto1)
        else:
            print(i)
            count += 1


    return count


print(mensaje("Fizz", "Buzz"))
