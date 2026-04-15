
def main():

    numInicial = 11
    numFinal = 55
    for i in range(numInicial, numFinal):
        r1 = esMultiplo(i)
        r2 = esPar(i)
        resultado(r1, r2, i)




def esMultiplo(num):
    if num % 3 != 0:
        return True
    else :
        return False
    
def esPar(num):

    if num % 2 == 0 and num != 16:
        return True
    else :
        return False

def resultado(r1, r2, num):
    if r1 & r2:
        print(num)

main()