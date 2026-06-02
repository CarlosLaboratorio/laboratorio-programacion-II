
def sum():
    result = 1 + 1
    print(result)

def sub(num1, num2):
    result = num1 - num2
    print(result)

def mult():
    result = 5 * 5
    return result

mul = mult()

print(mul)

def div(num1, num2):
    result = num1 / num2
    return result

print(div(10, 2))

def outerFun(param1, param2):

    def innerFun(param2):
        return 10 + param2
    
    result = param1 + innerFun(param2)

    return result


print(outerFun(5,10))