maior = 0
menor = 0
media = 0
lista = []
for cont in range(1, 6):
    resp = int(input('Digite um valor: '))
    if cont == 1:
        lista.append(resp)
        maior = resp
        menor = resp
        print('O valor foi adicionado no final da lista!')
    if resp > maior and cont != 1 or resp == maior:
        lista.append(resp)
        maior = resp
        print(f'O valor {maior} foi adicionado no final da lista!')
    if resp < menor and cont != 1 or resp == menor:
        menor = resp
        lista.insert(0, menor)
        print(f'O valor {menor} foi adicionado na posição 0')
    if maior > resp > menor and cont != 1 or resp == media:
        lista.insert(1, resp)
        media = resp
        print(f'O valor {media} foi adicionado na posição {lista.index(resp)}')
print('-='* 30)
print(f'Os Valorem em ordem crescente fica {lista}')