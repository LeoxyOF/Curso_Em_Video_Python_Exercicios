def fatorial(num):
    f = 1
    for c in range(1, num + 1):
        f *= c
    return f


# Programa Principal
resp = int(input('Digite um valor: '))
fat = fatorial(resp)
print(f'O Fatorial de {resp} é igual á {fat}')