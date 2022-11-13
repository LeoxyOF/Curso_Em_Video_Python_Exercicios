dic = {}
lista = []
soma = 0
while True:
    print("-=" * 3, f"Pessoa {len(lista) + 1}", "-=" * 3)
    dic["nome"] = str(input(f'Nome: ')).strip()
    dic["idade"] = int(input('Idade: '))
    soma += dic["idade"]
    while True:
        dic["sexo"] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dic['sexo'] in 'MF':
            break
        print('Resposta Inválida!')
    lista.append(dic.copy())
    dic.clear()
    print('-=' * 10)
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print("-=" * 30)
print(f'Dados >>>>>>')
print(f"    - O grupo tem {len(lista)} pessoas")
print(f"    - A média de idade é de {soma / len(lista):.2f} anos")
print(f'    - As Mulheres do grupo são: ', end='')
for a in lista:
    if 'F' in a["sexo"]:
        print(a["nome"], end=' ')
print()
print(f'    - Maiores de idade >>>')
for a in lista:
    if a["idade"] >= 18:
        print(f'            {a["nome"]} com {a["idade"]} anos')
print('\n<<< FIM >>>')
