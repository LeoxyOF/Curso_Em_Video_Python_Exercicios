from time import sleep
lista = list()
dc = {
    "Nome": str(input('Nome do Jogador: ')).strip().title(),
    "Partidas": int(input('Quantas partidas foram jogadas: ')),
    "Gols": lista,
}
print('-=' * 20)
for c in range(1, dc["Partidas"] + 1):
    lista.append(int(input(f'Quantos gols na partida {c}? ')))
dc['Total'] = sum(lista)
print('-=' * 20)
print(dc)
for key, valor in dc.items():
    print(f'{key} = {valor}')
    sleep(1)
print('-=' * 20)
print(f'O jogador {dc["Nome"]} jogou {len(lista)} partidas:')
for key, valor in enumerate(lista):
    print(f'    --> Na {key + 1}º Partida, fez {valor} Gols')
    sleep(1)
print(f'Fez um total de {dc["Total"]} gols')