lista = []
resp = ''
while resp != 'N':
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} elementos')
print(f'Em forma decrescente fica: {lista}')
if 5 in lista:
    print(f'\033[1;32mO valor 5 se encontra na lista na posição {lista.index(5)+1}:)')
elif 5 not in lista:
    print(f'\033[1;31mNão foi encontrado o valor 5 na lista ;-;')
