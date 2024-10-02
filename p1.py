def es_perfecto(num):
    num = str(num)
    if(num == num[::-1]):
        return True
    else:
        return False

num = input("Digite un numero: ")
num = int(num)
if(es_perfecto(num)):
    print(f"El numero {num} es perfecto")
else:
    print(f"El numero {num} NO es perfecto")
