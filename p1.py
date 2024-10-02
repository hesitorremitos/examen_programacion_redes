def invertido(num):
    new = 0
    while num > 10:
        mod = num % 10
        num = (num-mod)/10
        new = (new + mod) * 10
    return int(new+num)
        

def es_perfecto(num):
    if(num == invertido(num)):
        return True
    else:
        return False
num = int(input("Digite un numero: "))

if(es_perfecto(num)):
    print(f"El numero {num} es perfecto")
else:
    print(f"El numero {num} NO es perfecto")
