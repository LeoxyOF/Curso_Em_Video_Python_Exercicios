def soccer(jogador, gols):
    if jogador == '':
        jogador = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato'


jog = str(input("Jogador: ")).strip()
gol = str(input("Gols: ")).strip()
print(soccer(jog, gol))
