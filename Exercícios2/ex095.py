from time import sleep
geral = []
golsa = []
dc = {}
somar = 0
while True:
    print('-' * 33)
    dc['Nome'] = str(input('Nome do jogador: ')).strip().title()
    dc["Partidas"] = int(input('Quantas partidas foram jogadas? '))
    print('-' * 33)
    for c in range(1, dc['Partidas'] + 1):
        gols = int(input(f'    >> Quantos gols na partida {c}? '))
        somar += gols
        golsa.append(gols)
    dc['Gols'] = golsa[:]
    dc['Total'] = somar
    geral.append(dc.copy())
    dc.clear()
    golsa.clear()
    somar = 0
    print('-' * 33)
    cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print('-' * 45)
print(f'{"Pos.":<10}{"Nome":^10}{"Gols":>10}{"Total":>15}')
print('-' * 45)
for key, valor in enumerate(geral):
    print(f'{key + 1:<10}{valor["Nome"]:^10}{valor["Gols"]!s:>12}{valor["Total"]:>12}')
print('-' * 45)
while True:
    qa = int(input('Mostrar dados de qual jogador? (999 imterrompe) ')) - 1
    if qa == 998:
        print('<<< PROGRAMA ENCERRADO >>>')
        break
    if qa < len(geral):
        print('-' * 45)
        print(f'Levantamento do jogador {geral[qa]["Nome"].upper()}')
        print('-' * 45)
        for key, valor in enumerate(geral[qa]['Gols']):
            print(f'Na partida {key + 1} fez "{valor}" Gols')
            sleep(1)
        print('-' * 45)
    else:
        print('-' * 45)
        print(f'Resposta incorreta! não existe este jogador na lista')
        print('-' * 45)
