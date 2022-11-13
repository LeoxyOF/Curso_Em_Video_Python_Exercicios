continuar = ''
lista = []
while True:
    abc = int(input('Digite um valor: '))
    if abc not in lista:
        lista.append(abc)
        print('Valor adicionado com sucesso!')
    else:
        print('Este valor já foi adicionado, não irei replicar!')
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar not in 'NnSs':
        while continuar not in 'NnSs':
            continuar = str(input('Resposta Inválida!, Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        lista.sort()
        break
print('-='* 20)
print(f'Os valores digitados foram {lista}')
