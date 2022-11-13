from random import choice
print('===Aleatorizar Aluno===')
N1 = input('nome do primeiro aluno: ')
N2 = input('Nome Do Segundo Aluno: ')
N3 = input('Nome Do Terceiro Aluno: ')
N4 = input('Nome Do Quarto Aluno: ')
Resp = choice([N1, N2, N3, N4])
print(f'{Resp} Irá Limpar O Quadro')
