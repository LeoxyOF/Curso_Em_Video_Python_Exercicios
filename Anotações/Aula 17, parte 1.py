valores = [8, 4, 7, 14, 3, 78]
valores[2] = 11  # troca
# valores.append(21)  # adiciona no final
# valores.insert(2 + 1, 5)  # adiciona em tal posição
# org = valores.sort(reverse=True) #organiza
# valores.pop()  # apaga último valor
# valores.pop(2)  # apaga valor escolhido( na sua posição, não valor )
# valores.remove(8)  # apaga o valor requisitado da lista( dessa maneira ele só apaga o primeiro valor visto, não todos )
print(valores)
# print(f'Esta lista tem {len(valores)} elementos')

# lista = []

# for cont in range(0, 4):
    # lista.append(int(input('Digite um valor: ')))
# lista.sort()
# for a, b in enumerate(lista):
    # print(f'Na posição {a+1} encontrei o valor {b}')

# cópia de uma lista

a = [2, 3, 4, 7]
b = a[:]
b[2] = 9
print(f'Lista A: {a}')
print(f'Lista B: {b}')